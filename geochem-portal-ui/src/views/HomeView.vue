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
      <h1 class="text-4xl pb-4">GSQ Geochemistry Data Portal</h1>
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

    <div class="flex flex-row">
      <article class="lg:basis-2/3">
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
