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

import ValidationFailure from '@/components/examples/ValidationFailure.vue'
import ValidationSuccess from '@/components/examples/ValidationSuccess.vue'

type Example = {
  name: string
  value: string
}

const toast = useToast()

const textareaValue = ref('')

const selectedExample = ref<Example>()
const examples = ref([
  {
    name: 'rock sample (valid)',
    description: 'A valid rock sample in RDF Turtle.',
    value: `PREFIX : <https://example.com/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX sosa: <http://www.w3.org/ns/sosa/>

:data-1
    a sosa:Sample ;
    rdfs:label "A valid sample" ;
.`
  },
  {
    name: 'rock sample (invalid)',
    description: 'An invalid rock sample in RDF Turtle.',
    value: `PREFIX : <https://example.com/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX sosa: <http://www.w3.org/ns/sosa/>

:data-1
    a sosa:Sample ;
    rdfs:label "An invalid sample" ;
.`
  }
])

const defaultValidator = { name: 'QLD Validator' }
const selectedValidator = ref(defaultValidator)
const validators = ref([defaultValidator])
const validated = ref(false)

const inputValue = computed(() => {
  if (selectedExample.value) {
    return selectedExample.value.value
  } else {
    return textareaValue.value
  }
})

const valid = computed(() => {
  if (inputValue.value.includes('A valid sample')) {
    return true
  }
  return false
})

const handleValidateButtonClick = () => {
  validated.value = true
}

const onAdvancedUpload = () => {
  toast.add({ severity: 'info', summary: 'Success', detail: 'File Uploaded', life: 3000 })
}

watch([inputValue, selectedValidator], () => {
  validated.value = false
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
      :disabled="!inputValue || !selectedValidator"
      @click="handleValidateButtonClick"
      class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800"
    >
      Validate
    </Button>

    <div v-if="validated" class="pt-8">
      <hr />
      <ValidationSuccess v-if="valid" />
      <ValidationFailure v-else />
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
