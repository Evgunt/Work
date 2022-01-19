$(document).ready(function() {
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
		autoWidth: 250
		
	});
	$(".content_slider").owlCarousel({
		items:5,
		loop:true,
		margin:5,
		nav:true,
		dots:false,
		autoWidth: 200
		
	});
	$(".items_slider").owlCarousel({
		items:1,
		loop:true,
		margin:0,
		nav:true,
		dots:false,
		autoWidth: 140
		
	});

	$(document).mouseup(function (e) {
		var container = $(".products_items_click");
		if (container.has(e.target).length === 0){
			container.hide();
		}
	});

	$('.products_title').on('click', function(){
		$('.products_items_click').show(0);
		
	});
	$('.cross').click(function(){
		$('.products_items_click').hide(0);
	})
});	