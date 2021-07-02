<template>
  <div class="container is-fullhd is-fluid">
    <section class="section mt-6">
      <b-steps
        v-model="activeStep"
        :animated="isAnimated"
        :rounded="isRounded"
        :has-navigation="hasNavigation"
        :icon-prev="prevIcon"
        :icon-next="nextIcon"
        :label-position="labelPosition"
        :mobile-mode="mobileMode"
      >
        <b-step-item
          step="1"
          label="Informationen"
          :clickable="isStepsClickable"
        >
          <div class="columns is-mobile is-centered">
            <div class="column is-half-desktop">
              <p class="m-5 has-text-centered">
                Bitte geben Sie Ihre information an, ya?
              </p>
              <b-field label="Vorname">
                <b-input v-model="firstName" required></b-input>
              </b-field>
              <b-field label="Nachname">
                <b-input v-model="lastName" required></b-input>
              </b-field>
              <b-field label="Freie Plätze">{{ free_tour_places }}</b-field>

              <b-field label="Personen">
                <b-input
                  v-model="amount"
                  placeholder="Für wie viel Personen möchten Sie buchen?"
                  type="number"
                  min="1"
                  :max="free_tour_places"
                  value="1"
                  required
                >
                  <>
                </b-input>
              </b-field>
              <b-field label="Email">
                <b-input
                  v-model="email"
                  placeholder="Email"
                  type="email"
                  required
                ></b-input>
              </b-field>
              <b-field>
                <b-checkbox v-model="newsletter"
                  >Ich möchte Newsletter</b-checkbox
                >
              </b-field>
              <b-field>
                <b-checkbox v-model="privacy" required
                  >Mir ist Datenschutz egal</b-checkbox
                >
              </b-field>
            </div>
          </div>
        </b-step-item>

        <b-step-item
          v-if="privacy && firstName && lastName && amount && email"
          :step="2"
          label="Zusammenfassung"
          :clickable="isStepsClickable"
          disabled
        >
          <div class="container ml-5 mr-5">
            <p class="m-5 has-text-centered">
              Überprüfe bitte deine Angaben :)
            </p>
            <div class="columns is-mobile is-centered">
              <div class="column is-half-fullhd">
                <div class="box">
                  <div class="columns is-half is-multiline">
                    <div class="column is-half">
                      <p class="has-text-weight-semibold">Tour:</p>
                    </div>
                    <div class="column is-half">
                      <p>{{ offer.title }}</p>
                    </div>
                    <div class="column is-half">
                      <p class="has-text-weight-semibold">Datum:</p>
                    </div>
                    <div class="column is-half">
                      <p>{{ tour.date }}</p>
                    </div>
                    <div class="column is-half">
                      <p class="has-text-weight-semibold">Name:</p>
                    </div>
                    <div class="column is-half">
                      <p>{{ lastName }} {{ firstName }}</p>
                    </div>
                    <div class="column is-half">
                      <p class="has-text-weight-semibold">Email:</p>
                    </div>
                    <div class="column is-half">
                      <p>{{ email }}</p>
                    </div>
                    <div class="column is-half">
                      <p class="has-text-weight-semibold">Personen:</p>
                    </div>
                    <div class="column is-half">
                      <p>{{ amount }}</p>
                    </div>
                    <div class="column is-half">
                      <p class="has-text-weight-semibold">Preis:</p>
                    </div>
                    <div class="column is-half">
                      <p>
                        {{ amount }} x {{ offer.price }} = 24 € (inkl. Mwst)
                      </p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </b-step-item>

        <b-step-item
          v-if="privacy"
          step="3"
          label="Bezahlung"
          :clickable="isStepsClickable"
          :type="{ 'is-success': isProfileSuccess }"
        >
          <div class="columns is-mobile is-centered">
            <div class="column is-half-desktop">
              <p class="m-5 has-text-centered">Hier wird Geld gelazt</p>

              <Paypal />
            </div>
          </div>
        </b-step-item>
      </b-steps>
    </section>
  </div>
</template>

<script>
export default {
  data() {
    return {
      activeStep: 0,

      showSocial: false,
      isAnimated: true,
      isRounded: false,
      isStepsClickable: true,

      hasNavigation: true,
      customNavigation: false,
      isProfileSuccess: true,

      prevIcon: 'chevron-left',
      nextIcon: 'chevron-right',
      labelPosition: 'bottom',
      mobileMode: 'minimalist',

      firstName: '',
      lastName: '',
      amount: 1,
      email: '',
      newsletter: false,
      privacy: false,

      tour: {},
      offer: {},

      free_tour_places: 0,
    }
  },
  mounted() {
    this.tour = this.$route.params.tour
    this.offer = this.$route.params.offer
    if (!this.tour || !this.offer) {
      this.$router.back()
    } else {
      this.free_tour_places =
        this.tour.max_participants - this.tour.participants
    }
  },
}
</script>
