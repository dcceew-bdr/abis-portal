<script setup lang="ts">
import { ref, computed } from 'vue'

import TabView from 'primevue/tabview'
import TabPanel from 'primevue/tabpanel'
import Textarea from 'primevue/textarea'
import Dropdown from 'primevue/dropdown'
import Message from 'primevue/message'
import Accordion from 'primevue/accordion'
import AccordionTab from 'primevue/accordiontab'
import Fieldset from 'primevue/fieldset'
import Button from 'primevue/button'
import FileUpload from 'primevue/fileupload'
import Toast from 'primevue/toast'
import { useToast } from 'primevue/usetoast'

const toast = useToast()

const textareaValue = ref('')

const selectedExample = ref()
const examples = ref([
  {
    name: 'rock sample (valid)',
    value: `PREFIX : <https://example.com/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX sosa: <http://www.w3.org/ns/sosa/>

:data-1
    a sosa:Sample ;
    rdfs:label "A sample" ;
.`
  },
  { name: 'rock sample (invalid)', value: 'BR' }
])

const defaultValidator = { name: 'QLD Validator' }
const selectedValidator = ref(defaultValidator)
const validators = ref([defaultValidator])

const inputValue = computed(() => {
  if (selectedExample.value) {
    return selectedExample.value.value
  } else {
    return textareaValue.value
  }
})

const handleValidateButtonClick = () => {
  console.log(inputValue.value)
}

const onAdvancedUpload = () => {
  toast.add({ severity: 'info', summary: 'Success', detail: 'File Uploaded', life: 3000 })
}
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
      :disabled="!inputValue"
      @click="handleValidateButtonClick"
      class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800"
    >
      Validate
    </Button>

    <div class="pt-8">
      <hr />
      <h2 class="text-2xl">Validation Results</h2>
      <p>2 messages: 2 violations, 0 warnings, 0 infos</p>
      <Message severity="error"
        >For :data-1: The object MUST indicate the sample type as an IRI value using the property
        geochem:sampleType.</Message
      >
      <Message severity="error"
        >For :data-1: The object MUST indicate the sampling activity which created this sample using
        the property sosa:isResultOf.</Message
      >
      <Accordion>
        <AccordionTab header="Validation Report">
          <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
            incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud
            exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure
            dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
            Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt
            mollit anim id est laborum.
          </p>
        </AccordionTab>
      </Accordion>
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
    </div>
  </div>
</template>
