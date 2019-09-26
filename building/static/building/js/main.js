
// Refresh map state 
function maprefresh() {
   if (map) {
       map.invalidateSize();
   }
}



function geojsonload(url, geodata, style, onEachFeature, check) {
    $.ajax({
        url: url,
        async: false,
    }).done(function(res) {
        geodata = L.geoJSON(res, { style: style, onEachFeature: onEachFeature });
        geodata.bringToBack();
        if (check) { map.addLayer(geodata) }
        // $(check).on('change', function(e){
        //   layerTogglefunction(map, geodata, $(this));
        // });

    })

    return geodata
}

function highlightFeature(e) {
    var layer = e.target;

    layer.setStyle({
        weight: 5,
        color: '#666',
        dashArray: '',
        fillOpacity: 0.7,
        fillColor: 'transparent',
    });

    if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
        layer.bringToFront();
    }
}



function loadVectorlayerfunction(url, layername) {
   let loaddata;
   loaddata = L.tileLayer.wms(url, {
       layers: 'cite:' + layername,
       format: 'image/png',
       transparent: true,
   });
   return loaddata;

}


function layerTogglefunction(map, layername, checkbox) {
    if (layername) {
        if (checkbox.prop('checked') == false) {
            map.removeLayer(layername);
        } else {
            map.addLayer(layername);
        }
    } else {
        alert('Layer not is ready for visualisation.');
        checkbox.prop('checked', false)
    }
}




function layerseldefine(mapm, layername, layername1) {
  if (layername1){
    mapm.removeLayer(layername1);
  }
   mapm.addLayer(layername);
   layername1 = layername
   return layername1
}



function removearray(array, itemtoremove ){
  array.splice($.inArray(itemtoremove, array),1);
}



function layerresetHighlight(e) {
    layer.resetStyle(e.target);
}



function geojsonloadpoint(url, geodata, style) {
    $.ajax({
        url: url,
        async: false,
    }).done(function(res) {
        geodata = L.geoJSON(res, {
            pointToLayer: function(feature, latlng) {
                return L.Marker(latlng, style);
            },          
        });
       { map.addLayer(geodata) }
    })

    return geodata
}