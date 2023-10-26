<script setup lang="ts">
import { ref } from 'vue'

import Sidebar from 'primevue/sidebar'

import Validator from '@/components/Validator.vue'
import Info from '@/components/Info.vue'

const visibleRight = ref(false)
</script>

<template>
  <main>
    <div class="flex">
      <h1 class="text-4xl pb-4">ABIS Portal</h1>
      <div class="grow"></div>
      <div class="block lg:hidden place-self-center">
        <button
          icon="pi pi-info-circle"
          @click="visibleRight = true"
          class="border-0 text-white bg-[#225578] hover:bg-[#1c4764] cursor-pointer focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-3 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800"
        >
          <i class="pi pi-info-circle align-middle"></i>
        </button>
      </div>
    </div>

    <div class="lg:grid lg:grid-cols-3">
      <article class="lg:col-span-2">
        <section>
          <div class="pt-4 pr-4">
            <div style="display:grid;">
              <div style="grid-column:1; padding:5px;">
                <h3>About</h3>
                <p>This is a one-stop-shop for <a href="https://linked.data.gov.au/def/abis">ABIS - the Australian Biodiversity Information Standard</a> built for <a href="https://github.com/AusBIGG/">AusBIGG</a> by <a href="">BDR Project staff at DCCEEW</a>. For more information, contact them!</p>
                <h4>Information about ABIS</h4>
                <p>All you could want to know about ABIS is linked to on the right.</p>
              </div>
              <div style="grid-column:2; padding:5px;">
                <h3>Uses</h3>
                <h4>Validation</h4>
                <p>Below you can validate ABIS data, using one of the several validators for ABIS and its profiles.</p>
                <h4>Vocabularies</h4>
                <p>Use of ABIS is dependent on many vocabularies. See the list of them to the right.</p>
              </div>
            </div>
          </div>
        </section>
        <section>
          <div class="pt-4 pr-4">
            <Validator />
          </div>
        </section>
      </article>

      <Sidebar v-model:visible="visibleRight" position="right">
        <Info :large="false" />
      </Sidebar>
      <Info large />
    </div>
  </main>
</template>

<style>
.p-sidebar .p-sidebar-header,
.p-sidebar-content {
  @apply bg-[#f8f8fa];
}

.p-sidebar .p-sidebar-content {
  @apply px-0;
}
</style>
