$( document ).ready(function() {
    /*$("#fogotClick").click(function(){
        $('#login').hide(300);
        $('#fogot').show(300);
    });
    $("#back").click(function(){
        $('#fogot').hide(300);
        $('#login').show(300);
    });
    $("#create").click(function(){
        $('#login').hide(300);
        $('#registr').show(300);
    });
    $("#auth").click(function(){
        $('#registr').hide(300);
        $('#login').show(300);
    });*/
    $('#personal').click(function(){
        if($(this).prop('checked'))
            $('#createusBut').removeAttr('disabled')
        else
            $('#createusBut').attr('disabled', 'disabled')
    });
    $('#change_key').click(function(){
        if($('#key_choice').is(":visible"))
        {
            $('#key_choice').hide(300);
            $('#key_choice').children('input').removeAttr('required');
            $('#key_choice').children('input').val('');
            $('#email_choice').show(300);
            $('#email_choice').children('input').attr('required','true');
            $(this).html('Войти по ключу');

        }
        else
        {
            $('#email_choice').hide(300);
            $('#email_choice').children('input').removeAttr('required');
            $('#email_choice').children('input').val('');
            $('#key_choice').show(300);
            $('#key_choice').children('input').attr('required','true');
            $(this).html('Войти по email');
        }
    });
    $('.errors_container_cross').click(function(){
        $(this).parent().parent().parent().fadeOut(300);
    });
    $('.tarif_icon').hover(function () {
            let id = $(this).attr('data-ind');
            $('.tarif_dop_info_item[data-ind='+id+']').show(300);
            
        }, function () {
            let id = $(this).attr('data-ind');
            $('.tarif_dop_info_item[data-ind='+id+']').hide(300);
        }
    );
    $('.icon_quest').hover(function () {
        let id = $(this).attr('data-ind');
        $('.cell_quest_dopInfo[data-ind='+id+']').fadeIn(300);
        
    }, function () {
        let id = $(this).attr('data-ind');
        $('.cell_quest_dopInfo[data-ind='+id+']').fadeOut(300);
        }
    );
    $(".nav_item").click(function(){
        var id = $(this).attr('data-id');
        $('.nav_item').removeClass('nav_item--active');
        $(this).addClass('nav_item--active');
        $(".section_page").hide();
        $(".section_page[data-id='"+id+"']").show();

    });
    $('#add_key').click(function(){
        $('#delete_key_form').hide(0);
        $('#form_get_key').hide(0);
        $('#code').hide(0);
        $('#key_edit').hide(0);
        $('.dark_errors').fadeIn(300);
        $('#add_key_form').fadeIn(0);
    });
    $('.icon_edit').click(function(){
        $('#delete_key_form').hide(0);
        $('#form_get_key').hide(0);
        $('#code').hide(0);
        $('#add_key_form').hide(0);
        $('.dark_errors').fadeIn(300);
        $('#key_edit').fadeIn(0);

        let num = $(this).parent().parent().find('.cell_item[data-type="num"]').html();
        let name = $(this).parent().parent().find('.cell_item[data-type="name"]').html();
        let tarif = $(this).parent().parent().find('.cell_item_text[data-type="tariff"]').html();
        let date = $(this).parent().parent().find('.cell_item_text[data-type="date"]').html();

        $('.key_info_item[data-type="num"]').html(num);
        $('.key_info_item[data-type="name"]').html(name);
        $('.key_info_item[data-type="tariff"]').html(tarif);
        $('.key_info_item[data-type="date"]').html(date);
        $('.tarif').removeClass('tarif_disabel');
        $('.tarif[data-hide="'+tarif+'"]').addClass('tarif_disabel');
    });
    $("#delete_keys_but").click(function(){
        if(!$(this).hasClass('hidden_for_click'))
        {
            let vals = '';
            $('.cell-active').each(function(){
                vals += $(this).find('.cell_item[data-type="num"]').html()+';';
            });
            $('#delKeys').val(vals);
            $('#form_get_key').hide(0);
            $('#code').hide(0);
            $('#key_edit').hide(0);
            $('.dark_errors').fadeIn(300);
            $('#delete_key_form').fadeIn(0);

        }
    });
    let i=0;
    $('.cell_item_click').click(function(){
        let parent = $(this).parent()
        if(parent.hasClass("cell-active"))
        {
            i--;
            parent.removeClass("cell-active");
        }
        else
        {   
            i++;
            parent.addClass("cell-active");
        }
        if(i>0)
            $('.kyes_butts_button--white').removeClass("hidden_for_click");
        else
            $('.kyes_butts_button--white').addClass("hidden_for_click");
    });
    $('.tarif_butts').click(function(){
        let price = $(this).attr('data-price');
        let col = parseInt($(this).attr('data-col'));
        let dateNow = new Date();
        let day = parseInt(dateNow.getDate());
        let month = parseInt(dateNow.getMonth())+1+col;
        console.log(dateNow.getMonth()+'----'+col);
        if(month>12) 
            month = month-12;

        if(Math.floor(month/10) == 0)
            month = '0'+month
        
        if(Math.floor(day/10) == 0)
            day = '0'+day

        let date = day+'.'+(month)+'.'+dateNow.getFullYear();
        $(this).parent().find('.tarif_info_price').html(price+'<span>₽</span>');
        $(this).parent().find('.tarif_info_date').html(date);

        $(this).parent().find('.tarif_butts').each(function(){
            $(this).removeClass('tarif_butts-selected');
        });
        $(this).addClass('tarif_butts-selected');

    });

    $('#key_add_butt').click(function(){
        let key = $('#key_add_input').val();
        $.ajax({
            url: '/validateKey',
            data: {'key': key, 'type': 1},
            dataType: "text",
            headers: {
                "X-Requested-With": "XMLHttpRequest",
              },
            success: function (response) {
                if(+response)
                {
                    $('#key_errors').hide(0);
                    $('#add_key_form').hide(0);
                    $('#code').fadeIn(300);
                }
                else $('#key_errors').show(0);
            }
        });
    });
    $('#get_key').click(function(){
        let key = $('#key_add_input').val();
        let check = $('#code_add_input').val();
        $.ajax({
            url: '/validateKey',
            data: {'key': key, 'type': 0, 'check': check},
            dataType: "text",
            headers: {
                "X-Requested-With": "XMLHttpRequest",
              },
            success: function (response) {
                if(+response)
                {
                    $('#code').hide(0);
                    $('#form_get_key').find('.sucsess_text').html('Ключ добавлен');
                    $('#form_get_key').fadeIn(300);
                    setTimeout(function(){
                        location.reload()
                    }, 2000);
                }
                else $('#code_errors').show(0);
            }
        });
    });
    $('#not_del').click(function(){
        $('.dark_errors').fadeOut(300);
    });

    $('#del_yes').click(function(){
        let kyes = $('#delKeys').val();
        let keysAr = kyes.split(';');
        let json = JSON.stringify(keysAr);
        console.log(json);
        $.ajax({
            url: '/validateKey',
            data: {'delKeys': kyes, 'type': 2},
            dataType: "text",
            headers: {
                "X-Requested-With": "XMLHttpRequest",
              },
            success: function (response) {
                $('#delete_key_form').fadeOut(300);
                $('#form_get_key').find('.sucsess_text').html('Ключ отвязан от аккаунта');
                $('#form_get_key').fadeIn(300);
                console.log(response)
                setTimeout(function(){
                    location.reload()
                }, 2000);
            }
        });
    });
    $('.cross_input').click(function(){
        $(this).parent().find('input').val('');
    });
    $(".eye_input").click(function(){
        let type =  $(this).parent().find("input").attr('type')
        if (type == 'password')
        {
            $(this).parent().find("input").attr('type', "text");
            $(this).addClass('eye_input--close');

        }
        else
        {
            $(this).parent().find("input").attr('type', "password");
            $(this).removeClass('eye_input--close');
        }
    });
    $('.tableCell[data-type="summ_js"]').each(function(){
        let summ_js = parseInt($(this).html());
        $(this).html(summ_js.toLocaleString('ru-RU', { style: 'currency', currency: 'RUB', maximumFractionDigits: 0}));
    });
    $("#file_help").change(function(){
        console.log(this.files);
        if(this.files.length > 0)
        {
            let filesStr = '';
            for (var i = 0; i < this.files.length; i++)
                filesStr += this.files[i].name+"; ";
            $('.errors_file').html(filesStr)
        }
    });
    $('.inputTableOgrn').keyup(function() { 
        let ognr = '';
        $('.inputTableOgrn').each(function(){
            ognr += $(this).val();
        });
        $('#ogrn').val(ognr);

        let thisNum = $(this).attr('data-change');
        if (thisNum < 13 && $(this).val()!='')
        {
            thisNum++;
            $('.inputTableOgrn[data-change="'+thisNum+'"]').focus();
        }
    });
    $('.agreementConditionsInput').click(function(){
        if($('#docs').prop('checked') && $('#docsTwo').prop('checked'))
            $('#butt_add_req').removeAttr('disabled');
        else
            $('#butt_add_req').attr('disabled', 'disabled');
    });

    if($('#phone').length > 0)
    {
        let numbers = $('#phone').children().html();
        let re = /(?:([\d]{1,}?))??(?:([\d]{1,3}?))??(?:([\d]{1,3}?))??(?:([\d]{2}))??([\d]{2})$/;
        let formatted = numbers.replace( re, function( all, a, b, c, d, e ){
            return ( a ? a + " " : "" ) + ( b ? b + " " : "" ) + ( c ? c + "-" : "" ) + ( d ? d + "-" : "" ) + e;
        });
        console.log(numbers);
        $('#phone').html(formatted);
    }
});