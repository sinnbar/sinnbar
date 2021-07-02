<template>
  <div class="container is-fullhd is-fluid">
    <section class="section has-background-light mt-6">
      <div class="columns is-centered is-vcentered">
        <div class="column">
          <b-image src="/img/intro.png" ratio="9by9"></b-image>
        </div>
        <div class="column">
          <p class="is-size-2 is-family-secondary m-2">{{ offer.title }}</p>
          <p class="is-size-6 m-2">
            {{ offer.description }}
          </p>
          <p v-if="offer.price == null" class="m-2 is-size-4">kostenfrei</p>
          <p v-else class="m-2 is-size-4">{{ offer.price }} €</p>
          <div class="columns">
            <b-select
              v-model="selectedTourId"
              class="m-2"
              placeholder="terminauswahl"
              @change="getSelectedItem"
            >
              <option v-for="tour of tours" :key="tour.id" :value="tour">
                {{ tour.date }}
              </option>
            </b-select>

            <b-button
              type="m-2 is-primary is-light"
              tag="router-link"
              :to="{
                name: 'buchen',
                params: { offer: offer, tour: selectedTourId },
              }"
              >teilnehmen</b-button
            >
          </div>
        </div>
      </div>
      <div class="column">
        <p class="is-size-4 is-family-secondary m-2">über die anbietenden</p>
        <p class="m-2">
          Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean
          commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus
          et magnis dis parturient montes, nascetur ridiculus mus. Donec quam
          felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla
          consequat massa qu aliquet nec, vulputate mpteger tincidunt.
        </p>
      </div>
    </section>

    <OfferGrid />
  </div>
</template>

<script>
export default {
  data() {
    return {
      offer: {},
      tours: [],
      selectedTourId: {},
    }
  },
  async fetch() {
    this.offer = await this.$axios.$get(
      `/api/v1/offers/${this.$route.params.id}/`
    )
    this.tours = await this.$axios.$get(
      `/api/v1/tours/?offer=${this.$route.params.id}`
    )
  },
  methods: {
    getSelectedItem(myarg) {
      // Just a regular js function that takes 1 arg
      console.log('asdfasdf')
    },
  },
}
</script>
‘

<style></style>
