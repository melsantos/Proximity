function getLocation() {
    // var output = document.getElementById("message");

    if (!navigator.geolocation) {
        // output.innerHTML = "Not supported";
        return;
    }

    function success(position) {
        document.getElementById('latitude').value = position.coords.latitude;
        document.getElementById('longitude').value = position.coords.longitude;
        // output.innerHTML = "Success!";
        document.getElementById("geolocation").submit();
        return;
    }

    function error() {
        // output.innerHTML = "geolocation api error";
    }

    // output.innerHTML = "Looking for your location...";
    navigator.geolocation.getCurrentPosition(success, error);
}

function sortPeople(radius) {
    profileList = document.getElementById("profiles");
    profileListItems = profileList.getElementsByTagName('li');

    for (i = 0; i < profileListItems.length; i++) {
        dist = document.getElementsByClassName("distances")[i];
        if (parseFloat(dist.innerHTML) < radius) {
            profileListItems[i].style.display = "";
        } else {
            profileListItems[i].style.display = "none";
        }
    }
}
