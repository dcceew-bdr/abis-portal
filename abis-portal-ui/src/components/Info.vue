<script setup lang="ts">
const props = defineProps<{ large: boolean }>()
</script>

<template>
  <aside class="lg:col-span-1" :class="{ 'lg:block hidden': props.large }">
    <article class="bg-[#f8f8fa] p-5">
      <h2 class="text-xl">ABIS Documentation</h2>

      <article>
        <h3 class="text-base">The Standard</h3>
        <ul class="list-disc pl-[2rem]">
          <li><a href="http://linked.data.gov.au/def/abis/overview" target="_blank">ABIS Overview - 1-pager <i class="pi pi-external-link"></i></a></li>
          <li><a href="http://linked.data.gov.au/def/abis/spec" target="_blank">ABSI Specification <i class="pi pi-external-link"></i></a></li>
          <li><a href="http://linked.data.gov.au/def/abis" target="_blank">Standard Definition - all the ABIS parts <i class="pi pi-external-link"></i></a></li>
        </ul>
      </article>

      <article>
        <h3 class="text-base">Profiles of ABIS</h3>
        <p><em><RouterLink to="/profiles">What are Profiles?</RouterLink></em></p>
        <ul class="list-disc pl-[2rem]">
          <li><a href="http://linked.data.gov.au/def/abis/spec#profile-bdr" target="_blank">Biodiversity Data Repository Profile <i class="pi pi-external-link"></i></a></li>
        </ul>
      </article>

      <article>
        <h3 class="text-base">Vocabularies</h3>
        <p><em><RouterLink to="/vocabs">What vocabularies does use of ABIS require?</RouterLink></em></p>
        <ul class="list-disc pl-[2rem]">
          <li><a href="https://linkeddata.tern.org.au/viewer/tern/vocabulary/" target="_blank">TERN Vocabularies <i class="pi pi-external-link"></i></a></li>
          <li>
            BDR System Vocabularies
            <ul>
              <li><a href="http://linked.data.gov.au/def/abis" target="_blank">Voc X <i class="pi pi-external-link"></i></a></li>
              <li><a href="http://linked.data.gov.au/def/abis" target="_blank">Voc Y <i class="pi pi-external-link"></i></a></li>
            </ul>
          </li>
        </ul>
      </article>

      <article>
        <h3 class="text-base">System Information</h3>
        <p><em><RouterLink to="/system">What is this Portal system?</RouterLink></em></p>
        <ul class="list-disc pl-[2rem]">
          <li><a href="#">Portal Version 0.0.1</a></li>
        </ul>
      </article>

      <article>
        <h3 class="text-base">Related Specifications</h3>
        <ul class="list-disc pl-[2rem]">
          <li><a href="https://kurrawong.github.io/nsl-model/spec.html">National Species List Data Model</a></li>
        </ul>
      </article>
    </article>
  </aside>
</template>
