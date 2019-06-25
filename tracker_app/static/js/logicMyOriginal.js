// Create map
function createMap(chainStores){

  var lightmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.light",
    accessToken: API_KEY
  });

  // Create a baseMaps object to hold the lightmap layer
  var baseMaps = {
    "Light Map": lightmap
  };

  // Create an overlayMaps object to hold the chainStores layer
  var overlayMaps = {
    "Stores": chainStores
  };

  // Create the map object with options
  var map = L.map("map-id", {
    center: [38,-95.561328],
    zoom: 5,
    layers: [lightmap, chainStores]
  });

  // Create a layer control, pass in the baseMaps and overlayMaps. Add the layer control to the map
  L.control.layers(baseMaps, overlayMaps, {
    collapsed: false
  }).addTo(map);
}

function createMarkers(response) {

  // Pull the "storenumber" property off of response.data
  var totalStoreList = response.all_stores;
  
  // Initialize an array to hold bike markers
  var storeMarkers = [];
  
  // Loop through the totalStoreList array
  for (var index = 0; index < totalStoreList.address.length; index++) {
    // var store_number = totalStoreList[index];
  
    // For each station, create a marker and bind a popup with the station's name
    var storeMarker = L.marker([totalStoreList.latitude[index], totalStoreList.longitude[index]])
      .bindPopup("<h3>" + totalStoreList.address[index] + "<h3><h3>Distributor: " + totalStoreList.distributor[index] + "<h3>");
  
    // Add the marker to the storeMarkers array
    storeMarkers.push(storeMarker);
  }
  
  // Create a layer group made from the bike markers array, pass it into the createMap function
  createMap(L.layerGroup(storeMarkers));
}
  
 
// Perform an API call to the Citi Bike API to get station information. Call createMarkers when complete
d3.json("/data", createMarkers);



// function getColor(d) {
//   return d < 1 ? '#e20000' :
//          d > 3.9 ? '#0ab10d' :
//                  '#e6e61c';
// }
 

//     // Markers on map
//     function createMarkers(chainStoreData){

//         var stores = L.geoJSON(chainStoreData, {
//         onEachFeature: function (data, layer) { 
//             layer.bindPopup(`<h3>Store #${storenumber}, ${status}<br>Case Opportunity: ${caseopportunity}</h3> 
//             Address: ${address}<br>
//             City: ${city}<br>
//             Distributor: ${distributor}<br>
//             Area: ${area}<br>
//             Region: ${region}<br>
//             Case Shipped: ${casesshipped}<br>
//             Case Needed: ${casesneeded}`);
//         },
//         pointToLayer: function (data) {

//             var MarkerOptions = {
//             radius: 10,
//             fillColor: getColor(casesshipped),
//             color: "#000",
//             weight: 1,
//             opacity: 1,
//             fillOpacity: 0.8
//             };
//             return L.circleMarker(latlng, MarkerOptions);
//         }
//         });

//         createMap(stores);
//         }

//         // Depletion data
//         // var link = "data";
//         d3.json("/data").then(function(data){
//         createMarkers(data);
// });