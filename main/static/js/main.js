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
		dots:false,
		autoWidth: 140
	});
});	