// Position of the marker and center of the map
const position = [data.data.companyAddressCoordinatesLat, data.data.companyAddressCoordinatesLng];

// Map options including center and zoom level
let mapOptions = {
    center: position,
    zoom: 16,
    gestureHandling: true,
};

// Create the map
let map = new L.map("map", mapOptions);

// Add the OpenStreetMap tiles
let layer = new L.TileLayer("http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png");
map.addLayer(layer);

// Add a marker
let marker = new L.Marker(position);
marker.addTo(map);
