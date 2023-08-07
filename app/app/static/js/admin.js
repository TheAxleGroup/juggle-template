$(function () {
    /**************************************************************************************************/
    // Page title container selector
    var header_div = $('div.left.col9.header-title');
    /**************************************************************************************************/


    /**************************************************************************************************/
    // Add 'Show in Explorer View' button to edit pages
    var explorer_button = document.createElement('a');
    explorer_button.innerHTML = 'Show in Explorer';
    explorer_button.href = window.location.href.replace('/edit/', '/');
    explorer_button.classList.add('button', 'button-small', 'icon', 'icon-folder-open-inverse');
    header_div.append(explorer_button);
    /**************************************************************************************************/


    /**************************************************************************************************/
    // Toggler for LinkBlock type selector
    function linkBlockToggler(elem){
        var value = $(elem).find('input:checked').val();
        var container = $(elem).closest('.link-block');
        var show_list = [];
        var hide_list = [];
        switch (value) {

            case(''):
                show_list = [];
                hide_list = ['url', 'document', 'email', 'phone', 'anchor', 'link_text', 'page', 'link_format', 'link_opens_in_new_tab'];
            break;

            case('link_text'):
                hide_list = ['page', 'document', 'email', 'phone', 'anchor', 'link_format', 'link_opens_in_new_tab', 'url'];
                show_list = ['link_text'];
            break;

            case('url'):
                hide_list = ['page', 'document', 'email', 'phone', 'anchor', 'link_format',];
                show_list = ['url', 'link_text', 'link_opens_in_new_tab'];
            break;

            case('page'):
                hide_list = ['url', 'document', 'email', 'phone', 'anchor', 'link_format',];
                show_list = ['page', 'link_text', 'link_opens_in_new_tab'
                ];
            break;

            case('document'):
                hide_list = ['page', 'url', 'email', 'phone', 'anchor', 'link_format',];
                show_list = ['document', 'link_text', 'link_opens_in_new_tab'];
            break;

            case('phone'):
                hide_list = ['page', 'document', 'email', 'url', 'anchor', 'link_format',];
                show_list = ['phone', 'link_text', 'link_opens_in_new_tab'];
            break;

            case('email'):
                hide_list = ['page', 'document', 'url', 'phone', 'anchor', 'link_format',];
                show_list = ['email', 'link_text', 'link_opens_in_new_tab'];
            break;

            case('anchor'):
                hide_list = ['page', 'document', 'email', 'phone', 'url', 'link_format',];
                show_list = ['anchor', 'link_text', 'link_opens_in_new_tab'];
            break;

        }

        $.each(show_list, function (index, item) {
            container.find('.fieldname-'+ item).parent().closest('.field').show().addClass('required');
        }.bind(this));

        $.each(hide_list, function(index, item) {
            container.find('.fieldname-'+ item).parent().closest('.field').hide().removeClass('required');
        }.bind(this));

    }

    function indexToggler(elem){
        var value = $(elem).find('input:checked').val();
        var container = $(elem).closest('.block');

        if(value){
            container.find('.fieldname-index_title').parent().closest('.field').show().addClass('required');
        }
        else{
            container.find('.fieldname-index_title').parent().closest('.field').hide().removeClass('required');
        }

    }

    // linkBlockToggler call on load
    $('.link-block .fieldname-link_type').each(function() {
       linkBlockToggler(this);
    });
    // linkBlockToggler call on change
    $('body').on('change', '.link-block .fieldname-link_type', function() {
       linkBlockToggler($(this));
    });


    $('.block .fieldname-has_index').each(function() {
       indexToggler(this);
    });
    // linkBlockToggler call on change
    $('body').on('change', '.block .fieldname-has_index', function() {
       indexToggler(this);
    });

    /**************************************************************************************************/
    // General function called from observer
    var observer = new MutationObserver(function(mutations) {
        // linkBlockToggler call on observed mutation
        $('.link-block .fieldname-link_type').each(function() {
           linkBlockToggler(this);
        });
        $('.block .fieldname-has_index').each(function() {
           indexToggler(this);
        });

    });

    // General listener for added/removed nodes on body
    observer.observe(document.body, {
        childList: true,
        subtree: true,
    });
    /**************************************************************************************************/

});