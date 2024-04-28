<script setup>

import ExcuteTheOrder from "@/components/ExcuteTheOrder.vue";
import Dataout_window from "@/components/dataout_window.vue";
import GetFlag from "@/components/getFlag.vue";
</script>

<template>
  <header>


      <excute-the-order msg="You did it!" />
      <get-flag />
  </header>

  <main>

  <dataout_window/>
  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
}


</style>
