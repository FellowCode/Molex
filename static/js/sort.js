$(document).ready(function () {
    var state = 'up';
    var sort = 'price';
    let sortValue = Cookies.get('sort');
    if (typeof sortValue !== 'undefined') {
        sort = sortValue.split('.')[0];
        state = sortValue.split('.')[1];
        $('.category .sort .sort-item i').text('');
        if (state === 'up')
            $('.category .sort .sort-item#' + sort + ' i').text('arrow_drop_up');
        else
            $('.category .sort .sort-item#' + sort + ' i').text('arrow_drop_down');
        Sort(sort, state)
    }
    var icon = '';
    $('.category .sort .sort-item').click(function () {
        $('.category .sort .sort-item i').text('');
        if($(this).attr('id') === sort){
            if(state === 'up') {
                state = 'down';
                icon = 'arrow_drop_down';
            } else {
                state = 'up';
                icon = 'arrow_drop_up';
            }
        } else {
            sort = $(this).attr('id');
            state = 'up';
            icon = 'arrow_drop_up';
        }
        $(this).find('i').text(icon);
        sortValue = sort + '.' + state;
        Cookies.set('sort', sortValue);
        Sort(sort, state);
    });
});
function Sort(sort, state) {
    if (sort === 'price') {
        if (state === 'up')
            sortPriceAscending();
        else
            sortPriceDescending();
    } else if (sort === 'name'){
        if (state === 'up')
            sortNameAscending();
        else
            sortNameDescending();
    } else if (sort === 'instock') {
        if (state === 'up')
            sortInstockAscending();
        else
            sortInstockDescending();
    }
}
function sortPriceAscending() {
    var products = $('.category .category-item');
    products.sort(function (a,b) {
        return $(a).data("price")-$(b).data("price");
    });
    $('.category div#list').html(products);
}
function sortPriceDescending() {
    var products = $('.category .category-item');
    products.sort(function (a,b) {
        return $(b).data("price")-$(a).data("price");
    });
    $('.category div#list').html(products);
}
function sortNameAscending() {
    var products = $('.category .category-item');
    products.sort(function (a,b) {
        var keyA = $(a).data("name");
        var keyB = $(b).data("name");
        return (keyA > keyB) ? 1 : 0;
    });
    $('.category div#list').html(products);
}
function sortNameDescending() {
    var products = $('.category .category-item');
    products.sort(function (a,b) {
        var keyA = $(a).data("name");
        var keyB = $(b).data("name");
        return (keyA < keyB) ? 1 : 0;
    });
    $('.category div#list').html(products);
}
function sortInstockAscending() {
    var products = $('.category .category-item');
    products.sort(function (a,b) {
        return $(a).data("instock")-$(b).data("instock");
    });
    $('.category div#list').html(products);
}
function sortInstockDescending() {
    var products = $('.category .category-item');
    products.sort(function (a,b) {
        return $(b).data("instock")-$(a).data("instock");
    });
    $('.category div#list').html(products);
}