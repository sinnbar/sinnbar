<template>
  <b-navbar class="center container column is-10">
    <template #brand>
      <b-navbar-item tag="router-link" :to="{ path: '/' }">
        <p class="is-size-4">sinnbar</p>
      </b-navbar-item>
    </template>
    <template #start>
      <b-navbar-item href="/erlebnisse"> erlebnisse </b-navbar-item>
      <b-navbar-item href="#"> vision </b-navbar-item>
      <b-navbar-item href="#"> menschen </b-navbar-item>
      <b-navbar-item href="#"> kollektiv </b-navbar-item>
    </template>

    <!--    <template #end>-->
    <!--      <b-navbar-item tag="div">-->
    <!--        <div class="buttons">-->
    <!--          <a class="button is-primary">-->
    <!--            <strong>Mach mit</strong>-->
    <!--          </a>-->
    <!--          <a class="button is-light"> Log in </a>-->
    <!--        </div>-->
    <!--      </b-navbar-item>-->
    <!--    </template>-->
  </b-navbar>
</template>
<script>
export default {
  name: 'Navbar',
}
</script>

<style scoped></style>
