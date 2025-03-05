btn = document.getElementById('sendBtn');
btn.addEventListener("click",handleMessage);

const fast_forward = document.getElementById("fast_forward");
fast_forward.addEventListener("click", handleFastForward);

function handleMessage() {

    const inputField = document.getElementById("user-input");
    const message = inputField.value.trim();
    if (message === "") {
        return;
    }
    else {
        console.log(`Message from user: ${message}`);
        sendMessage(message, false);
    }
    
    const chatBox = document.getElementById("chat-box");
    const userMessage = document.createElement("div");
    userMessage.className = "message user";
    userMessage.textContent = message;
    chatBox.appendChild(userMessage);
    
    inputField.value = "";
    chatBox.scrollTop = chatBox.scrollHeight;

    setTimeout(() => {
        const botMessage = document.createElement("div");
        botMessage.className = "message bot";
        botMessage.textContent = "Let me think...";
        chatBox.appendChild(botMessage);
        chatBox.scrollTop = chatBox.scrollHeight;
    }, 500);

    
}

async function sendMessage(message) {
    console.log("Sending message to server...");

    let funny_mode = document.getElementById("funny_toggle").checked;
    console.log(funny_mode);

    if (funny_mode === true) {
        const joke_prompt = "Make sure you reply by beginning with a joke. Say 'Here is a joke'.";
        message = joke_prompt + message;
    }

    body = JSON.stringify(`{"message": ${message}}`);
    console.log(message);

    const response = await fetch("/chat/", {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: body,
        });
    
    let reply = "";
    response.json().then(data => {
        console.log(JSON.stringify(data));
        reply = data["response"].replaceAll("\n", "</br>");
        

    if (response !== "") {
        const chatBox = document.getElementById("chat-box");
        const botMessage = document.createElement("div");
        botMessage.className = "message bot";
        botMessage.innerHTML = reply; //newlines
        chatBox.appendChild(botMessage);
        chatBox.scrollTop = chatBox.scrollHeight;
    } 

    });
}


async function handleFastForward(message) {
    console.log("Sending message to server...");

    //sendMessage(message,true);
    /////////

    body = JSON.stringify(`{"message": ${message}}`);
    console.log(message);

    const response = await fetch("/predict/", {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: body,
        });
    
    let reply = "";
    response.json().then(data => {
        console.log(JSON.stringify(data));
        reply = data["response"].replaceAll("\n", "</br>");
        

    if (response !== "") {
        //this is fast forward mode message
        const chatBox = document.getElementById("chat-box");
        const predictMessage = document.createElement("div");
        predictMessage.className = "message predict";
        const predict_start = " "
        predictMessage.innerHTML = predict_start + reply
        chatBox.appendChild(predictMessage);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    });
   
}

