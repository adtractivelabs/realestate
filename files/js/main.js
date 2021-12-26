$(document).ready(function(){
	$('.slick-banner').slick({
  dots: false,
  infinite: true,
  autoplay: true,
  speed: 300,
  slidesToShow: 4,
  slidesToScroll: 4,
  responsive: [
    {
      breakpoint: 1024,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 3,
        infinite: true,
        dots: true
      }
    },
    {
      breakpoint: 800,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2
      }
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1
      }
    }
  ]
});

$('.testmonial-slide').slick({

  slidesToShow: 1,
  slidesToScroll: 1,
  autoplay: true,
  autoplaySpeed: 2000,
  dots: false
 
});


if($(window).width() < 991){
	$(".menu").click(function(){
    $('.nav-right').addClass('active');
    $('.overlay').addClass('active');
	});
   $(".close-menu").click(function(){
    $('.nav-right').removeClass('active');
    $('.overlay').removeClass('active');
   })
}


$(".overview-tab > ul > li > a").click(function(){
 $(".overview-tab > ul > li > a").removeClass('active');
 $(this).addClass('active');
 var x = $(this).attr('data-tab');
 $(".overvie-sub").removeClass('active');
 $('#'+x).addClass('active');

});

$(".about-tab-sec-main > ul > li > a").click(function(){
 $(".about-tab-sec-main > ul > li > a").removeClass('active');
 $(this).addClass('active');
 var x = $(this).attr('data-id');
 $(".about-tab-content").removeClass('active');
 $('#'+x).addClass('active');

});

$(function () {
    $(".a8").slice(0, 6).addClass('display');
    $(".load-more-btn > a").on('click', function (e) {
        e.preventDefault();
        $(".a8:hidden").slice(0, 6).addClass('display');
        if ($(".a8:hidden").length == 0) {
           $(".load-more-btn > a").remove();
        } else {
            $('html,body').animate({
                scrollTop: $(this).offset().top
            }, 1500);
        }
    });
});

        AOS.init({duration: 1200,});

        $('html').addClass('scroll-remove');
		
});