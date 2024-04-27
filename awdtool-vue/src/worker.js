import {chage_passwd} from "@/tool.js";


self.onmessage = async function  (event) { //监听主线程发过来的消息
    // const { chage_passwd } = await import('@/tool.js');
    // const { chage_passwd } = await import('./tool.js')
    const { host, port, username, password, new_password } = event.data;
    let strr = await chage_passwd(host, port, username, password,new_password)
    console.log(host, port, username, password, new_password);
    self.postMessage(strr); // 将信息发送到主线程上
}
