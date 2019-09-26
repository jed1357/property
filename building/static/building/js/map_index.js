// const placesurl = "/property/places"
const conflicturl = "/property/conflict"
const districtsurl = "/property/district"
const schoolsurl = "/property/school"
const healthurl = "/property/health"
const roadsurl = "/property/roads"
const policeurl = "/property/police"
const fireurl = "/property/fire"
const gamaurl = "/property/gama"


// var map = addtomap('mapid', true);

// L.control.browserPrint({ title: 'MAP' }).addTo(map)
//OSM tiles attribution and URL
var osmLink = '<a href="http://openstreetmap.org">OpenStreetMap</a>';
var osmURL = 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
var osmAttrib = '&copy; ' + osmLink;

//Carto tiles attribution and URL
var cartoLink = '<a href="http://openstreetmap.org">OpenStreetMap</a>';
var cartoURL = 'https://maps.wikimedia.org/osm-intl/{z}/{x}/{y}{r}.png';
var cartoAttrib = '&copy; ' + osmLink + ' &copy; ' + cartoLink;

//Stamen Toner tiles attribution and URL
var stamenURL = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}';
var stamenAttrib = '© Data <a href="https://openstreetmap.org/copyright/">OpenStreetMap</a> © Map <a href="https://mapbox.com/">Mapbox</a> © 3D <a href="https://osmbuildings.org/copyright/">OSM Buildings</a>';

//Creation of map tiles
var osmMap = L.tileLayer(osmURL, {attribution: osmAttrib});
var cartoMap = L.tileLayer(cartoURL, {attribution: cartoAttrib});
var stamenMap = L.tileLayer(stamenURL,{
  attribution: stamenAttrib,
  subdomains: 'abcd',
  minZoom: 0,
  maxZoom: 20,
  ext: 'png'
});

//Map creation
var map = L.map('mapid',{
  layers: [osmMap]
}).setView([7.799, -1], 7);

//Base layers definition and addition
var baseLayers = {
  "OSM Mapnik": osmMap,
  "Carto DarkMatter": cartoMap,
  "Stamen Toner": stamenMap
};

 //Add baseLayers to map as control layers
 L.control.layers(baseLayers).addTo(map);



function zoomToFeature(e) {
    map.fitBounds(e.target.getBounds());
}



function districtstye() {
    return {
        fillColor: 'transparent',
        weight: 3,
        opacity: 1,
        color: '#2c3638',
        dashArray: '',
        fillOpacity: 0.7
    }
}


function districtresetHighlight(e) {
    districtboundary.resetStyle(e.target);
}


function districtzoomToFeature(e){
  map.fitBounds(e.target.getBounds());
}

function districtonEachFeature(feature, layer) {
    layer.on({
        mouseover: highlightFeature,
        mouseout: districtresetHighlight,
        click: zoomToFeature
    });
//      layer.bindPopup(`<table class='table table-bordered'><tr><td><b>External Diameter</b></td><td><b>${feature.properties.ext_diamet} m</b></td></tr><tr><td><b>Internal Diameter</b></td><td><b>${feature.properties.int_diamet} m</b></td></tr><tr><td><b>Data Source</b></td><td><b>${feature.properties.datasource}</b></td>
//              </tr><tr><td><b>Type</b></td><td><b>${feature.properties.mtype}</b></td></tr><tr><td><b>Year</b></td><td><b>${feature.properties.year}</b></td></tr></table>`);
// }
}


var districtboundary = geojsonload(districtsurl, districtboundary, districtstye, districtonEachFeature, 'check')
districtboundary.on('mouseover', function(e){
    e.layer.bindTooltip(e.layer.feature.properties.district_n).openTooltip();
})
$('#districtCheck').on('change', function(e){
  if (districtboundary) {
    layerTogglefunction(map, districtboundary, $(this));
  }
});



function ratestye() {
    return {
        fillColor: 'transparent',
        weight: 3,
        opacity: 1,
        color: '#2c3638',
        dashArray: '',
        fillOpacity: 0.7
    }
}

function rateresetHighlight(e) {
    rateboundary.resetStyle(e.target);
}


function ratezoomToFeature(e){
  map.fitBounds(e.target.getBounds());
}

