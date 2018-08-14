$(document).ready(function () {
    $('select').formSelect();
    $('.collapsible').collapsible();
    $('.sidenav').sidenav();
    carouselInit();
    mainResize();

    $('.sidenav .category-list .category-item li a').hover(function () {
        $(this).stop().animate({backgroundColor: '#eeeeee', color: '#424242'}, 100);
    }, function () {
        $(this).stop().animate({backgroundColor: '#ffffff', color: '#616161'}, 100);
    });

});
$(window).resize(function () {
   mainResize();
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

var mainResize = function () {
    var windowWidth = $(window).width();
    var paddingRight = 0;
    if (windowWidth > 992){
        paddingRight = windowWidth < 1540 ? 0 : windowWidth - 1540;
        $('.sidenav .category-item .sub-category a.btn').addClass('waves-effect');
    } else {
        $('.sidenav .category-item .sub-category a.btn').removeClass('waves-effect');
    }
    $('.sidenav-padding').css('padding-right', paddingRight);
    $('.nav-wrapper').css('padding-right', paddingRight);
};


