<script setup lang="ts">
import { ref, computed, watch } from 'vue'

import TabView from 'primevue/tabview'
import TabPanel from 'primevue/tabpanel'
import Textarea from 'primevue/textarea'
import Dropdown from 'primevue/dropdown'
import Fieldset from 'primevue/fieldset'
import Button from 'primevue/button'
import FileUpload from 'primevue/fileupload'
import Toast from 'primevue/toast'
import { useToast } from 'primevue/usetoast'

import ValidationResults from '@/components/ValidationResults.vue'
import qldValidator from '@/assets/qld-validator.ttl?raw'
import type { ValidationReport } from '@/types'

type Example = {
  name: string
  value: string
}

const toast = useToast()

const textareaValue = ref('')

const selectedExample = ref<Example>()
const examples = ref([
  {
    name: 'A demonstration dataset (valid)',
    description: 'Contains an observation, sample, feature of interest and related vocabularies.',
    value: `PREFIX dcat: <http://www.w3.org/ns/dcat#>
PREFIX ex: <http://example.com/>
PREFIX geo: <http://www.opengis.net/ont/geosparql#>
PREFIX op: <https://linked.data.gov.au/def/observable-properties/>
PREFIX prov: <http://www.w3.org/ns/prov#>
PREFIX rc: <http://def.isotc211.org/iso19115/-1/2018/CitationAndResponsiblePartyInformation/code/CI_RoleCode/>
PREFIX sdo: <https://schema.org/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX sosa: <http://www.w3.org/ns/sosa/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

ex:dataset-x
    a dcat:Dataset ;
    sdo:name "Dataset X" ;
    sdo:description "A demonstration dataset" ;
    sdo:dateCreated "2023-09-26"^^xsd:date ;
    sdo:dateModified "2023-09-27T14:30"^^xsd:dateTime ;
    prov:qualifiedAttribution [
        a prov:Attribution ;
        prov:agent ex:a-company ;
        prov:hadRole rc:originator ;
    ] ;
.

ex:obs-1
    a sosa:Observation ;
    sosa:usedProcedure <https://w3id.org/geochem/1.0/analyticalmethod/chromatographyanalysis> ;
    sosa:madeBySensor ex:sensor-c ;
    sosa:observedProperty <https://linked.data.gov.au/def/observable-properties/amount-of-gold> ;
    sosa:hasFeatureOfInterest ex:sample-d ;
    sosa:phenomenonTime "2023-05-11"^^xsd:date ;
    sosa:hasResult
        ex:result-e ,
        ex:result-f ;
.

ex:procedure-b
    a skos:Concept ;
    skos:prefLabel "Procedure B" ;
    skos:definition "A method for assessing the amount of gold in a sample" ;
.

ex:sensor-c
    a skos:Concept ;
    skos:prefLabel "Sensor C" ;
    skos:definition "A particular machine for assessing gold content in rock samples" ;
.

ex:sample-d
    a sosa:Sample ;
    sdo:name "Sample C" ;
    sdo:additionalType ex:soil-sample ;
    sdo:description "A soil sample from Sandy Creek" ;
    sdo:location "Zillmere Rock Store: Zone 4, Shelf N, Box 3" ;
    sosa:isSampleOf <https://linked.data.gov.au/dataset/qldgeofeatures/AnakieProvince> ;
.

ex:result-e
    sdo:value 0.027  ;
    sdo:unitCode <https://qudt.org/vocab/unit/PPM> ;
.

ex:result-f
    sdo:value 27.0 ;
    sdo:unitCode <https://qudt.org/vocab/unit/PPB> ;
.

<https://linked.data.gov.au/dataset/qldgeofeatures/AnakieProvince>
    a sosa:FeatureOfInterest , geo:Feature ;
    geo:hasGeometry [
        a geo:Geometry ;
        geo:asWKT "POLYGON((146.850699 -23.704934,146.850699 -20.863771,148.028386 -20.863771,148.028386 -23.704934,146.850699 -23.704934))"^^geo:wktLiteral ;
    ] ;
.`
  },
  {
    name: 'A demonstration dataset (invalid)',
    description:
      'Missing result and observable property in observation and qualified attribution in the dataset.',
    value: `# Dataset missing 1+ prov:qualifiedAttribution
#
# Observation missing 1 sosa:hasResult
#
# Observation refers to an unknown Observed Property value
#
PREFIX dcat: <http://www.w3.org/ns/dcat#>
PREFIX ex: <http://example.com/>
PREFIX geo: <http://www.opengis.net/ont/geosparql#>
PREFIX op: <https://linked.data.gov.au/def/observable-properties/>
PREFIX prov: <http://www.w3.org/ns/prov#>
PREFIX rc: <http://def.isotc211.org/iso19115/-1/2018/CitationAndResponsiblePartyInformation/code/CI_RoleCode/>
PREFIX sdo: <https://schema.org/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX sosa: <http://www.w3.org/ns/sosa/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

ex:dataset-x
    a dcat:Dataset ;
    sdo:name "Dataset X" ;
    sdo:description "A demonstration dataset" ;
    sdo:dateCreated "2023-09-26"^^xsd:date ;
    sdo:dateModified "2023-09-27T14:30"^^xsd:dateTime ;
    # prov:qualifiedAttribution [
    #     a prov:Attribution ;
    #     prov:agent ex:a-company ;
    #     prov:hadRole rc:originator ;
    # ] ;
.

ex:obs-1
    a sosa:Observation ;
    sosa:usedProcedure <https://w3id.org/geochem/1.0/analyticalmethod/chromatographyanalysis> ;
    sosa:madeBySensor ex:sensor-c ;
    # sosa:observedProperty <http://unknown-vocab.org/amount-of-gold> ;
    sosa:hasFeatureOfInterest ex:sample-d ;
    sosa:phenomenonTime "2023-05-11"^^xsd:date ;
    # sosa:hasResult
    #     ex:result-e ,
    #     ex:result-f ;
.

ex:procedure-b
    a skos:Concept ;
    skos:prefLabel "Procedure B" ;
    skos:definition "A method for assessing the amount of gold in a sample" ;
.

ex:sensor-c
    a skos:Concept ;
    skos:prefLabel "Sensor C" ;
    skos:definition "A particular machine for assessing gold content in rock samples" ;
.

ex:sample-d
    a sosa:Sample ;
    sdo:name "Sample C" ;
    sdo:additionalType ex:soil-sample ;
    sdo:description "A soil sample from Sandy Creek" ;
    sdo:location "Zillmere Rock Store: Zone 4, Shelf N, Box 3" ;
    sosa:isSampleOf <https://linked.data.gov.au/dataset/qldgeofeatures/AnakieProvince> ;
.

ex:result-e
    sdo:value 0.027  ;
    sdo:unitCode <https://qudt.org/vocab/unit/PPM> ;
.

ex:result-f
    sdo:value 27.0 ;
    sdo:unitCode <https://qudt.org/vocab/unit/PPB> ;
.

<https://linked.data.gov.au/dataset/qldgeofeatures/AnakieProvince>
    a sosa:FeatureOfInterest , geo:Feature ;
    geo:hasGeometry [
        a geo:Geometry ;
        geo:asWKT "POLYGON((146.850699 -23.704934,146.850699 -20.863771,148.028386 -20.863771,148.028386 -23.704934,146.850699 -23.704934))"^^geo:wktLiteral ;
    ] ;
.`
  }
])

