$(document).ready(function () {
    resizeCarousel();
    removeText($('.index-carousel'));
    var carousel = $('#index.carousel.carousel-slider');
    setInterval(function () {
        carousel.carousel('next');
    }, 20000);
    valignCards();
});

$(window).resize(function () {
    resizeCarousel();
    valignCards();
});

var resizeCarousel = function () {
    var carousel = $("#index.carousel");
    var width = carousel.width();
    var height = width/3;
    $('#index.carousel .carousel-item > img').height(height);
    $('#index.carousel .carousel-item').height(height);
    $('#index.carousel').height(height);
    $("#index.carousel.carousel-slider .carousel-fixed-item.with-indicators").css('bottom', (height-68)/2);
};

function removeText(element){
    var newElement = $('<' + element[0].nodeName + '/>');
    element.children().each(function(){
        newElement.append(this);
    });
    element.replaceWith(newElement);
}

function valignCards() {
    var columnCount = 4;
    var windowWidth = $(window).width();
    if (windowWidth <= 600)
        columnCount = 1;
    else if(windowWidth <=1200)
        columnCount = 3;

    var rowItem = 0;
    var rowCardHeight = [];
    var rowCard = [];
    if(windowWidth > 600) {
        $('.card').each(function (i) {
            rowItem++;
            rowCardHeight.push($(this).height());
            rowCard.push($(this));
            if (rowItem > columnCount-1 || i === $('.card').length-1) {
                var max = Math.max.apply(Math, rowCardHeight);
                $.each(rowCard, function (i, elem) {
                    var dif = max - elem.height();
                    var cardContent = elem.find('.card-content');
                    cardContent.height(cardContent.height()+dif);
                });
                rowItem = 0;
                rowCardHeight = [];
                rowCard = [];
            }
        });
    }
}