$(document).ready(function () {
    updatePrice();
});

var updatePrice = function () {
    var totalPriceValue = 0;
    $('.order .order-item').each(function (i) {
       var count = parseInt($(this).find('#count').text());
       var price = parseInt($(this).find('#price').text());
       var optionsPrice = parseInt($(this).find('#options-price').text());
       price += optionsPrice;
       price *= count;
       $(this).find('.price').text(price + ' р.');
       totalPriceValue += price;
    });
    $('.order .total-price').text(totalPriceValue + ' р.');
};