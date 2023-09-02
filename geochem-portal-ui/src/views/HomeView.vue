<script setup lang="ts">
import { ref } from 'vue'

import Button from 'primevue/button'
import Sidebar from 'primevue/sidebar'

import Validator from '@/components/Validator.vue'
import Info from '@/components/Info.vue'

const visibleRight = ref(false)
</script>

<template>
  <main>
    <div class="flex">
      <h1 class="text-4xl pb-4">GSQ Geochemistry Data Validator</h1>
      <div class="grow"></div>
      <div class="block lg:hidden place-self-center">
        <Button
          icon="pi pi-info-circle"
          @click="visibleRight = true"
          class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800"
        ></Button>
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
