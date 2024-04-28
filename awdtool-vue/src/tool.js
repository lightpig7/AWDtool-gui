
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