```javascript
// static/js/main.js
$(document).ready(function() {
    var socket = io.connect('http://' + document.domain + ':' + location.port);
    socket.on('balance change', function(msg) {
        $('#balance').text(msg.balance);
    });
});
```
This JavaScript code is used to connect to the Flask-SocketIO server and listen for 'balance change' events. When a 'balance change' event is received, it updates the balance displayed on the page.
