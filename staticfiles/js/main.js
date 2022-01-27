window.addEventListener("load", function(event) {
	$("#mainSlide").owlCarousel({
		items:1,
		loop:true,
		margin:0,
		nav: false,
		dots: true,
		autoplay: true,
		autoplayHoverPause:true,
		autoplayTimeout: 10000,
	});
	$("#gallerySlide").owlCarousel({
		items:5,
		loop:true,
		margin:5,
		nav:true,
		dots:false,
		responsiveClass:true,
		responsive:{
			1340:{
				items:5
			},
			1125:{
				items:4
			},
			925:{
				items:3
			},
			720:{
				items:2
			},
			0:{
				items:1
			}

		}
	});
	$(".items_slider").owlCarousel({
		items:1,
		loop:false,
		margin:1,
		nav:true,
		dots:false
	});
	let move;
	$('.gallery_img, .items_slider__img').mousedown(function(){
		move = 1;
	    $(this).mousemove(function(){
			move = 0
		})
	});
	$('.gallery_img, .items_slider__img').mouseup(function(){
		if(move)
		{
		    if(($(this).hasClass('gallery_img') && innerWidth<720) || innerWidth<530) return 0;

			let img = $(this).attr('data-main');
			let alt = $(this).attr('alt');
			$('.photo_big').html(' <img class="photo_big__img" src="/media/'+img+'" alt="'+alt+'">');
			$('.photo_big').fadeIn(300);
			$('body').css('overflow', 'hidden');

		}
	});
	$('.photo_big').click(function(){
	    $('.photo_big').fadeOut(300);
		$('body').css("overflow",'auto');
	});
});
