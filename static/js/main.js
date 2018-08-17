$(document).ready(function () {
    $('select').formSelect();
    $('.collapsible').collapsible();
    $('.sidenav').sidenav();
    carouselInit();

    $('.sidenav .category-list .category-item li a').hover(function () {
        $(this).stop().animate({backgroundColor: '#eeeeee', color: '#424242'}, 100);
    }, function () {
        $(this).stop().animate({backgroundColor: '#ffffff', color: '#616161'}, 100);
    });

});
var carouselInit = function () {
    var carousel = $('.carousel.carousel-slider');
    carousel.carousel({
    fullWidth: true,
    indicators: true
    });
    $('.carousel-fixed-item#left').click(function () {
        carousel.carousel('prev');
    });
    $('.carousel-fixed-item#right').click(function () {
        carousel.carousel('next');
    });
};


