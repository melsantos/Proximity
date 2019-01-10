function getLocation() {
    var message = document.getElementById("location");

    if (!navigator.geolocation) {
        message.innerHTML = "<p>Geolocation is not supported by your browser</p>";
        return;
    }

    function success(position) {
        var lat = position.coords.latitude;
        var long = position.coords.longitude;

        message.innerHTML = "Lat: " + twoDec(lat) + " Long: " + twoDec(long);
    }

    function error() {
        message.innerHTML = "Unable to retrieve your location";
    }

    message.innerHTML = "<p>Locating…</p>";

    navigator.geolocation.getCurrentPosition(success, error);
}

function twoDec(num) {
    return Math.round(100 * num) / 100;
}