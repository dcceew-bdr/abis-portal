<script lang="ts" setup>
const archImg = import.meta.env.BASE_URL + 'aws-architecture.png'
</script>

<template>
  <main>
    <h1 class="text-4xl pb-4">Portal System</h1>
    <img src="@/assets/aws-architecture.svg" alt="Portal technical architecture" style="max-width:1000px;" />
    <p>This portal system is a tiny web interface and Application Programming Interface (API) back-end that really only contains several validator data files, some example ABIS data files, copies of the vocabularies listed and then a few pages of static web content.</p>
    <p>The entire system's code is available online at <a href="https://github.com/Kurrawong/abis-portal">https://github.com/Kurrawong/abis-portal</a>.</p>
    <p>There is a small bit of logic to combine the validators and elements of the vocabularies to allow for validation with value checking, but that's all.</p>
    <p></p>
    <p>In time, this Portal may be replaced by a more fully-features system delivered by DCCEEW that performs the functions you see here and also allows for some form of data submission too.</p>
    <h3>Technicals</h3>
    <p>As per the image above, this system uses serverless technology to operate: static web files in web-accessible storage and an AWS Lambda function to run the API.</p>
  </main>
</template>