const defaultValidator = { name: 'QLD Validator', value: qldValidator }
const selectedValidator = ref(defaultValidator)
const validators = ref([defaultValidator])
const report = ref<ValidationReport | null>(null)
const isValidating = ref(false)

const inputValue = computed(() => {
  if (selectedExample.value) {
    return selectedExample.value.value
  } else {
    return textareaValue.value
  }
})

const handleValidateButtonClick = async () => {
  isValidating.value = true
  report.value = null

  const response = await fetch('/api/v1/validate', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ data: inputValue.value, shacl_shapes: selectedValidator.value.value })
  })

  report.value = await response.json()
  isValidating.value = false
}

const onAdvancedUpload = () => {
  toast.add({ severity: 'info', summary: 'Success', detail: 'File Uploaded', life: 3000 })
}

watch([inputValue, selectedValidator], () => {
  report.value = null
})
</script>

<template>
  <div class="space-y-6">
    <p>Validate geochemistry data via text input or file upload.</p>

    <Fieldset legend="Input">
      <TabView>
        <TabPanel header="Text">
          <div>
            Optionally load an example:
            <Dropdown
              v-model="selectedExample"
              :options="examples"
              optionLabel="name"
              placeholder="Select an example"
              showClear
              class="ml-4"
            >
              <template #value="slotProps">
                <div v-if="slotProps.value">
                  <div>{{ slotProps.value.name }}</div>
                </div>
                <div v-else="">
                  {{ slotProps.placeholder }}
                </div>
              </template>
              <template #option="slotProps">
                <div class="font-medium">{{ slotProps.option.name }}</div>
                <div>{{ slotProps.option.description }}</div>
              </template>
            </Dropdown>
          </div>

          <div class="pt-4">
            <Textarea
              v-if="selectedExample"
              autoResize
              rows="5"
              placeholder="Input text data"
              style="width: 100%"
              :value="selectedExample.value"
              disabled
            />
            <Textarea
              v-else
              autoResize
              rows="5"
              placeholder="Input text data"
              style="width: 100%"
              v-model="textareaValue"
            />
          </div>
        </TabPanel>

        <TabPanel header="File">
          <div class="card">
            <Toast />
            <FileUpload
              name="demo[]"
              url="./upload.php"
              @upload="onAdvancedUpload()"
              :multiple="true"
              accept="image/*"
              :maxFileSize="1000000"
            >
              <template #empty>
                <p>Drag and drop files to here to upload.</p>
              </template>
            </FileUpload>
          </div>
        </TabPanel>
      </TabView>
    </Fieldset>

    <div>
      Validate data with:
      <Dropdown
        v-model="selectedValidator"
        :options="validators"
        optionLabel="name"
        placeholder="Select a validator"
        showClear
        class="ml-4"
      >
      </Dropdown>
    </div>

    <Button
      type="button"
      :disabled="!inputValue || !selectedValidator"
      :loading="isValidating"
      label="Validate"
      icon="pi pi-wrench"
      @click="handleValidateButtonClick"
      class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800"
    >
    </Button>

    <div v-if="report" class="pt-8">
      <hr />
      <ValidationResults v-if="report" :report="report" />
    </div>
  </div>

  <div class="pt-14 pb-8">
    <hr />
    <h2 class="text-2xl">Data Submission</h2>
    <p>Input data can be submitted to GSQ if validation has no violations.</p>
    <div class="pt-8">
      <Button
        disabled
        class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800"
      >
        Submit data
      </Button>
      <p><em>Data submission will be implemented at a later date.</em></p>
    </div>
  </div>
</template>

<style>
.p-tabview .p-tabview-nav li.p-highlight .p-tabview-nav-link {
  @apply text-[#414141] border-b-[#414141];
}

.p-button {
  @apply bg-blue-700;
}

.p-fileupload-choose:not(.p-disabled):hover {
  @apply bg-blue-800;
}

.p-button:enabled:hover {
  @apply bg-blue-800;
}

div.p-dropdown-items-wrapper div.flex.align-items-center {
  display: block !important;
}
</style>
