<template>
  <div class="pt-6  flex flex-col items-center dark:bg-gray-100 w-4/5 mx-auto pb-3 rounded-b">
    <div class="flex flex-col items-center">
      <h1 class="m-1 p-1 text-6xl bg-green-900 text-gray-100 uppercase font-bold transform -skew-x-12">
        Truthy</h1>
      <h2 class="text-green-800 uppercase font-bold w-4/5">Only certified accounts for only certified news</h2>
    </div>

    <div class="grid grid-cols-1 gap-6 mt-6">
      <div class="mx-auto w-4/5 center">
        <h3 class="text-green-800 font-bold text-2xl uppercase">Sign in</h3>

      </div>
      <label class="block">
        <span class="text-green-800">Email</span>
        <input type="text"
               v-model="email"
               class="mt-1 block w-full rounded border-green-600 shadow-sm focus:border-green-900 focus:ring focus:outline-none focus:ring-green-600 focus:ring-opacity-50 "/>
      </label>

      <label class="block">
        <span class="text-green-800">Password</span>

        <input type="password"
               v-model="password"
               class="mt-1 block w-full rounded border-green-600 shadow-sm focus:border-green-900 focus:ring focus:outline-none focus:ring-green-600 focus:ring-opacity-50 "/>
      </label>
      <label class="inline-flex items-center">
        <input type="checkbox" checked="" v-model="rememberMe"
               class="block rounded text-green-900 shadow-sm focus:border-green-900 focus:ring focus:outline-none focus:ring-green-600 focus:ring-opacity-50 ">
        <span class="ml-2 text-green-900">Remember me</span>
      </label>
      <button type="submit"
              @click="onClick"
              class="rounded bg-green-900 py-2 text-green-100 focus:border-green-900 focus:ring focus:outline-none focus:ring-green-600 focus:ring-opacity-50">
        Sign in
      </button>
    </div>
  </div>


</template>

<script>
import {ref} from "vue";
import {useRouter} from "vue-router";
import {useStore} from "vuex";

export default {
  setup() {
    const email = ref("")
    const password = ref("")
    const rememberMe = ref(true)
    const router = useRouter()
    const store = useStore()
    const onClick = async () => {
      await store.dispatch('login', {
        email: email.value,
        password: password.value,
        rememberMe: rememberMe.value
      })

      return router.push({path: "home"})
    }
    return {email, password, onClick, rememberMe}
  }
}
</script>
