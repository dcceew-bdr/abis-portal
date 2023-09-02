<template>
  <div class="qgds__header__pre-header">
    <nav class="qgds__skip-link" aria-label="skip links" tabindex="-1">
      <a class="qgds__skip-link__link" href="#content">Skip to main content</a>
      <a class="qgds__skip-link__link" href="#main-nav">Skip to main navigation</a>
    </nav>
    <div class="container-fluid">
      <a href="https://www.resources.qld.gov.au" title="Queensland Government">
        <span class="qgds__header__pre-header-url">resources.qld.gov.au</span>
        <span class="qgds__pre-header-brand-image"
          ><span class="visually-hidden">Queensland Government website</span>

          <svg><use href="/qg-coa-white.svg#qg-coa-white"></use></svg>
        </span>
      </a>
      <a class="qgds__header__pre-header-cta" href="https://www.resources.qld.gov.au/contact-us">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="19" height="19">
          <path
            d="M511.2 387l-23.25 100.8c-3.266 14.25-15.79 24.22-30.46 24.22C205.2 512 0 306.8 0 54.5c0-14.66 9.969-27.2 24.22-30.45l100.8-23.25C139.7-2.602 154.7 5.018 160.8 18.92l46.52 108.5c5.438 12.78 1.77 27.67-8.98 36.45L144.5 207.1c33.98 69.22 90.26 125.5 159.5 159.5l44.08-53.8c8.688-10.78 23.69-14.51 36.47-8.975l108.5 46.51C506.1 357.2 514.6 372.4 511.2 387z"
          ></path>
        </svg>
        <span class="qgds__header__pre-header-cta__text">Contact us</span>
      </a>
    </div>
  </div>
  <header>
    <div class="container-fluid qgds__header">
      <div class="qgds__header-brand">
        <div class="qgds__header-brand-image">
          <a href="http://www.qld.gov.au" title="Queensland Government"
            ><span class="visually-hidden">Queensland Government website</span
            ><svg>
              <use href="/qg-coa-header.svg#qg-coa"></use></svg
          ></a>
        </div>
        <div class="qgds__header-brand-sitename">
          <h4><a href="/">Department of Resources</a></h4>
        </div>
      </div>
      <div class="qgds__header-search">
        <div class="qgds__header-search-form collapse" id="qgds__header-search-form"></div>
      </div>
    </div>
  </header>
</template>

<style scoped>
@import '/public/bootstrap.min.css';
</style>
