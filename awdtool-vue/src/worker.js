function fetchApi(url) {
    return new Promise((resolve, reject) => {
        const xhr = new XMLHttpRequest();
        xhr.open('GET', url);
        xhr.onload = () => {
            if (xhr.status >= 200 && xhr.status < 300) {
                resolve(xhr.responseText);
            } else {
                reject(new Error(`Request failed with status ${xhr.status}`));
            }
        };
        xhr.onerror = () => {
            reject(new Error('Request failed'));
        };
        xhr.send();
    });
}

self.onmessage = async function(event) {
    const {url, method, param, header} =event.data
    console.log(url, method, param, header)
    try {
        const responseText = await fetchApi(`/api?url=${url}&method=${method}&param=${param}&header=${header}`);
        self.postMessage(responseText); // 将信息发送到主线程上
    } catch (error) {
        console.error('Error fetching data:', error);
    }
};
