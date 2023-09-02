<script lang="ts" setup>
import { RouterLink, RouterView } from 'vue-router'

import Header from './components/Header.vue'
import Footer from './components/Footer.vue'

const globalCss = import.meta.env.BASE_URL + 'globals.css'
</script>

<template>
  <link rel="stylesheet" :href="globalCss" />
  <link
    rel="preconnect stylesheet"
    href="https://fonts.googleapis.com/css2?family=Fira+Sans:ital,wght@0,600;0,700;1,600;1,700&amp;family=Lato:wght@300;400;700;900&amp;display=swap"
  />

  <div class="app">
    <Header />

    <div class="bg-[#f5f5f5] mb-4 nav-border">
      <div class="container mx-auto">
        <nav id="main-nav" class="flex space-x-6 text-lg text-[#414141]">
          <div class="py-4">
            <RouterLink to="/">Home</RouterLink>
          </div>
          <div class="py-4">
            <RouterLink to="/about">About</RouterLink>
          </div>
        </nav>
      </div>
    </div>

    <div id="content" class="container mx-auto my-4">
      <RouterView />
    </div>

    <Footer />
  </div>
</template>

<style scoped>
@import '/public/bootstrap.min.css';

.nav-border {
  border-bottom: 8px solid #c14213;
}
</style>

<style scoped>
.router-link-active {
  font-weight: bold;
}

.app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

footer {
  margin-top: auto;
}

td {
  padding: 10px !important;
}

#page-heading > h1 {
  color: rgb(242, 242, 242);
}

.qgds__header-brand-image {
  color: #022a50;
}

.qgds__header-brand-sitename:hover {
  color: #022a50;
}

.qgds__header__pre-header-url {
  font-size: 16px;
  font-weight: 400;
  line-height: 24px;
}

.prez-app > main {
  background-color: rgb(245, 245, 245);
}

#nav-header > h2 {
  color: white !important;
}
</style>
