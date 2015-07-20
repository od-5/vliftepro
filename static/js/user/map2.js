// 
// $(function(){
ymaps.ready(init);
var myMap;

function init(){
    city = $('body').data('city');
    var coord = ''
    var myGeocoder = ymaps.geocode(city);
        myGeocoder.then(
            function (res) {
                coord = res.geoObjects.get(0).geometry.getCoordinates();
                myMap = new ymaps.Map("YMapsID", {
                    center: coord,
                    zoom: 11
                });
            },
            function (err) {
                coord = [48.707103, 44.516939];
                myMap = new ymaps.Map("YMapsID", {
                    center: coord,
                    zoom: 11
                });
            }
        );
    console.log(coord);
    //myMap = new ymaps.Map("YMapsID", {
    //    center: coord,
    //    zoom: 11
    //});
    //console.log(ymaps.geocode('Волгоград', { results: 1 }));
    $.get("/map/",
        function(e) {
            //var data = JSON.parse(e); // получаем данные от сервера
            //console.log(e);
            function outputItem(item, i, e) {
                myMap.geoObjects.add(
                    new ymaps.Placemark([item['coord_y'], item['coord_x']], {
                    balloonContent: item['address'],
                    hintContent: item['name']
                    })
                );
            }
            e.forEach(outputItem);
        }
    );


    $('.city-menu-wrap li.ch').click(function(){
        var city = $(this).text();
        ymaps.geocode(city, { results: 1 })
        .then(function (res) {
            myMap.panTo(res.geoObjects.get(0).geometry.getCoordinates(),
                {
                    flying: true
                }
            )
            console.log(res.geoObjects.get(0).geometry.getCoordinates())
        });
        // alert('Hello');
        
    });

}