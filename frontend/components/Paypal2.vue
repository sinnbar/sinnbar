<template>
  <div id="paypal-button-container" />
</template>

<script>
export default {
  name: 'PayPalButton',
  data() {
    return {
      clientId:
        'Afdfrvax7g8d1Hi0SSkQ2X04UgETMG0mRGy3i6MQIBH1T1iXAckZDbBH09n1YauECOrMFmwRCZfb2XQk',
      sdkLoaded: false,
    }
  },
  async mounted() {
    await this.loadSdkScript()
    this.renderButton()
  },
  methods: {
    loadSdkScript() {
      return new Promise((resolve) => {
        const script = document.createElement('script')
        script.async = true
        script.src = 'https://www.paypal.com/sdk/js?client-id=' + this.clientId
        script.onload = () => {
          this.sdkLoaded = true
          resolve()
        }
        document.body.appendChild(script)
      })
    },
    renderButton() {
      window.paypal
        .Buttons({
          style: {
            shape: 'rect',
            color: 'gold',
            layout: 'horizontal',
            label: 'checkout',
            tagline: false,
          },
          createOrder: this.createOrder,
          onShippingChange: this.onShippingChange,
          onApprove: this.onApprove,
          onError: this.onError,
        })
        .render('#paypal-button-container')
    },
    createOrder() {
      // ...

      console.error('PayPal', 'createOrder', arguments)
    },
    onShippingChange() {
      // ...

      console.error('PayPal', 'onShippingChange', arguments)
    },
    onApprove() {
      // ...
      actions.order

      console.error('PayPal', 'onApprove', arguments)
    },
    onError() {
      // ...

      console.error('PayPal', 'onError', arguments)
    },
  },
}
</script>
