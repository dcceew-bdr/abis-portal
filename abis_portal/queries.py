from textwrap import dedent


def get_oc_to_o_query() -> str:
    return dedent(
        """
        # Applies certain properties if present for an Observation Collection
        # to each Observation within it

        PREFIX sdo: <https://schema.org/>
        PREFIX sosa: <http://www.w3.org/ns/sosa/>

        INSERT {
            ?o ?obs_pred ?obj
        }
        WHERE {
            ?oc sosa:hasMember ?o .
            {
                SELECT ?oc ?obs_pred ?obj
                WHERE {
                    VALUES ?obs_pred {
                        sdo:marginOfError
                        sosa:hasFeatureOfInterest
                        sosa:madeBySensor
                        sosa:observedProperty
                        sosa:phenomenonTime
                        sosa:usedProcedure
                    }

                    {
                        ?oc
                            a sosa:ObservationCollection ;
                            ?obs_pred ?obj ;
                        .
                    }
                }
            }
        }
    """
    )
