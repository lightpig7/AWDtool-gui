<script setup>
import {ref} from "vue";
import emitter from "@/eventBus.js";

const dataout=ref('');
emitter.on('dataout',data=>{
  dataout.value+=data+'\n';
})
</script>

<template>

  <div>日志信息 : </div>
  <br>
  <div id="log">
  <pre>{{ dataout }}</pre>
  </div>
</template>

<style scoped>
#log{
  height: 120px;
  overflow: auto;
}
</style>