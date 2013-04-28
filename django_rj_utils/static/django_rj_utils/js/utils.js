function highdpi_init() {
  if(jQuery('.retina').css('font-size') == '1px') {
    var els = jQuery('img.retina').get();
    for (var i = 0; i < els.length; i++) {
      var src = els[i].src;
      src = src.replace('.png', '@2x.png');
      els[i].src = src;
    }
  }
}

$('a, button, input[type="button, submit"]').bind('touchstart', function() {
  $(this).addClass('touch');
});
$('a, button, input[type="button, submit"]').bind('touchend', function() {
  $(this).removeClass('touch');
});

jQuery(document).ready(function() {
  highdpi_init();
});
