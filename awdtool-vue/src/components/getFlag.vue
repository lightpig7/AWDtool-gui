<script setup>

import {chage_passwd} from "@/tool.js";
import {ref} from "vue";
import emitter from "@/eventBus.js";

const username = ref('');
const password = ref('');
const host = ref('');
const port = ref(22);
const new_password = ref('');
const thread = ref(5);
let dataout = ref('');
const regex = /\.[0-9]{1,3}\/\d{1,2}$/;
const workerQueue = [];
const eventQueue = [];

function startWorker(event) {
  const worker = new Worker(new URL('../worker.js', import.meta.url));

  // 监听 Web Worker 返回的消息
  worker.onmessage = (e) => {

    emitter.emit('dataout',e.data);
    workerQueue.shift(); // 完成任务后移除队列中的该任务
    worker.terminate(); // 关闭线程
    processNextWorker(); // 处理下一个任务
  };
  worker.postMessage(event);
  workerQueue.push(worker);
}

function processNextWorker() {
  if (eventQueue.length > 0 && workerQueue.length < thread.value) {
    const nextEvent = eventQueue.shift(); // 从队列中取出下一个任务
    if (nextEvent) {
      startWorker(nextEvent); // 启动新的 Web Worker
    }
  }
}
function changemore(){
  const regex_val= /\.[0-9]{1,3}\.[0-9]{1,3}\/\d{1,2}$/
  if(host.value.includes('/24')) {
    let host_val = host.value.replace(regex, '');
    for (let i = 1; i <= 255; i++) {
      const event = {
        host: host_val + '.' + i,
        port: port.value,
        username: username.value,
        password: password.value,
        new_password: new_password.value
      };
      eventQueue.push(event);
      processNextWorker();
    }
  }
  if(host.value.includes('/16')) {
    let host_val = host.value.replace(regex_val, '');
    for (let i = 1; i <= 255; i++) {
      for (let j = 1; j <= 255; j++) {
        const event = {
          host: host_val + '.' + i+'.'+j,
          port: port.value,
          username: username.value,
          password: password.value,
          new_password: new_password.value
        };
        eventQueue.push(event);
        processNextWorker();
      }
    }
  }
}
const confirm_ssh = async () => {
  if (regex.test(host.value)) {
    changemore();
  } else {
    dataout.value = await chage_passwd(host.value, port.value, username.value, password.value, new_password.value);
    console.log(dataout.value)
    emitter.emit('dataout',dataout.value);
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
            <input v-model="host" style="width: 220px" placeholder="192.168.52.143或192.168.52.0/24">
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
            <input v-model="thread" style="width: 50px" placeholder="5">
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