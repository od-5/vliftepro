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
