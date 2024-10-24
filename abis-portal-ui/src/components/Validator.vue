<script setup lang="ts">
import { ref, computed, watch } from 'vue'
import type { Ref } from 'vue'

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
import examplesData from '@/examples'
import type { ValidationReport } from '@/types'

type Example = {
  name: string
  value: string
}

const toast = useToast()

const activeTab = ref(0)
const textareaValue = ref('')
const fileInput: Ref<HTMLInputElement | null> = ref(null)
const fileSelected = ref(false)
const formatValues = [
  { name: 'JSON', value: 'application/json' },
  { name: 'JSON-LD', value: 'application/ld+json' },
  { name: 'RDF Turtle', value: 'text/turtle' },
  { name: 'Excel', value: 'application/vnd.ms-excel' }
]
const formatValue = ref(formatValues[2])

const selectedExample = ref<Example | null>(null)
const examples = ref(examplesData)

const defaultValidator = { name: 'BDR Validator' }
const selectedValidator = ref(defaultValidator)
const validators = ref([defaultValidator, {name: 'ABIS Validator'}, { name: 'TERN Ontology Validator' }])
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

  try {
    const response = await fetch('/api/v1/validate', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        data: inputValue.value,
        shacl_shapes: selectedValidator.value.name,
        format: formatValue.value.value
      })
    })

    if (response.status == 200) {
      report.value = await response.json()
    } else {
      const data = await response.json()
      throw new Error(
        `Request to the server failed with status ${response.status}. Message: ${data['detail']}`
      )
    }
  } catch (err) {
    toast.add({ severity: 'error', summary: 'Error', detail: err })
  }
  isValidating.value = false
}

watch([inputValue, selectedValidator], () => {
  report.value = null
})

const handleFileInput = async (event: Event) => {
  const target = event.target as HTMLInputElement
  const files = target.files
  if (files && files.length > 0) {
    const file = files[0]
    textareaValue.value = await file.text()
    fileSelected.value = true
  } else {
    textareaValue.value = ''
    fileSelected.value = false
  }
}

const handleFileInputClearClick = () => {
  textareaValue.value = ''
  if (fileInput.value) {
    fileInput.value.value = ''
  }

  fileSelected.value = false
}

const handleTabChange = (event: Event, tabIndex: Number) => {
  textareaValue.value = ''
  selectedExample.value = null
  if (fileInput.value) {
    fileInput.value.value = ''
  }

  fileSelected.value = false
}
</script>

<template>
  <Toast />
  <div class="space-y-6">
    <h3>Validate Data</h3>

    <Fieldset legend="Input">
      <TabView v-model:activeIndex="activeTab" @tabChange="handleTabChange">
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
            <input
              ref="fileInput"
              type="file"
              accept=".ttl,.xlsx,.json"
              @change="handleFileInput"
            />
            <button v-if="fileSelected" @click="handleFileInputClearClick">
              <i class="pi pi-times"></i>
            </button>
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

.p-toast {
  @apply opacity-100;
}

.p-toast .p-toast-message {
  @apply bg-white opacity-100;
}
</style>
