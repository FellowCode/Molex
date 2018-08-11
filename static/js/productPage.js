$(document).ready(function () {
    resizeFunc();

    var priceStr = $('.product-price').attr('id');
    originPrice = parseInt(priceStr);
    $('ul.multiple-select-dropdown li').click(function () {
        optionSelect()
    });
    $('.product-panel #Buy').click(function () {
        Buy();
    });
    $('.product-panel #toCart').click(function () {
        if (checkIntoCart())
            deleteFromCart();
        else
            addToCart();
        cartBtnChange();
        cartNavbarUpdate();
    });
    cartBtnChange();
    $('.product-panel .count .remove').click(function () {
        var input = $('.product-panel .count input');
        var value = parseInt(input.val());
        if(value>1)
            input.val(value-1);
    });
    $('.product-panel .count .add').click(function () {
        var input = $('.product-panel .count input');
        input.val(parseInt(input.val())+1);
    });
});
$(window).resize(function () {
    resizeFunc();
});


var resizeFunc = function() {
    var carousel = $(".product-panel .carousel");
    var width = carousel.width();
    var height = carousel.height();
    if ($(window).width() > 601) {
        height = width < 400 ? width : height > width ? width : height;
        height = height > 400 ? 400 : height;
    } else
        height = 300;
    carousel.height(height);
    $('.product-panel .carousel-item > img').height(height);
    $('.product-panel .carousel-item > img').width(height);
    $(".product-panel .carousel.carousel-slider .carousel-fixed-item.with-indicators").css('bottom', (height-68)/2);
    height = $(window).width() < 584 ? height+330 : height;
    if($('.product-panel .select-color').length === 0)
        height-=60;
    if($('.product-panel .select-options').length === 0)
        height-=60;
    $(".product-panel").css('min-height', height+20);
};


/*   PRODUCT PAGE  */
/* select color and options */

var originPrice = 0;
var colorPrice = 0;
var optionsPrice = 0;
var options_id = [];
var colorId = null;

$('.select-color').change(function () {

    var selected = $('.select-color option:selected');
    colorId = selected.attr('value');
    var addedPriceStr = selected.attr('name');
    colorPrice = parseInt(addedPriceStr);
    var newPrice = String(originPrice + colorPrice + optionsPrice);
    $('.product-price').html(newPrice + ' Р.');

    var count = parseInt(selected.attr('count'));
    if(count > 0)
        $('.product-panel #existence').text('В наличии: ' + count + ' шт.');
    else {
        var deliveryDays = $('#deliveryDays').text();
        $('.product-panel #existence').text('Под заказ: ' + deliveryDays + ' д.');
        $('.product-panel #Buy>#text').text('Заказать');
    }
    cartBtnChange();
});

var optionSelect = function() {
    optionsPrice = 0;
    options_id = [];
    $('ul.multiple-select-dropdown li').each(function (i) {
        if(i>0 && $(this).hasClass('selected')) {
            var option = $('select.select-options option').eq(i);
            optionsPrice += parseInt(option.attr('name'));
            options_id.push(option.attr('value'));
        }
    });
    var newPrice = String(originPrice + colorPrice + optionsPrice);
    $('.product-price').html(newPrice + ' Р.');
};

var checkIntoCart = function () {
    var deviceId = $('#deviceId').text();
    var category = $('#category').text();
    var cartForm = Cookies.getJSON('cart');
    var exist = false;
    if(cartForm.hasOwnProperty(category)) {
        $.each(String(cartForm[category]).split('~'), function (i, elem) {
            var values = String(elem).split('.');
            if (deviceId === values[0] && colorId === values[1])
                exist = true;
        });
    }
    return exist;
};

var cartBtnChange = function () {
    var cartBtn = $('.product-panel #toCart');
    if (checkIntoCart()){
        cartBtn.find('i').text('check');
        cartBtn.find('div').text('В корзине');
        cartBtn.removeClass('red', 'darken-1');
        cartBtn.addClass('orange', 'darken-4')
    }
    else {
        cartBtn.find('i').text('add_shopping_cart');
        cartBtn.find('div').text("В корзину");
        cartBtn.removeClass('orange', 'darken-4');
        cartBtn.addClass('red', 'darken-1')
    }
};

var deleteFromCart = function () {
    var device_id = $('#deviceId').text();
    var category = $('#category').text();
    var cartForm = Cookies.getJSON('cart');
    cartForm['count']--;
    var devices = cartForm[category].split('~');
    var str = '';
    $.each(devices, function (i, device) {
        var vals = device.split('.');
        if(vals[0] !== device_id || vals[1] !== colorId){
            str += '~' + device;
        }
    });
    cartForm[category] = str.slice(1);
    if (cartForm[category] === '')
        delete cartForm[category];
    Cookies.set('cart', cartForm);
};

var Buy = function () {
    if($('.product-panel .select-color').length > 0 && colorId === null)
        alert('Выберите цвет');
    else {
        var deviceId = $('#deviceId').text();
        var category = $('#category').text();
        var deviceCount = $('.product-panel .count input').val();
        var deviceStr = deviceId  + '.' + colorId + '.' + deviceCount;
        $.each(options_id, function (i, elem) {
            deviceStr += '.' + elem;
        });
        Cookies.set('fromCart', 'false');
        var url = '/products/order/?' + category + '=' + deviceStr;
        window.location.href = url;
    }
};