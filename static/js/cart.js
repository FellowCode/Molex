$(document).ready(function () {
    cartInit();
    resize();
    cartUpdatePrices()
});

$(window).resize(function () {
    resize();
});

var cartInit = function () {
    //Cookies.remove('cart');
    var cartForm = Cookies.getJSON('cart');
    if(typeof cartForm === 'undefined') {
        cartForm = {'count': 0};
        Cookies.set('cart', cartForm);
    }
   setCartNavbar(cartForm);
   $('a[name=cart]').click(function () {
       cartOpen();
   });
    $('.cart-item #delete').click(function () {
        removeFromCart($(this).closest('.cart-item'));
        cartUpdatePrices();
        cartNavbarUpdate();
    });
   $('.cart-item .count .remove').click(function () {
       var input = $(this).siblings('input');
       var value = parseInt(input.val());
       if (value>1)
           input.val(parseInt(input.val()) -1);
       onChangeCartItemCount($(this).closest('.cart-item'));
       cartUpdatePrices();
   });
    $('.cart-item .count .add').click(function () {
       var input = $(this).siblings('input');
       input.val(parseInt(input.val())+1);
       onChangeCartItemCount($(this).closest('.cart-item'));
       cartUpdatePrices();
   });
    $('.cart-item .count input').change(function () {
        cartUpdatePrices();
        onChangeCartItemCount($(this).closest('.cart-item'));
    })
};
var cartNavbarUpdate = function () {
    setCartNavbar(Cookies.getJSON('cart'))
};
var setCartNavbar = function(cartForm) {
    if(cartForm['count'] > 0) {
        $('#nav-cart').get(0).lastChild.nodeValue = cartForm['count'];
        $('#nav-cart-text').get(0).lastChild.nodeValue = 'Корзина: ' + cartForm['count'];
    }
    else
    {
         $('#nav-cart').get(0).lastChild.nodeValue = '';
         $('#nav-cart-text').get(0).lastChild.nodeValue = 'Корзина';
    }
};
var cartOpen = function () {
    var cartForm = Cookies.getJSON('cart');
    delete cartForm['count'];
    let urlParameters = Object.entries(cartForm).map(e => e.join('=')).join('&');
    let url = '/products/cart/?' + urlParameters;
    window.location.href = url;
};

var resize = function () {
    if ($(window).width() < 601) {
        $('#row-on-small').addClass('row');
        $('#cart-total .total-price').removeClass('right-align');
        $('#cart-total .total-price').addClass('center-align');
    }
    else {
        $('#row-on-small').removeClass('row');
        $('#cart-total .total-price').addClass('right-align');
        $('#cart-total .total-price').removeClass('center-align');
    }

};

var addToCart = function () {
    var deviceId = $('#deviceId').text();
    var category = $('#category').text();
    var deviceCount = $('.count input').val();
    var deviceStr = deviceId  + '.' + colorId + '.' + deviceCount;
    if($('.product-panel .select-color').length > 0 && colorId === null)
        alert('Выберите цвет');
    else {
        $.each(options_id, function (i, elem) {
            deviceStr += '.' + elem;
        });
        var cartForm = Cookies.getJSON('cart');
        if(typeof cartForm === 'undefined')
            cartForm = {'count': 0};
        if(cartForm.hasOwnProperty(category)) {
            var exist = false;
            $.each(String(cartForm[category]).split('~'), function (i, elem) {
                var values = String(elem).split('.');
                if (deviceId === values[0] && colorId === values[1])
                    exist = true;
            });
            if (!exist) {
                cartForm[category] = cartForm[category] + '~' + deviceStr;
                cartForm['count']++;
            }
        }
        else {
            cartForm[category] = deviceStr;
            cartForm['count']++;
        }
        Cookies.set('cart', cartForm);
        setCartNavbar(cartForm);
    }
};

var removeFromCart = function (cartItem) {
    var category = cartItem.find("#category").text();
    var device_id = cartItem.find('#device_id').text();
    var color_id = cartItem.find('#color_id').text();

    cartItem.remove();

    var cartForm = Cookies.getJSON('cart');
    cartForm['count']--;
    var devices = cartForm[category].split('~');
    var str = '';
    $.each(devices, function (i, device) {
        var vals = device.split('.');
        if(vals[0] !== device_id || vals[1] !== color_id){
            str += '~' + device;
        }
    });
    cartForm[category] = str.slice(1);
    if (cartForm[category] === '')
        delete cartForm[category];
    Cookies.set('cart', cartForm);
    delete cartForm['count'];
    let urlParameters = Object.entries(cartForm).map(e => e.join('=')).join('&');
    let url = '/products/cart/?' + urlParameters;
    history.pushState(null, $(document).title, url);
};

var cartUpdatePrices = function () {
    var cartTotalPriceObj = $('#cart-total .total-price');
    if (typeof cartTotalPriceObj !== 'undefined') {
        var cartTotalPriceValue = 0;
        $('.cart-container .cart-item').each(function (i) {
            var price = parseInt($(this).find('#price').text());
            var options_price = parseInt($(this).find('#options-price').text());
            var count = parseInt($(this).find('.count input').val());
            price*=count;
            options_price*=count;
            $(this).find('.price .main').text(price + ' Р.');
            if (options_price>0)
                $(this).find('.price .extra').text('+' + options_price + ' Р.');
            cartTotalPriceValue += price + options_price
        });
        cartTotalPriceObj.text(cartTotalPriceValue + ' Р.')
        if (cartTotalPriceValue>0) {
            $('#cart-total a.btn-large').removeClass('disabled');
            var cartForm = Cookies.getJSON('cart');
            delete cartForm['count'];
            let urlParameters = Object.entries(cartForm).map(e => e.join('=')).join('&');
            let url = '/products/order/?' + urlParameters;
            $('#cart-total a.btn-large').attr('href', url);
        }
        else
            $('#cart-total a.btn-large').addClass('disabled');
    }
};

var onChangeCartItemCount = function (cartItem) {
       var input = $(this).siblings('input');
       var category = cartItem.find("#category").text();
       var device_id = cartItem.find('#device_id').text();
       var color_id = cartItem.find('#color_id').text();
       var cartForm = Cookies.getJSON('cart');
       var devices = cartForm[category].split('~');
       var str = '';
        $.each(devices, function (i, device) {
            var vals = device.split('.');
            if(vals[0] === device_id || vals[1] === color_id){
                var deviceModify = '';
                vals[2] = input.val();
                $.each(vals, function (i, elem) {
                    deviceModify += '.' + elem;
                });
                str += deviceModify.slice(1);
            }
            else {

                str += '~' + device;
            }
        });
        cartForm[category] = str.slice(1);
        Cookies.set('cart', cartForm);
        delete cartForm['count'];
        let urlParameters = Object.entries(cartForm).map(e => e.join('=')).join('&');
        let url = '/products/cart/?' + urlParameters;
        history.pushState(null, $(document).title, url);
};
