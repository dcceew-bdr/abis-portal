<script setup lang="ts">
import Message from 'primevue/message'
import Accordion from 'primevue/accordion'
import AccordionTab from 'primevue/accordiontab'

import type { ValidationReport } from '@/types'

const props = defineProps<{ report: ValidationReport }>()
</script>

<template>
  <h2 class="text-2xl">Validation Results</h2>
  <p>0 messages: 0 violations, 0 warnings, 0 infos</p>

  <Message severity="success" :closable="false">Data is conformant.</Message>

  <Accordion>
    <AccordionTab header="Validation Report">
      <pre>{{ props.report.results_text }}</pre>
    </AccordionTab>
  </Accordion>
</template>
