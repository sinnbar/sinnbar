<template>
  <p v-if="$fetchState.pending">Fetching mountains...</p>
  <p v-else-if="$fetchState.error">An error occurred :(</p>
  <div v-else>
    <div class="columns is-multiline is-centered mt-6">
      <div v-for="offer of offers" class="column is-one-third">
        <NuxtLink :to="{ name: 'offer-id', params: { id: offer.id } }">
          <div class="card card-equal-height">
            <div class="card-image">
              <figure class="image is-4by3">
                <img class="is-cover" :src="offer.images | defaultImage" />
              </figure>
            </div>
            <div class="card-content">
              <div class="content">
                <p class="is-size-4-desktop is-bold-tablet is-size-5-touch">
                  {{ offer.title }}
                </p>
                {{ offer.description }}
              </div>
            </div>
          </div>
        </NuxtLink>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  filters: {
    defaultImage(value) {
      const defaultImage = value.find((image) => image.default === true)
      return defaultImage
        ? defaultImage.image.toString()
        : 'https://bulma.io/images/placeholders/1280x960.png'
    },
  },
  data() {
    return {
      offers: [],
    }
  },
  async fetch() {
    this.offers = await this.$axios.$get('/api/v1/offers/')
  },
}
</script>
