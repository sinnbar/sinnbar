<template>
  <footer class="footer mt-6 has-background-light">
    <section>
      <div class="container column is-10">
        <div class="container is-fullhd is-fluid">
          <div class="columns is-mobile">
            <div class="column">
              <p>&#160;</p>
              <a href="mailto:zusammen@sinnbar.de"
                ><p class="has-text-left has-text-danger">kontakt</p></a
              >
              <a href="https://www.instagram.com/sinnbar_/" target="_blank"
                ><p class="has-text-left has-text-danger">instagram</p></a
              >
              <a href="https://www.facebook.com/sinnbar_/"
                ><p class="has-text-left has-text-danger">facebook</p></a
              >
            </div>
            <div class="column">
              <nuxt-link to="/agb"><p class="has-text-right has-text-danger">agb</p></nuxt-link>
              <nuxt-link to="/datenschutz"
                ><p class="has-text-right has-text-danger">datenschutz</p></nuxt-link
              >
              <nuxt-link to="/impressum"
                ><p class="has-text-right has-text-danger">impressum</p></nuxt-link
              >
              <nuxt-link to="/widerufsbelehrung"
                ><p class="has-text-right has-text-danger">widerufsbelehrung</p></nuxt-link
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
