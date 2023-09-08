from rdflib import Graph, RDF, SH
from pyshacl import validate as shacl_validate
from pydantic import BaseModel, constr


class ParseError(Exception):
    """This is raised when there's a parsing error into an RDFLib Graph."""


class ValidationResult(BaseModel):
    severity: constr(pattern="^(info|warning|violation)$")
    focus_node: str
    result_path: str
    message: str

    def __eq__(self, __value: object) -> bool:
        if (
            type(__value) == type(self)
            and __value.severity == self.severity
            and __value.message == self.message
        ):
            return True
        return False


class ValidationReport(BaseModel):
    conforms: bool
    results: list[ValidationResult]
    results_text: str


severity_to_str = {
    SH.Violation: "violation",
    SH.Warning: "warning",
    SH.Info: "info",
}


def validate(data: str, shacl_shapes: str) -> ValidationReport:
    """Validate RDF Turtle data with the supplied SHACL shapes.

    This is a wrapper function around `pyshacl.validate` to simplify the function signature.

    :param data: RDF Turtle data as a string.
    :param shacl_shapes: RDF Turtle descriptions of the SHACL shapes.
    """

    data_graph = Graph()
    try:
        data_graph.parse(data=data, format="text/turtle")
    except Exception as err:
        raise ParseError(f"Failed to parse input data. {err}")
    shacl_graph = Graph()
    try:
        shacl_graph.parse(data=shacl_shapes, format="text/turtle")
    except Exception as err:
        raise ParseError(f"Failed to parse SHACL shapes data. {err}")

    conforms, results_graph, results_text = shacl_validate(
        data_graph=data_graph,
        shacl_graph=shacl_graph,
        allow_infos=True,
        allow_warnings=True,
    )

    results = []

    validation_result_nodes = results_graph.subjects(RDF.type, SH.ValidationResult)
    for result_node in validation_result_nodes:
        severity_iri = results_graph.value(result_node, SH.resultSeverity)
        severity = severity_to_str[severity_iri]
        focus_node = results_graph.value(result_node, SH.focusNode)
        result_path = results_graph.value(result_node, SH.resultPath)
        message = results_graph.value(result_node, SH.resultMessage)

        results.append(
            ValidationResult(
                severity=severity,
                focus_node=focus_node,
                result_path=result_path,
                message=str(message),
            )
        )

    return ValidationReport(
        conforms=conforms, results=results, results_text=results_text
    )
