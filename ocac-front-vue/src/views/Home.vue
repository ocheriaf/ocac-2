<template>
  <div class="home">
    <ProfileCreation></ProfileCreation>
  </div>
</template>

<script>
// @ is an alias to /src
import ProfileCreation from "@/components/ProfileCreation";

export default {
  name: "Home",
  components: {ProfileCreation},
  setup() {
    return {}
  }
};
</script>
