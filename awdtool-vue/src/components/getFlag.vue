<script setup>

import {chage_passwd} from "@/tool.js";
import {ref} from "vue";
import emitter from "@/eventBus.js";
import axios from 'axios';

const url = ref('');
const method = ref('');
const param = ref('');
const header = ref('');
const thread = ref(5);
let dataout = ref('');
const regex = /\.[0-9]{1,3}\/\d{1,2}$/;

async function getFlag(url) {
  const response = await fetch(url,{
    method: "post",
    headers: {
      "Content-Type": "application/json"
    }
  }
  )
  console.log(response)

}
function changemore(){
  const regex_val= /\.[0-9]{1,3}\.[0-9]{1,3}\/\d{1,2}$/
  if(host.value.includes('/24')) {

    }

  if(host.value.includes('/16')) {

    }

}
const confirm_ssh = async () => {
  if (regex.test(url.value)) {
    changemore();
  } else {
    dataout.value = await getFlag('http://'+url.value+'/');
    console.log(url.value)
    console.log(dataout.value);
    emitter.emit('dataout',dataout.value);
  }
}


</script>

<template>
  <div>
    <h3>Get-flag</h3>
    <div class="display">
      <div>
        <div class="item-mini">
          <div>
            <label>Url : </label>
            <input v-model="url" style="width: 220px" placeholder="192.168.52.143或192.168.52.0/24">
          </div>
          <div>
            <label>方法 : </label>
            <input v-model="method" style="width: 50px" placeholder="22">
          </div>
          <div>
            <label>参数 : </label>
            <input v-model="param" style="width: 50px" placeholder="5">
          </div>
          <div>
            <label>线程 : </label>
            <input v-model="thread" style="width: 50px" placeholder="5">
          </div>
          <div>
            <label>HTTP Header : </label>
            <input v-model="header"  placeholder="5">
          </div>
        </div>
        <hr>
        <div style="text-align: center">
          <button @click="confirm_ssh('1')">确认</button>
        </div>
      </div>

    </div>
  </div>
</template>

<style scoped>
.display {

  justify-items: center;
}

.item-mini {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
}
</style>