<script setup lang="ts">
import Message from 'primevue/message'
import Accordion from 'primevue/accordion'
import AccordionTab from 'primevue/accordiontab'
</script>

<template>
  <h2 class="text-2xl">Validation Results</h2>
  <p>2 messages: 2 violations, 0 warnings, 0 infos</p>
  <Message severity="error"
    >For :data-1: The object MUST indicate the sample type as an IRI value using the property
    geochem:sampleType.</Message
  >
  <Message severity="error"
    >For :data-1: The object MUST indicate the sampling activity which created this sample using the
    property sosa:isResultOf.</Message
  >
  <Accordion>
    <AccordionTab header="Validation Report">
      <p>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
        labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco
        laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in
        voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat
        cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
      </p>
    </AccordionTab>
  </Accordion>
</template>
