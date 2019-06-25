// Perform an API call to the Citi Bike API to get station information. Call createMarkers when complete
d3.json("/data", createMarkers);

function createMarkers(response) {

  // Pull the "stations" property off of response.data
  var totalStoreList = response.data.stations;

  // Initialize an array to hold bike markers
  var storeMarkers = [];

  // Loop through the stations array
  for (var index = 0; index < totalStoreList.address.length; index++) {
    // var station = stations[index];

    // For each station, create a marker and bind a popup with the station's name
    var storeMarker = L.marker([totalStoreList.latitude[index], totalStoreList.longitude[index]])
    .bindPopup("<h3>" + totalStoreList.address[index] + "<h3><h3>Distributor: " + totalStoreList.distributor[index] + "<h3>");

    // Add the marker to the bikeMarkers array
    storeMarkers.push(storeMarker);
  }

  // Create a layer group made from the bike markers array, pass it into the createMap function
  createMap(L.layerGroup(storeMarkers));
}






// NEW CODE THAT ACTUALLY WORKS
// THIS CREATES THE MAP
var myMap = L.map("map-id", {
  center: [38,-95.561328],
  zoom: 5
});

// THIS (I BELIEVE) CREATES A LAYER CALLED "tileLayer", THAT IS ADDED TO THE MAP VARIABLE "myMap" USING ".addTo(myMap)"
L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/light-v9/tiles/256/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"http://openstreetmap.org\">OpenStreetMap</a> contributors, <a href=\"http://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"http://mapbox.com\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.light",
  accessToken: API_KEY
}).addTo(myMap);


