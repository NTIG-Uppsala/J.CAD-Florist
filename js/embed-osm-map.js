// Position of the marker and center of the map
const position = [67.86593, 20.2341];

// Check if user is on a computer or mobile device
const isMobile = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);

// Map options including center and zoom level
let mapOptions = {
    center: position,
    zoom: 16,
    dragging: !isMobile,
};

// Create the map
let map = new L.map("map", mapOptions);

// Add the OpenStreetMap tiles
let layer = new L.TileLayer("http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png");
map.addLayer(layer);

// Add a marker
let marker = new L.Marker(position);
marker.addTo(map);
