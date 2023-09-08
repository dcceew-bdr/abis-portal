<script setup lang="ts">
const props = defineProps<{ large: boolean }>()
</script>

<template>
  <aside class="lg:col-span-1" :class="{ 'lg:block hidden': props.large }">
    <article class="bg-[#f8f8fa] p-5">
      <h2 class="text-xl">Geochemistry Data System Documentation</h2>

      <article>
        <h3 class="text-base">Data Submission Formats</h3>
        <ul class="list-disc pl-[2rem]">
          <li><a href="#">GSQ Excel template</a></li>
          <li><a href="#">JSON</a></li>
          <li><a href="#">RDF</a></li>
        </ul>
      </article>

      <article>
        <h3 class="text-base">Geochemistry Standards</h3>
        <ul class="list-disc pl-[2rem]">
          <li><a href="#">Conceptual Model</a></li>
        </ul>
      </article>

      <article>
        <h3 class="text-base">OpenAPI Specification</h3>
        <ul class="list-disc pl-[2rem]">
          <li><a href="#">Geochemistry Validation API</a></li>
        </ul>
      </article>

      <article>
        <h3 class="text-base">System Information</h3>
        <ul class="list-disc pl-[2rem]">
          <li><a href="#">Version 0.1.0-dev.0</a></li>
        </ul>
      </article>
    </article>
  </aside>
</template>
