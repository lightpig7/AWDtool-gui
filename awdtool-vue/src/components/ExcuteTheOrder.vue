<script setup>

import {chage_passwd} from "@/tool.js";
import {ref} from "vue";

const username = ref('');
const password = ref('');
const host = ref('');
const port = ref('');
const new_password = ref('');
const thread = ref('');
let dataout = ref('');

const regex = /\.[0-9]{1,3}\/\d{1,2}$/;
const confirm = async () => {
  if (regex.test(host.value)) {
    let host_val = host.value.replace(regex,'');
    for(let i =1;i <= 255;i++ ){
      console.log(host_val+'.'+i);
    }
  } else {
    dataout.value = await chage_passwd(host.value, port.value, username.value, password.value, new_password.value)
    console.log(dataout.value)
  }
}


</script>

<template>
  <div>
    <h3>修改ssh密码</h3>
    <div class="display">
      <div>
        <div class="item-mini">
          <div>
            <label>IP地址 : </label>
            <input v-model="host" placeholder="192.168.52.143">
          </div>
          <div>
            <label>端口 : </label>
            <input v-model="port" style="width: 50px" placeholder="默认22">
          </div>
          <div>
            <label>用户名 : </label>
            <input v-model="username" placeholder="默认为ubuntu">
          </div>
          <div>
            <label>密码 : </label>
            <input v-model="password" placeholder="默认123456">
          </div>
          <div>
            <label>新密码 : </label>
            <input v-model="new_password" placeholder="默认peiqi7@987">
          </div>
          <div>
            <label>线程 : </label>
            <input v-model="thread" placeholder="默认为5">
          </div>
        </div>
        <hr>
        <div style="text-align: center">
          <button @click="confirm('1')">确认</button>
        </div>
      </div>
      <label>日志信息 : </label>
      <br>
      <span>{{ dataout }}</span>
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