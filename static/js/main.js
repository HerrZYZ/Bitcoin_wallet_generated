## Code: static/js/main.js
```javascript
// Establish a connection to the server
var socket = io.connect('http://' + document.domain + ':' + location.port);

// Listen for the 'balance change' event from the server
socket.on('balance change', function(msg) {
    // Update the balance in the UI
    $('#balance').text(msg.balance);
});

// Function to send Bitcoin
function sendBitcoin(amount, recipient) {
    // Emit the 'send bitcoin' event to the server
    socket.emit('send bitcoin', {amount: amount, recipient: recipient});
}

// Function to receive Bitcoin
function receiveBitcoin(amount, sender) {
    // Emit the 'receive bitcoin' event to the server
    socket.emit('receive bitcoin', {amount: amount, sender: sender});
}
```
