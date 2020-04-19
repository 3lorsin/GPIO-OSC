    //
    // var ws = new WebSocket("ws://192.168.2.2:5678/"),
    //     messages = document.createElement('ul');


    url = 'ws://192.168.2.2:5678/';
    const ws = new ReconnectingWebSocket(url);
    // Connection opened
    ws.addEventListener('open', function(event) {
      console.log("Socket Opened");
    });

ws.onopen = function(e) {
// ws.send('{ "type":"button_press", "data": [{ "button":"button_1", "state":"off"}] }');


};

function button_pressed(button_name) {
  ws.send('{ "type":"button_press", "data": [{ "button":"' + button_name + '", "state":"on"}] }');
}
function button_released(button_name) {
  ws.send('{ "type":"button_press", "data": [{ "button":"' + button_name + '", "state":"off"}] }');
}



ws.onmessage = function (event) {

// Check if its config


// var messages = document.getElementsByTagName('ul')[0],
// message = document.createElement('li'),
// content = document.createTextNode(event.data);
// message.appendChild(content);
// messages.appendChild(message);
};
document.body.appendChild(messages);
