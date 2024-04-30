<script setup>
// import {fetchApi} from "@/worker.js";
import {ref} from "vue";
import emitter from "@/eventBus.js";

const url = ref('');
const method = ref('GET');
const param = ref('');
const header = ref('');
const thread = ref(20);
const path = ref('/');
const port = ref('80');
let dataout = ref('');
const regex = /\.[0-9]{1,3}\/\d{1,2}$/;
const workerQueue = [];
const eventQueue = []
let pause=0;

function startWorker(event) {
  if(pause ===1)
  {
    console.log(pause);
    return
  }
  const worker = new Worker(new URL('../worker.js', import.meta.url));
  if (workerQueue.length < thread.value) {
    worker.postMessage(event);
    workerQueue.push(worker)
  }
  worker.onmessage = (e) => {
    emitter.emit('dataout', e.data);
    workerQueue.shift();
    worker.terminate();
    processNextWorker();
  };
}

function processNextWorker() {
  if(pause ===1)
  {
    console.log(pause);
    return
  }
  if (workerQueue.length < thread.value && eventQueue.length > 0) {
    const nextEvent = eventQueue.shift(); // 从队列中取出下一个任务
    if (nextEvent) {
      startWorker(nextEvent); // 启动新的 Web Worker
    }
  }
}

function get_moreflag(url, method, param, header) {
  const regex_val1 = /\.[0-9]{1,3}\/\d{1,2}$/
  if (url.value.includes('/24')) {
    const url_val = url.value.replace(regex_val1, '');
    for (let i = 1; i < 256; i++) {

      const event = {
        url: 'http://' + url_val + '.' + i + ':'+port.value+path.value,
        method: method.value,
        param: param.value,
        header: header.value
      };
      eventQueue.push(event);
      processNextWorker();
    }
  }
  const regex_val2 = /\.[0-9]{1,3}\.[0-9]{1,3}\/\d{1,2}$/
  if (url.value.includes('/16')) {
    const url_val = url.value.replace(regex_val2, '');
    for (let i = 1; i < 256; i++) {
      for (let j = 1; j < 256; j++) {
        const event = {
          url: 'http://' + url_val + '.' + i + '.' + j + ':'+port.value+path.value,
          method: method.value,
          param: param.value,
          header: header.value
        };
        eventQueue.push(event);
        processNextWorker();
      }
    }
  }
}

const confirm_ssh = async (mode) => {
  if(mode === '0') {
    pause=0;
  if (regex.test(url.value)) {

    get_moreflag(url, method, param, header)

  } else {
    const event = {
      url: 'http://' + url.value+':'+port.value + path.value,
      method: method.value,
      param: param.value,
      header: header.value
    }
    eventQueue.push(event);
    processNextWorker();
  }
  }else {
    pause = 1;
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
            <label>IP地址 : </label>
            <input v-model="url" style="width: 220px" placeholder="192.168.52.143或192.168.52.0/24">
          </div>
          <div>
            <label>端口 : </label>
            <input v-model="port" style="width: 50px" placeholder="80">
          </div>
          <div>
            <label>Path : </label>
            <input v-model="path" placeholder="/">
          </div>
          <div>
            <label>方法 : </label>
            <input v-model="method" style="width: 100px" placeholder="GET">
          </div>
          <div>
            <label>参数 : </label>
            <input v-model="param" placeholder="5">
          </div>
          <div>
            <label>线程 : </label>
            <input v-model="thread" style="width: 50px" placeholder="20">
          </div>
          <div>
            <label>HTTP Header : </label>
            <input v-model="header" placeholder="5">
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