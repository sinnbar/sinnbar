<template>
  <div>
    <div ref="paypal"></div>
  </div>
</template>

<script>
export default {
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
    setLoaded() {
      window.paypal
        .Buttons({
          createOrder(data, actions) {
            // This function sets up the details of the transaction, including the amount and line item details.
            return actions.order.create({
              purchase_units: [
                {
                  amount: {
                    value: '0.01',
                  },
                },
              ],
            })
          },
          onApprove(data, actions) {
            // This function captures the funds from the transaction.
            return actions.order.capture().then(function (details) {
              // This function shows a transaction success message to your buyer.
              alert('Transaction completed by ' + details.payer.name.given_name)
            })
          },
        })
        .render(this.$refs.paypal)
    },
  },
}
</script>
<style scoped></style>
