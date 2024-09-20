const position = [67.86593, 20.2341];

let mapOptions = {
    center: position,
    zoom: 18,
};

let map = new L.map("map", mapOptions);

let layer = new L.TileLayer("http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png");
map.addLayer(layer);

let marker = new L.Marker(position);
marker.addTo(map);
