<script setup>

import {chage_passwd} from "@/tool.js";
import {ref} from "vue";

const username =ref('');
const password =ref('');
const host =ref('');
const port =ref('');
const new_password =ref('');
let dataout= ref('');

const confirm = async () => {
  dataout = await chage_passwd(host.value, port.value, username.value, password.value, new_password.value)
  console.log(dataout)
}
</script>

<template>
  <div>
    <h3>修改ssh密码</h3>
    <div class="display">
      <div>
        <div class="item-mini">
          <div>
            <label>用户名</label>
            <input v-model="username" placeholder="默认为ubuntu">
          </div>
          <div>
            <label>密码</label>
            <input v-model="password" placeholder="默认123456">
          </div>
          <div>
            <label>IP地址</label>
            <input v-model="host" placeholder="默认192.168.52.143">
          </div>
          <div>
            <label>端口</label>
            <input v-model="port" placeholder="默认22">
          </div>
          <div>
            <label>新密码</label>
            <input v-model="new_password" placeholder="默认peiqi7@987">
          </div>
        </div>
        <hr>
        <div style="text-align: center">
          <button @click="confirm('1')">确认</button>
        </div>
      </div>
      <label>日志信息 : </label>
      <span>{{dataout}}</span>
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