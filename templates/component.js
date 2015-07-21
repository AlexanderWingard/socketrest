{% for service in services %}
setData({{ call_api(service) | tojson }});
{% endfor %}
socket.on('connect', function() {
    console.log('***', component_name, 'on connect');
    socket.emit('join_rooms', {data: {{services | tojson}}});
});
socket.on('data', function(data) {
    console.log('***', component_name, 'on data', data);
    setData(data)
});
