import axios from "axios";
import emitter from "@/eventBus.js";

export const chage_passwd = async function (host, port, username, password,new_password) {
    console.log(host, port, username, password,new_password)
    // return '123';
    return await pywebview.api.chage_passwd(host, port, username, password, new_password);
    //
}
export const change_morepasswd = async function (host, port, username, password,new_password,thread,mode) {
    console.log(host, port, username, password,new_password,thread,mode)
    return await pywebview.api.change_morepasswd(host, port, username, password, new_password,thread,mode);
    //
}
export const get_flag = async function (){
    axios.get('/api')
        .then(response => {
            // 处理返回的数据
            console.log(response.data);
            return response.data;
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
}