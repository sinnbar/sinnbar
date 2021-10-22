<template>
  <div class="container is-fullhd is-fluid">
    <section class="section has-background-light mt-6">
      <div class="columns is-centered is-vcentered">
        <div class="column">
          <b-image src="/img/intro.png" ratio="9by9"></b-image>
        </div>
        <div class="column">
          <p class="is-size-3 is-family-secondary">{{ offer.title }}</p>
          <p class="is-size-6 mt-1">
            {{ offer.description }}
          </p>
          <p v-if="offer.price == null" class="is-size-4 mt-2">kostenfrei</p>
          <p v-else class="is-size-4 mt-2">{{ offer.price }} €</p>
          <div class="columns mt-2">
            <div class="column">
              <b-select placeholder="Datum auswählen" v-model="selectedTourId" @input="getSelectedItem">
                <option v-for="tour of tours" :key="tour.id" :value="tour">
                  {{ tour.date }}
                </option>
              </b-select>
              <div class="columns">
                <div class="column is-narrow ml-1 ">
                  <p v-if="free_tour_places > 0">
                    noch {{ free_tour_places }} freie Plätze
                  </p>
                  <p v-else-if="free_tour_places === 1">
                    noch {{ free_tour_places }} freier Platz
                  </p>
                </div>
              </div>
            </div>
            <div class="column">
              <b-button
                type="is-primary"
                tag="router-link"
                :to="{
                  name: 'buchen',
                  params: { offer: offer, tour: selectedTourId },
                }"
                >jetzt buchen</b-button
              >
            </div>
          </div>
        </div>
      </div>
        <p class="is-size-4 is-family-secondary m-2">über die anbietenden</p>
        <p class="m-2">
          Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean
          commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus
          et magnis dis parturient montes, nascetur ridiculus mus. Donec quam
          felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla
          consequat massa qu aliquet nec, vulputate mpteger tincidunt.
        </p>
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
      selectedTourId: null,
      free_tour_places: 0,
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
    getSelectedItem() {
      this.free_tour_places =
        this.selectedTourId.max_participants - this.selectedTourId.participants
    },
  },
}
</script>
‘

<style></style>
