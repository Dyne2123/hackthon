const url = "http://127.0.0.1:5000/test"
const url2 = "http://127.0.0.1:5000/sendContent"


export function sendEditorContent(content,pastedText){
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body: JSON.stringify({content,pastedText})
    })
    .then(response => response.json())
    .then(data => {
        console.log("Server response: ",data);
    }).catch(error => {
        console.error(error);

    })
}

export function getEditorContent() {
  return fetch(url2, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ response: "send" })
  })
    .then(response => response.json())
    .then(data => {
      console.log("Server response: ", data);
      return data;  // 
    })
    .catch(error => {
      console.error("API error:", error);
      return { content: "<p>Error loading</p>", pasted_text: [] }; k
    });
}


