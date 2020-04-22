var mymap = L.map('mapid').setView([43.654487, -79.380407], 13);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoicHJhamp3b2xtIiwiYSI6ImNrOTQ1cWg5bjA5a2YzaW4xdjIwOXh6NWgifQ.7qjiROoJrPrPijJloe1PBA', {
    maxZoom: 18,
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
        '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
        'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1
}).addTo(mymap);


function addMapMarker(){
    postal_code = document.getElementById('postal_code').value
    console.log(postal_code)
    if (postal_code.length > 5){
        let url = 'https://polished-cloud-foodserver.herokuapp.com/getlatlongfrompostalcode/'+postal_code
        console.log(url)
        axios.get(url)
        .then(data => {
            L.marker([data.data['latLong'][0], data.data['latLong'][1]]).addTo(mymap)
            .bindPopup('Your postal code')
            .openPopup();
        })
        .catch(err => console.log(err))
    }
    
}