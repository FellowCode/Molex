$(document).ready(function () {
    $('select').formSelect();
    $('.collapsible').collapsible();
    carouselInit();
});



var carouselInit = function () {
    var carousel = $('.carousel.carousel-slider');
    carousel.carousel({
    fullWidth: true,
    indicators: true
    });
    $('.carousel-fixed-item > #left').click(function () {
        carousel.carousel('prev');
    });
    $('.carousel-fixed-item > #right').click(function () {
        carousel.carousel('next');
    });
};



