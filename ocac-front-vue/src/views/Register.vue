<template>
  <div class="pt-6  flex flex-col items-center dark:bg-gray-100 w-4/5 mx-auto pb-3 rounded-b">
    <div class="flex flex-col items-center">
      <h1 class="m-1 p-1 text-6xl bg-green-900 text-gray-100 uppercase font-bold transform -skew-x-12">
        Truthy</h1>
      <h2 class="text-green-800 uppercase font-bold w-4/5">Only certified accounts for only certified news</h2>
    </div>

    <div class="grid grid-cols-1 gap-6 mt-6">
      <div class="mx-auto w-4/5 center">
        <h3 class="text-green-800 font-bold text-2xl ">Registration form</h3>
        <span v-if="success" class="text-green-600 uppercase">Registration complete. You can login <router-link
            to="/login">here</router-link></span>
      </div>
      <label class="block">
        <span class="text-green-800">Email</span>
        <input type="text"
               required
               v-model="email"
               class="mt-1 block w-full rounded border-green-600 shadow-sm focus:border-green-900 focus:ring focus:outline-none focus:ring-green-600 focus:ring-opacity-50 "/>
      </label>

      <label class="block">
        <span class="text-green-800">Password</span>

        <input type="password"
               v-model="password"
               required
               class="mt-1 block w-full rounded border-green-600 shadow-sm focus:border-green-900 focus:ring focus:outline-none focus:ring-green-600 focus:ring-opacity-50 "/>
      </label>
      <button type="submit"
              @click="onClick"
              class="rounded bg-green-900 py-2 text-green-100 focus:border-green-900 focus:ring focus:outline-none focus:ring-green-600 focus:ring-opacity-50">
        Submit
      </button>
    </div>
  </div>


</template>

<script>
import {ref} from "vue";
import {register} from "@/api/api";

export default {
  setup() {
    const email = ref("")
    const password = ref("")
    const success = ref(false)

    const onClick = async () => {
      const response = await register({password: password.value, email: email.value})
      console.log(response)
      success.value = true
    }
    return {email, password, onClick, success}
  }
}
</script>