// Position of the marker and center of the map
const position = [67.86593, 20.2341];

// Map options including center and zoom level
let mapOptions = {
    center: position,
    zoom: 16,
};

// Create the map
let map = new L.map("map", mapOptions);

// Add the OpenStreetMap tiles
let layer = new L.TileLayer("http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png");
map.addLayer(layer);

// Add a marker
let marker = new L.Marker(position);
marker.addTo(map);
