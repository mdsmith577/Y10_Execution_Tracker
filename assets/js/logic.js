// Create map
function createMap(earthquakeInstances){

  var lightmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 10,
    id: "mapbox.light",
    accessToken: API_KEY
  });

  var map = L.map("map-id", {
    center: [36.7783,-119.4179],
    zoom: 6,
    layers: [lightmap, earthquakeInstances]
    });
    };

  function getColor(d) {
    return d > 5 ? '#FF0000' :
           d > 4 ? '#FF3300' :
           d > 3 ? '#FF6600' :
           d > 2 ? '#FF9900' :
           d > 1 ? '#FFCC00' :
                   '#FFFF00';
  } 

    // Markers on map
    function createMarkers(earthquakeData){

        var earthquakes = L.geoJSON(earthquakeData, {
        onEachFeature: function (feature, layer) {
            layer.bindPopup(`<h3>${feature.properties.place}</h3>
            ${new Date(feature.properties.time)}<br>
            Magnitude: ${feature.properties.mag}`);
        },
        pointToLayer: function (feature, latlng) {

            var geojsonMarkerOptions = {
            radius: 5*feature.properties.mag,
            fillColor: getColor(feature.properties.mag),
            color: "#000",
            weight: 1,
            opacity: 1,
            fillOpacity: 0.8
            };
            return L.circleMarker(latlng, geojsonMarkerOptions);
        }
        });

        createMap(earthquakes);
        }

        // Last 24hr data
        var link = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson";
        d3.json(link, function(data){
        createMarkers(data.features);
});