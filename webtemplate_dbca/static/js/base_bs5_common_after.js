var chevron_toggle = {
	init: function() { 
               $('.chevron-toggle').each(function(i, obj) {
                       var collapsed_id = $(this).data('bs-target');
                       var collapsed_status = $(collapsed_id).css('display');  
                       if (collapsed_status == 'none') {
                             $(this).removeClass("down-chevron-open");
                             $(this).addClass("down-chevron-close");
               
                       } else {
                             $(this).removeClass("down-chevron-close");
                             $(this).addClass("down-chevron-open");
               
                       }
               });
               
               
               $('.chevron-toggle').click(function(e) {
                      var collapsed_id = $(this).data('bs-target');
                      if ($(this).hasClass("down-chevron-close")) {
                           $(this).removeClass("down-chevron-close");
                           $(this).addClass("down-chevron-open");
                           $(collapsed_id).slideDown(500);
               
                       } else {
               
                             $(this).removeClass("down-chevron-open");
                             $(this).addClass("down-chevron-close");
                             $(collapsed_id).slideUp(500);
                       }
               })
        }

}
chevron_toggle.init();
