function getLocation() {

    var loc = document.getElementById("location");
    
    if(loc !== undefined || loc !== null){
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition((position) => {
                if(loc !== null){
                    loc.innerHTML = "Latitude: " + (position.coords.latitude).toFixed(2) + ", Longitude: " + (position.coords.longitude).toFixed(2);
                }
            });
        } else {
            loc.innerHTML = "Geolocation is not supported by this browser.";
        }
    
    }
}