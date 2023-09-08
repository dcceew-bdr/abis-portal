<script setup lang="ts">
import Message from 'primevue/message'
import Accordion from 'primevue/accordion'
import AccordionTab from 'primevue/accordiontab'

import type { ValidationReport } from '@/types'

const props = defineProps<{ report: ValidationReport }>()
</script>

<template>
  <h2 class="text-2xl">Validation Results</h2>
  <p>2 messages: 2 violations, 0 warnings, 0 infos</p>

  <Message v-for="result in props.report.results"
    ><div class="font-bold pb-2">For {{ result.focus_node }}:</div>
    <div>{{ result.message }}</div></Message
  >

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
