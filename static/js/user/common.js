$(function(){

  $('.city_list button').click(function(){
    $('.city_list ul').slideToggle();
  });

  $.validator.messages.required = "* Заполните поле! *";
  $('.frm-wrp1 form').validate({
    rules: {
      name: { required: true },
      phone: { required: true },
    },
    submitHandler: function() {
      $('.frm-wrp1 form').ajaxSubmit(function(data){
        if(data.success){
          console.log(data.success);
        } else {
          console.log(data.error);
        }
      });
    }
  });

  $('.form2-wrap form').validate({
    rules: {
      name: { required: true },
      phone: { required: true },
    },
    submitHandler: function() {
      $('.form2-wrap form').ajaxSubmit(function(data){
        if(data.success){
          console.log(data.success);
        } else {
          console.log(data.error);
        }
      });
    }
  });

  $('.form3-wrap form').validate({
    rules: {
      name: { required: true },
      phone: { required: true },
    },
    submitHandler: function() {
      $('.form3-wrap form').ajaxSubmit(function(data){
        if(data.success){
          console.log(data.success);
        } else {
          console.log(data.error);
        }
      });
    }
  });

  // валидация форм
    $.validator.messages.required = "* Заполните поле! *";
    $(".content-10 form input.nm, .content-10 form input.tele").addClass("required");
    $(".content-10 form").validate();
    // запускаем formset
    $('.content-10 tr.lines').formset({
        prefix: '{{ calc_formset.prefix }}',
        addText: 'Добавить город',
        deleteText: 'Удалить'
    });
    $('a.add-row').click(function(){
        $('a.delete-row').show();
    });
    $('.col-2 input, .col-4 input, .col-5 input, .tbl-sum input[type=text]').attr('readonly', true);

    var id;
    var lift_id;
    var price_id;
    var sum_id;
    var total_sum;
    var id_constructor = function(i){
        id = i.attr('id').split('-');
        lift_id = id;
        price_id = id;
        sum_id = id;
        lift_id[lift_id.length-1] = 'lift';
        lift_id = '#' + lift_id.join('-');
        price_id[price_id.length-1] = 'price';
        price_id = '#' + price_id.join('-');
        sum_id[sum_id.length-1] = 'sum';
        sum_id = '#' + sum_id.join('-');
    };
    var apply_change = function(i){
        if(i.val() != ''){
            $(sum_id).val($(lift_id).val() * $(price_id).val());
        } else {
            $(sum_id).val('');
        }
    }
    var total_sum_change = function(){
        total_sum = 0;
        $('.col-5 input').each(function(){
            if($(this).val() != ''){
                total_sum = total_sum + parseInt($(this).val());
            }
        });
        if (total_sum == 0) {
            total_sum = '';
        }
        $('.tbl-sum-col2').val(total_sum);
    }
    $('a.delete-row').click(function(){
        total_sum_change();
    });
    // ajax city change
    $('.col-1 select').change(function(){
        id_constructor($(this));
        if($(this).val() == ''){
            $(id).val('');
          console.log('empty');
        } else {
          console.log($(this).val());
            $.get("/city", {
                    name: $(this).val()
                },
                function(e){
                    var data = e;
                    console.log(data.lift);
                    $(lift_id).val(data.lift);
                    apply_change($(price_id));
                    total_sum_change();
                }
            );
        }
    });
    // ajax format change
    $('.col-3 select').change(function(){
        id_constructor($(this));
        if($(this).val() == '---------'){
            $(id).val('');
        } else {
            $.get("/format", {
                    name: $(this).val()
                },
                function(e){
                    $(price_id).val(e.price);
                    apply_change($(lift_id));
                    total_sum_change();
                }
            );
        }
    });


    // Затемнение фона
    $('.tbl-sum button').click(function(){
        $('#retain_form').fadeIn();
        var docHeight = $(document).height();
        $("body").append("<div id='overlay'></div>");
        $("#overlay")
           .height(docHeight)
           .css({
              'opacity' : 0.4,
              'position': 'fixed',
              'top': 0,
              'left': 0,
              'background-color': 'black',
              'width': '100%',
              'z-index': 9
           });
    });

    // Закрытие модального окна
    $(document).mouseup(function (e) {
        var container = $("#retain_form");
        if (container.has(e.target).length === 0){
        container.hide();
        $('#overlay').remove();
        }
    });

  $('.city-slider').bxSlider({
    minSlides: 1,
    maxSlides: 1,
    slideWidth: 900,
    moveSlides: 1,
    pager: false,
    auto: true,
    mode: 'fade',
    pause: 5000
  });

  $('.slider-1').bxSlider({
    minSlides: 3,
    maxSlides: 3,
    slideWidth: 230,
    moveSlides: 1,
    pager: false,
    auto: true,
    pause: 5000,
    slideMargin: 20
  });

  $('.slider-2').bxSlider({
    minSlides: 1,
    maxSlides: 1,
    slideWidth: 775,
    moveSlides: 1,
    pager: false,
    auto: true,
    mode: 'fade',
    pause: 5000
  });
});
