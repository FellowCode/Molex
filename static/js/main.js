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
    categoryWavesEffectUpdate();
});
$(window).resize(function () {
    categoryWavesEffectUpdate();
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

function categoryWavesEffectUpdate() {
    if($(window).width() <= 992)
        $('.sidenav .category-list .category-item .sub-category a').removeClass('waves-effect');
    else
        $('.sidenav .category-list .category-item .sub-category a').addClass('waves-effect');
}


function RemoveAt(str, i) {
    if (str.length > i+1)
        str = str.slice(0,i) + str.slice(i+1);
    else
        str = str.slice(0,i);
    return str
}
