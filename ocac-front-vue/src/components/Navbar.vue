<template>
  <nav class="w-full bg-green-400 shadow-lg flex items-center justify-around">
    <div>
      <span
          class="m-1 block p-1 text-3xl bg-gray-100 text-green-900 uppercase font-bold transform -skew-x-12	shadow-lg">Truthy</span>
    </div>
    <div class="p-3 bg-gray-100 text-green-400 uppercase font-bold text-sm" v-if="!isAuthenticated">
      <router-link to="/login" class="text-green-900">Sign in</router-link>
      |
      <router-link to="/register">Register</router-link>
    </div>
    <div class="p-3 relative text-green-400 uppercase font-bold text-sm" v-if="isAuthenticated">
      <input placeholder="Search to implement" type="text"
             class="mt-1 block w-full text-green-900 rounded border-none shadow-sm focus:border-green-900 focus:ring focus:outline-none focus:ring-green-600 focus:ring-opacity-50 "/>
      <button type="submit" class="absolute right-0 top-0 mt-7 mr-6">
          <svg class="text-green-600 h-4 w-4 fill-current" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Capa_1" x="0px" y="0px" viewBox="0 0 56.966 56.966" style="enable-background:new 0 0 56.966 56.966;" xml:space="preserve" width="512px" height="512px">
            <path d="M55.146,51.887L41.588,37.786c3.486-4.144,5.396-9.358,5.396-14.786c0-12.682-10.318-23-23-23s-23,10.318-23,23  s10.318,23,23,23c4.761,0,9.298-1.436,13.177-4.162l13.661,14.208c0.571,0.593,1.339,0.92,2.162,0.92  c0.779,0,1.518-0.297,2.079-0.837C56.255,54.982,56.293,53.08,55.146,51.887z M23.984,6c9.374,0,17,7.626,17,17s-7.626,17-17,17  s-17-7.626-17-17S14.61,6,23.984,6z"></path>
          </svg>
        </button>
    </div>
  </nav>
</template>

<script>
import {useStore} from "vuex";

export default {
  name: "Navbar",
  setup() {
    const store = useStore()
    const isAuthenticated = store.getters.isAuthenticated
    return {isAuthenticated}
  }
}
</script>

<style lang="scss">

</style>