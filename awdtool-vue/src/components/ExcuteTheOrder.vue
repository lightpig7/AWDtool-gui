<script setup>

import {chage_passwd, change_morepasswd} from "@/tool.js";
import {ref, watch} from "vue";
import emitter from "@/eventBus.js";


const username = ref('');
const password = ref('');
const host = ref('');
const port = ref(22);
const new_password = ref('');
const thread = ref(20);
let dataout = ref('');
const regex = /\.[0-9]{1,3}\/\d{1,2}$/;


const confirm_ssh = async (mode) => {
  if (regex.test(host.value)) {
    if(mode === '0') {
    emitter.emit('dataout', '扫描中...');
    dataout.value = await change_morepasswd(host.value, port.value, username.value, password.value, new_password.value,thread.value,mode);
    emitter.emit('dataout', dataout.value);
    }else {
      emitter.emit('dataout', '关闭中...');
      dataout.value = await change_morepasswd(host.value, port.value, username.value, password.value, new_password.value,thread.value,mode);
      emitter.emit('dataout', dataout.value);
    }
  } else {
    dataout.value = await chage_passwd(host.value, port.value, username.value, password.value, new_password.value,);
    emitter.emit('dataout', dataout.value);
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
            <input v-model="host" style="width: 210px" placeholder="192.168.52.143或192.168.52.0/24">
          </div>
          <div>
            <label>端口 : </label>
            <input v-model="port" style="width: 50px" placeholder="22">
          </div>
          <div>
            <label>用户名 : </label>
            <input v-model="username" placeholder="ubuntu">
          </div>
          <div>
            <label>密码 : </label>
            <input v-model="password" placeholder="123456">
          </div>
          <div>
            <label>新密码 : </label>
            <input v-model="new_password" placeholder="peiqi7@987">
          </div>
          <div>
            <label>线程 : </label>
            <input v-model="thread" style="width: 50px" placeholder="20">
          </div>
        </div>
        <hr>
        <div class="item-mini">
        <div style="text-align: center">
          <button @click="confirm_ssh('0')">确认</button>
        </div>
          <div style="text-align: center;margin-left: -100px">
            <button @click="confirm_ssh('1')">取消</button>
          </div>
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