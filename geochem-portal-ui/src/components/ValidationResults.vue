<script setup lang="ts">
import { computed } from 'vue'

import Message from 'primevue/message'
import Accordion from 'primevue/accordion'
import AccordionTab from 'primevue/accordiontab'

import type { ValidationReport } from '@/types'

const props = defineProps<{ report: ValidationReport }>()

const singularValues = [0, 1]

const messagesCount = computed(() => {
  return props.report.results.length
})

const violationCount = computed(() => {
  return props.report.violation_count
})

const violationText = computed(() => {
  if (singularValues.includes(violationCount.value)) {
    return 'violation'
  }

  return 'violations'
})

const warningCount = computed(() => {
  return props.report.warning_count
})

const warningText = computed(() => {
  if (singularValues.includes(warningCount.value)) {
    return 'warning'
  }

  return 'warnings'
})

const infoCount = computed(() => {
  return props.report.info_count
})

const infoText = computed(() => {
  if (singularValues.includes(infoCount.value)) {
    return 'information'
  }

  return 'informations'
})
</script>

<template>
  <h2 class="text-2xl">Validation Results</h2>
  <p>
    {{ messagesCount }}
    <template v-if="messagesCount === 1">result</template>
    <template v-else>results</template>: {{ violationCount }} {{ violationText }},
    {{ warningCount }} {{ warningText }}, {{ infoCount }} {{ infoText }}
  </p>

  <Message v-if="props.report.conforms" severity="success" :closable="false"
    >Data is conformant.</Message
  >

  <template v-if="!props.report.conforms" v-for="result in props.report.results">
    <Message v-if="result.severity == 'violation'" severity="error">
      <div class="font-bold pb-2">For {{ result.focus_node }}:</div>
      <div>{{ result.message }}</div>
    </Message>
    <Message v-else-if="result.severity == 'warning'" severity="warn">
      <div class="font-bold pb-2">For {{ result.focus_node }}:</div>
      <div>{{ result.message }}</div>
    </Message>
    <Message v-else severity="info">
      <div class="font-bold pb-2">For {{ result.focus_node }}:</div>
      <div>{{ result.message }}</div>
    </Message>
  </template>

  <div>
    <Accordion>
      <AccordionTab header="Validation Report">
        <code>
          <pre class="overflow-auto pb-6">{{ props.report.results_text }}</pre>
        </code>
      </AccordionTab>
    </Accordion>
  </div>
</template>