function rateonEachFeature(feature, layer) {
    layer.on({
        mouseover: highlightFeature,
        mouseout: districtresetHighlight,
        click: zoomToFeature
    });
     layer.bindPopup(`<table class='table table-bordered'><tr><td><b>Region</b></td><td><b>${feature.properties.region}</b></td></tr><tr><td><b>District</b></td><td><b>${feature.properties.district}</b></td></tr><tr><td><b>Safety</b></td><td><b>${feature.properties.safety}</b></td>
             </tr><tr><td><b>Amenities</b></td><td><b>${feature.properties.amenities}</b></td></tr></table>`);
}

var rateboundary = geojsonload(gamaurl, rateboundary, ratestye, rateonEachFeature, 'check')
rateboundary.on('mouseover', function(e){
    e.layer.bindTooltip(e.layer.feature.properties.district).openTooltip();
})
$('#rateCheck').on('change', function(e){
  if (rateboundary) {
    layerTogglefunction(map, rateboundary, $(this));
  }
});



L.easyButton('fa-reply', function(addtomap) {
    map.setView([7.799, -1], 7)
}).addTo(map);



L.easyButton('fa fa-close', function(redirectpage) {
    location.replace("#")
}).addTo(map);



// for points marker popup
// var datas = '/static/building/js/address.json';
// var poiLayers
// $.getJSON(datas, function(data){
//      poiLayers = L.geoJSON(data, {
//         onEachFeature: function(feature, layer) {
//             layer.bindPopup(`<table class='table table-bordered'><tr><td><b>External Diameter</b></td><td><b>${feature.properties.ext_diamet} m</b></td></tr><tr><td><b>Internal Diameter</b></td><td><b>${feature.properties.int_diamet} m</b></td></tr><tr><td><b>Data Source</b></td><td><b>${feature.properties.datasource}</b></td>
//             </tr><tr><td><b>Type</b></td><td><b>${feature.properties.mtype}</b></td></tr><tr><td><b>Year</b></td><td><b>${feature.properties.year}</b></td></tr></table>`);
//             }
//         }).addTo(map)
// });





// fire
function geojsonloadpoint(url, geodata) {
    $.ajax({
        url: url,
        async: false,
    }).done(function(res) {
        geodata = L.geoJSON(res, {
            pointToLayer: function(feature, latlng) {
              var smallIcon = L.icon({
                iconSize: [30, 30],
                iconAnchor: [30, 26],
                popupAnchor:  [1, -24],
                iconUrl: '/static/building/css/images/fire.png'
            });
              return L.marker(latlng, {icon: smallIcon});
    }            
        });
        geodata.bringToBack();
       { map.addLayer(geodata) }
    })
    return geodata
}
var fires = geojsonloadpoint(fireurl, fires)




// police
function geojsonloadpoint1(url, geodata) {
    $.ajax({
        url: url,
        async: false,
    }).done(function(res) {
        geodata = L.geoJSON(res, {
            pointToLayer: function(feature, latlng) {
              var smallIcon = L.icon({
                iconSize: [30, 30],
                iconAnchor: [30, 26],
                popupAnchor:  [1, -24],
                iconUrl: '/static/building/css/images/policeman.png'
            });
              return L.marker(latlng, {icon: smallIcon});
    }            
        });
        geodata.bringToBack();
       { map.addLayer(geodata) }
    })
    return geodata
}
var police = geojsonloadpoint1(policeurl, police)


// school
function geojsonloadpoint2(url, geodata) {
    $.ajax({
        url: url,
        async: false,
    }).done(function(res) {
        geodata = L.geoJSON(res, {
            pointToLayer: function(feature, latlng) {
              var smallIcon = L.icon({
                iconSize: [30, 30],
                iconAnchor: [30, 26],
                popupAnchor:  [1, -24],
                iconUrl: '/static/building/css/images/school.png'
            });
              return L.marker(latlng, {icon: smallIcon});
    }            
        });
        geodata.bringToBack();
       { map.addLayer(geodata) }
    })
    return geodata
}
var school = geojsonloadpoint2(schoolsurl, school)



// health
// function geojsonloadpoint3(url, geodata) {
//     $.ajax({
//         url: url,
//         async: false,
//     }).done(function(res) {
//         geodata = L.geoJSON(res, {
//             pointToLayer: function(feature, latlng) {
//               var smallIcon = L.icon({
//                 iconSize: [10, 10],
//                 iconAnchor: [10, 12],
//                 popupAnchor:  [1, -24],
//                 iconUrl: '/static/building/css/images/hospital.png'
//             });
//               return L.marker(latlng, {icon: smallIcon});
//     }            
//         });
//         geodata.bringToBack();
//        { map.addLayer(geodata) }
//     })
//     return geodata
// }
// var health = geojsonloadpoint3(healthurl, health)