function initMap() {
    // Set the center of the map to Chembur, Mumbai
    var chembur = new google.maps.LatLng(19.0558, 72.8826);
    var map = new google.maps.Map(document.getElementById('map'), {
        center: chembur,
        zoom: 14
    });

    // Search for nearby hospitals in Chembur
    var request = {
        location: chembur,
        radius: '5000',
        type: ['hospital']
    };

    var service = new google.maps.places.PlacesService(map);
    service.nearbySearch(request, function (results, status) {
        if (status === google.maps.places.PlacesServiceStatus.OK) {
            // Display the list of nearby hospitals
            var resultList = document.getElementById('result-list');
            for (var i = 0; i < results.length; i++) {
                var place = results[i];
                var listItem = document.createElement('li');
                listItem.appendChild(document.createTextNode(place.name));
                resultList.appendChild(listItem);

                // Add a marker for the place
                var marker = new google.maps.Marker({
                    map: map,
                    position: place.geometry.location,
                    title: place.name,
                });
            }
        }
    });
}