(function(){"use strict";function o(t){return new Promise((s,n)=>{const e=new XMLHttpRequest;e.open("GET",t),e.onload=()=>{e.status>=200&&e.status<300?s(e.responseText):n(new Error(`Request failed with status ${e.status}`))},e.onerror=()=>{n(new Error("Request failed"))},e.send()})}self.onmessage=async function(t){try{const s=await o("/api");console.log(s),self.postMessage(s)}catch(s){console.error("Error fetching data:",s)}}})();