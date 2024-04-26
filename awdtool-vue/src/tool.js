export const chage_passwd = async function (host, port, username, password,new_password) {
    return await pywebview.api.chage_passwd(host, port, username, password,new_password)
}