$(document).ready(function(){
  $("#interest-form").hide();
  $("#why-adopt").hide();
  $("#about-petter").hide();
  $("#app-main").hide();
  $("#start-menu").hide();
  $("#list-page").hide();
  $(".notification").hide();

  $("#welcome-logo").hide();
  $("#welcome-text h1").hide();
  $("#welcome-text p").hide();
  $("#swipe-start").hide();
  $("#welcome-desc").hide();
  $("#welcome-logo").fadeIn(900);
  $("#welcome-text h1").fadeIn(900);
  $("#welcome-text p").delay(1000);
  $("#welcome-text p").fadeIn(900);
  $("#swipe-start").delay(2000);
  $("#welcome-desc").delay(2000);
  $("#swipe-start").fadeIn(900);
  $("#welcome-desc").fadeIn(900);
  $("#start-menu").fadeIn(900);
  var swiperV = new Swiper ('.swiper-container-v', {
    direction: 'vertical',
    loop: false,
    allowSlidePrev: false,
    speed: 750,
    resistance : true,
    resistanceRatio : 0,
    navigation: {
      nextEl: '.swiper-button-next'
    },
  });

  $("#start-about").click(function(){
    $("#start-menu").fadeOut(300);
    $("#about-petter").delay(300);
    $("#about-petter").fadeIn(300);
  });

  $("#about-back").click(function(){
    $("#about-petter").fadeOut(300);
    $("#start-menu").delay(300);
    $("#start-menu").fadeIn(300);
  });

  $("#start-why").click(function(){
    $("#start-menu").fadeOut(300);
    $("#why-adopt").delay(300);
    $("#why-adopt").fadeIn(300);
  });

  $("#why-back").click(function(){
    $("#why-adopt").fadeOut(300);
    $("#start-menu").delay(300);
    $("#start-menu").fadeIn(300);
  });

  $("#int-back").click(function(){
    $("#interest-form").fadeOut(300);
    $("#start-menu").delay(300);
    $("#start-menu").fadeIn(300);
  });

  $("#start-app").click(function(){
    $("#start-menu").fadeOut(300);
    $("#interest-form").delay(300);
    $("#interest-form").fadeIn(300);
  });

  $("#interest-submit").click(function(){
    $("#interest-form").fadeOut(300);
    $("#list-page").fadeOut(300);
    $("#app-main").delay(300);
    $("#pet-browser").delay(300);
    $(".actions").delay(300);
    $(".actions").fadeIn(300);
    $("#app-main").fadeIn(300);
    $("#pet-browser").fadeIn(300);
  });

  $("#back").click(function(){
    $("#app-main").fadeOut(300);
    $("#interest-form").delay(300);
    $("#interest-form").fadeIn(300);
  });

  $("#list").click(function(){
    $("#pet-browser").fadeOut(300);
    $(".actions").fadeOut(300);
    $("#list-page").delay(300);
    $("#list-page").fadeIn(300);
  });

  $("#browse").click(function(){
    $("#list-page").fadeOut(300);
    $(".actions").delay(300);
    $(".actions").fadeIn(300);
    $("#pet-browser").delay(300);
    $("#pet-browser").fadeIn(300);
  });

  var swiperS = new Swiper ('.swiper-container-scroll', {
    direction: 'vertical',
    autoHeight: true,
    //scrollbar: {
    //   el: '.swiper-scrollbar',
    //},
  });

});

var swiperH = new Swiper ('.swiper-container-h', {
  direction: 'horizontal',
  loop: false,
  speed: 500,
  pagination: {
    el: '.swiper-pagination',
    clickable: true,
  },
});

//map

var mymap = L.map('mapid').setView([29.654 , -82.330], 10.5);

L.tileLayer('https://api.mapbox.com/styles/v1/cinnar12/cja4q8sws2u1i2rrybmqogiyx/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoiY2lubmFyMTIiLCJhIjoiY2pnbW05bTIzMDBrZzJ3b2dyZHJuM294YyJ9.KlNNs1K3UteMLBMyBYoZOA', {
  attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
    id: 'mapbox.streets',
    accessToken: 'pk.eyJ1IjoiY2lubmFyMTIiLCJhIjoiY2pnbW05bTIzMDBrZzJ3b2dyZHJuM294YyJ9.KlNNs1K3UteMLBMyBYoZOA',
    maxZoom: 18
  }).addTo(mymap);

for ( var i=0; i < places.length; i++) {
  L.marker( [places[i].latitude, places[i].longitude] ) .bindPopup( '<b>' + places[i].placeName + '</b>').addTo( mymap );
}
