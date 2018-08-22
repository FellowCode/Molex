$(document).ready(function () {
    updatePrice();
    $('.order-list .order-item #device-show').click(function () {
        var deviceList = $(this).closest('.order-item').find('.device-list');
        if(deviceList.hasClass('hide')) {
            deviceList.removeClass('hide');
            $(this).text('Скрыть')
        } else {
            deviceList.addClass('hide');
            $(this).text('Показать')
        }
    });
    $('form').submit(function (e) {
        if (formValidation()) {
            if (Cookies.get('fromCart') === 'true')
                Cookies.remove('cart');
        }
        else
            e.preventDefault();
    });
    $('button#withoutPay').click(function () {
        $('input[name=pay]').attr('value', 'False')
    });
    $('button#withPay').click(function () {
        $('input[name=pay]').attr('value', 'True')
    });

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

function formValidation() {
    var phone = $('input[name=person_phone]').val();
    var name = $('input[name=person_name]').val();
    var email = $('input[name=person_email]').val();

    phone = phone.replace(' ', '');
    name = name.replace(' ', '');
    email = email.replace(' ', '');

    var digits = '0123456789';

    var formValid = true;

    if (name.length < 2) {
        alert('Некорректное имя');
        formValid = false;
    } else {
        var phoneError = false;
        if (phone.length === 11 && phone.charAt(0) === '8') {
            var error = false;
            for (var i = 1; i < 11; i++) {
                if (!digits.includes(phone.charAt(i))) {
                    error = true;
                    return false;
                }
            }
            if (error)
                phoneError = true

        } else
            phoneError = true;

        if (phoneError) {
            alert('Некорректный номер телефона');
            formValid = false
        } else {
            var emailError = false;
            try {
                if (email.split('@').length !== 2 || email.split('@')[1].split('.').length < 2)
                    emailError = true;

            } catch (e) {
                emailError = true;
            }
            if (emailError) {
                alert('Некорректный email');
                formValid = false
            }
        }
    }
    return formValid
}

