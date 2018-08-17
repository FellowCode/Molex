$(document).ready(function () {
    $('#openFilters').click(function () {
        $('#sidenav-category').css('display','none');
        $('#sidenav-filter').css('display', 'block');
    });
    $('#closeFilters').click(function () {
        $('#sidenav-filter').css('display', 'none');
        $('#sidenav-category').css('display','block');
    });
    checkFilterApply();


    FilterInitialize();

    $(window).on('popstate', function() {
        loadPage(window.location.href);
    });
});
var error;
var FilterInitialize = function () {
    var properties = $('#filterProperties').text().split(';');
    var fullSlug = $('#fullCategory').text();
    var filterData = {};
    $.each(properties, function (i, elem) {
        var vals = elem.split(':');
        filterData[vals[0]] = vals[1];
    });
    $('a#Filter').click(function () {
        error = false;
        var form = assemblyFormData(filterData);
        if (!error)
            filterProducts(form);
    });
    $('#resetFilter').click(function () {
        var url = window.location.href.split('?')[0];
        $('#list-container').load(url + ' #list');
        history.pushState(null, $(document).title, url);
        checkFilterApply();
    });
    var filterProducts = function(form) {
        let urlParameters = Object.entries(form).map(e => e.join('=')).join('&');
        let url = '/products/' + fullSlug + '/?' + urlParameters;
        $('#list-container').load(url + ' #list');
        history.pushState(null, $(document).title, url);
        checkFilterApply();
    };
};

var getCheckboxValues = function (name) {
    var values = [];
    $('input[name='+name+']:checked').each(function (i) {
        values.push($(this).val());
    });
    return String(values).replace(new RegExp(',','g'), '~');
};


var getRangeValues = function (name) {
    var elem = 'input[name='+name;
    var min = $(elem+'_min]').val();
    var max = $(elem+'_max]').val();
    if (parseFloat(min) > parseFloat(max) && !error){
        alert('Неправильный формат в поле \"' + $(elem+'_min]').closest('.collapsible').find('a.collapsible-header').text() + '\"');
        error = true;
    }
    return min + '-' + max;
};

var assemblyFormData = function(formData){
    var form = {};
    var keys = Object.keys(formData);
        $.each(keys, function (i, key) {
            if (formData[key].includes('Range')) {
                if (getRangeValues(key) !== '-')
                    form[key] = getRangeValues(key);
            }
            else {
                if (getCheckboxValues(key) !== '')
                    form[key] = getCheckboxValues(key);
            }
            if (error)
                return false;
        });
    return form;
};

function checkFilterApply() {
    if (window.location.href.split('?').length > 1 && window.location.href.split('?')[1] !== '') {
        $('.filter-apply').text('Применены фильтры');
    } else
        $('.filter-apply').text('');
}