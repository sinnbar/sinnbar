<template>
  <div>
    <div ref="paypal"></div>
  </div>
</template>

<script>
export default {
  props: ['bookingdata'],
  data() {
    return {
      booking: {},
    }
  },
  mounted() {
    const script = document.createElement('script')
    script.src =
      'https://www.paypal.com/sdk/js?client-id=Afdfrvax7g8d1Hi0SSkQ2X04UgETMG0mRGy3i6MQIBH1T1iXAckZDbBH09n1YauECOrMFmwRCZfb2XQk'
    script.addEventListener('load', this.setLoaded)
    document.body.appendChild(script)
  },

  methods: {
    openPaymentAmountModal() {
      this.isPaymentAmountModalVisible = true
    },
    closePaymentAmountModal() {
      this.isPaymentAmountModalVisible = false
    },
    async redirect(order) {
      const params = {
        orderData: order,
        bookingData: {
          participant: {
            first_name: this.$props.bookingdata.firstName,
            last_name: this.$props.bookingdata.lastName,
            email: this.$props.bookingdata.email,
            newsletter: this.$props.bookingdata.newsletter,
          },
          number_participants: this.$props.bookingdata.amount,
          tour: this.$props.bookingdata.tour.id,
          total_price: this.$props.bookingdata.total_price,
          order_id: order.orderID
        },
      }
      this.reservation = await this.$axios.$post(
        '/api/v1/reservations/',
        params
      )

      await this.$router.push('/buchungsabschluss')
    },
    setLoaded() {
      window.paypal
        .Buttons({
          createOrder: this.createOrder,
          onApprove: this.onApprove,
        })
        .render(this.$refs.paypal)
    },
    createOrder(data, actions) {
      // ...
      return actions.order.create({
        purchase_units: [
          {
            amount: {
              value: this.$props.bookingdata.total_price,
              currency: 'EUR',
            },
          },
        ],
      })
      // console.error('PayPal', 'createOrder', arguments)
    },
    onApprove(data, actions) {
      return actions.order.capture().then(() => {
        this.redirect(data)
      })
    },
  },
}
</script>
<style scoped></style>
