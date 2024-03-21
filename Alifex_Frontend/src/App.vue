<template>
  <v-app class="app-container">
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'App',

  data: () => ({
    //
  }),
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Raleway&display=swap');
* {
  font-family: 'Raleway', sans-serif;
}
</style>
