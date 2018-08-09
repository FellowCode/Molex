$(document).ready(function () {
    resizeCarousel();
    var carousel = $('#index.carousel.carousel-slider');
    setInterval(function () {
        carousel.carousel('next');
    }, 20000);
});

$(window).resize(function () {
    resizeCarousel();
});

var resizeCarousel = function () {
    var carousel = $("#index.carousel");
    var width = carousel.width();
    var height = width/3;
    $('#index.carousel .carousel-item > img').height(height);
    $('#index.carousel .carousel-item').height(height);
    $("#index.carousel.carousel-slider .carousel-fixed-item.with-indicators").css('bottom', (height-68)/2);
};