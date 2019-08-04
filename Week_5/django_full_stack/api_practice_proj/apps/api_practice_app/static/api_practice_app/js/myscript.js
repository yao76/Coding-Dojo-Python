function initMap() {
    var myLatLng = { lat: 47.606, lng: -122.3321 };
    var myLatLng2 = { lat: 34.606, lng: -122.3321 };

    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 4,
        center: myLatLng
    });

    var marker = new google.maps.Marker({
        position: myLatLng,
        map: map,
        title: 'Butthole!'
    });
    var marker2 = new google.maps.Marker({
        position: myLatLng2,
        map: map,
        title: 'Butthole2!'
    });
}