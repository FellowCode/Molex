$(document).ready(function () {
    resizeCarousel();
    removeText($('.index-carousel'));
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
    $('#index.carousel.carousel-slider a.image-container').height(height);
    $('#index.carousel .carousel-item').height(height);
    $('#index.carousel').height(height);
    $("#index.carousel.carousel-slider a.carousel-fixed-item").css('bottom', (height-68)/2);
};

function removeText(element){
    var newElement = $('<' + element[0].nodeName + '/>');
    element.children().each(function(){
        newElement.append(this);
    });
    element.replaceWith(newElement);
}