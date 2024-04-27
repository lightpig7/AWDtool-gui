<script setup>

import ExcuteTheOrder from "@/components/ExcuteTheOrder.vue";
import Dataout_window from "@/components/dataout_window.vue";
</script>

<template>
  <header>

    <div class="wrapper">
      <excute-the-order msg="You did it!" />
    </div>
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
