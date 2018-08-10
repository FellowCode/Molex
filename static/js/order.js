$(document).ready(function () {
    updatePrice();
    $('.order-list .order-item #device-show').click(function () {
        var deviceList = $(this).closest('.order-item').find('.device-list');
        if(deviceList.hasClass('hide')) {
            deviceList.removeClass('hide');
            $(this).text('Скрыть список устройств')
        } else {
            deviceList.addClass('hide');
            $(this).text('Показать список устройств')
        }

    })
});

var updatePrice = function () {
    var urls = window.location.href.split('?');
    if(urls[0].includes('/products/order/')) {
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
        $('input[name=goods]').attr('value', urls[1]);
        $('input[name=payment_amount]').attr('value', totalPriceValue);
    }
};