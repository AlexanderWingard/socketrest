{% for service in services %}
setData({{ call_api(service) | tojson }});
{% endfor %}
var socket = io.connect('http://' + document.domain + ':' + location.port);
socket.on('connect', function() {
    socket.emit('join_rooms', {data: {{services | tojson}}});
});
socket.on('data', function(data) {
    setData(data)
});
