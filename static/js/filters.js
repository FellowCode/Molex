$(document).ready(function () {
    $('#openFilters').click(function () {
        $('#sidenav-category').css('display','none');
        $('#sidenav-filter').css('display', 'block');
    });
    $('#closeFilters').click(function () {
        $('#sidenav-filter').css('display', 'none');
        $('#sidenav-category').css('display','block');
    });



    FilterInitialize();

    $(window).on('popstate', function() {
        loadPage(window.location.href);
    });
});

var FilterInitialize = function () {
    var properties = $('#filterProperties').text().split(';');
    var fullSlug = $('#fullCategory').text();
    var filterData = {};
    $.each(properties, function (i, elem) {
        var vals = elem.split(':');
        filterData[vals[0]] = vals[1];
    });
    $('a#Filter').click(function () {
        var form = assemblyFormData(filterData);
        filterProducts(form);
    });
    $('#resetFilter').click(function () {
        var url = window.location.href.split('?')[0];
        $('#list-container').load(url + ' #list');
        history.pushState(null, $(document).title, url);
        if (window.location.href.split('?').length > 1) {
            $('.filter-apply').text('Применены фильтры');
        } else
            $('.filter-apply').text('');
    });
    var filterProducts = function(form) {
        let urlParameters = Object.entries(form).map(e => e.join('=')).join('&');
        let url = '/products/' + fullSlug + '/?' + urlParameters;
        $('#list-container').load(url + ' #list');
        history.pushState(null, $(document).title, url);
        if (window.location.href.split('?').length > 1) {
            $('.filter-apply').text('Применены фильтры');
        } else
            $('.filter-apply').text('');
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
    return $(elem+'_min]').val() + '-' + $(elem+'_max]').val();
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
        });
    return form;
};