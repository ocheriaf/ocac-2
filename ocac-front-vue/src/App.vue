<template>
  <div class="dark">

  <div class="h-screen bg-gray-100 dark:bg-gray-900">

  <Navbar/>

  <router-view />
  </div>
  </div>
</template>
<script>import Navbar from "@/components/Navbar";

export default {
  components:{
    Navbar:Navbar
  },

}</script>
<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}


</style>
