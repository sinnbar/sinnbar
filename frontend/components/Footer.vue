<template>
  <footer class="footer mt-6 has-background-light">
    <section>
      <div class="container column is-10">
        <div class="container is-fullhd is-fluid">
          <div class="columns is-mobile">
            <div class="column">
              <p>&#160;</p>
              <a href="mailto:zusammen@sinnbar.de"
                ><p class="has-text-left">kontakt</p></a
              >
              <a href="https://www.instagram.com/sinnbar_/" target="_blank"
                ><p class="has-text-left">instagram</p></a
              >
              <a href="https://www.facebook.com/sinnbar_/"
                ><p class="has-text-left">facebook</p></a
              >
            </div>
            <div class="column">
              <nuxt-link to="/agb"><p class="has-text-right">agb</p></nuxt-link>
              <nuxt-link to="/datenschutz"
                ><p class="has-text-right">datenschutz</p></nuxt-link
              >
              <nuxt-link to="/impressum"
                ><p class="has-text-right">impressum</p></nuxt-link
              >
              <nuxt-link to="/widerufsbelehrung"
                ><p class="has-text-right">widerufsbelehrung</p></nuxt-link
              >
            </div>
          </div>
        </div>
      </div>
    </section>
  </footer>
</template>

<script>
export default {}
</script>
