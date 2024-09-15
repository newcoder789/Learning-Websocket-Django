const WebSocket = require('ws');

const wss = new WebSocket.Server({ port: 3000 });

wss.on('connection', (ws) => {
  console.log('A new client connected');
  

  ws.send(JSON.stringify({ message: 'Welcome to the WebSocket server!' }));
  // reply 
  ws.on('message', (message) => {
    if (message== 'hi'){
      ws.send("hello")

    }
    else if(message=='bye'){
      ws.send('goodbye!');
    }
  });


});

console.log('WebSocket server is running on ws://localhost:3000');
