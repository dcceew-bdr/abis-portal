<script setup lang="ts">
const props = defineProps<{ large: boolean }>()
</script>

<template>
  <aside class="lg:col-span-1" :class="{ 'lg:block hidden': props.large }">
    <article class="bg-[#f8f8fa] p-5">
      <h2 class="text-xl">Documentation</h2>

      <article>
        <h3 class="text-base">ABIS</h3>
        <ul class="list-disc pl-[2rem]">
          <li><a href="http://linked.data.gov.au/def/abis" target="_blank">Standard Definition<i class="pi pi-external-link"></i></a></li>
          <li><a href="http://linked.data.gov.au/def/abis/guidance" target="_blank">Guidance (intro doc)<i class="pi pi-external-link"></i></a></li>
          <li><a href="http://linked.data.gov.au/def/abis/spec" target="_blank">Specification (formal rules)<i class="pi pi-external-link"></i></a></li>
        </ul>
      </article>

      <article>
        <h3 class="text-base">Profiles of ABIS</h3>
        <ul class="list-disc pl-[2rem]">
          <li><a href="http://linked.data.gov.au/def/abis" target="_blank">Biodiversity Data Repository Profile<i class="pi pi-external-link"></i></a></li>
        </ul>
      </article>

      <article>
        <h3 class="text-base">Vocabularies</h3>
        <ul class="list-disc pl-[2rem]">
          <li>
            TERN Vocabularies
            <ul>
              <li><a href="http://linked.data.gov.au/def/abis" target="_blank">Biodiversity Data Repository Profile<i class="pi pi-external-link"></i></a></li>
              <li><a href="http://linked.data.gov.au/def/abis" target="_blank">Biodiversity Data Repository Profile<i class="pi pi-external-link"></i></a></li>
            </ul>
          </li>
          <li>
            Other Vocabularies
            <ul>
              <li><a href="http://linked.data.gov.au/def/abis" target="_blank">Biodiversity Data Repository Profile<i class="pi pi-external-link"></i></a></li>
              <li><a href="http://linked.data.gov.au/def/abis" target="_blank">Biodiversity Data Repository Profile<i class="pi pi-external-link"></i></a></li>
            </ul>
          </li>
        </ul>
      </article>

      <article>
        <h3 class="text-base">System Information</h3>
        <ul class="list-disc pl-[2rem]">
          <li><a href="#">Portal Version X.X.X</a></li>
        </ul>
      </article>
    </article>
  </aside>
</template>
