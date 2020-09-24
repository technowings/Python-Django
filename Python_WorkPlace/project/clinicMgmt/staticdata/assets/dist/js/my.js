
$(document).ready(function(){
   $("#testimonial-slider").owlCarousel({
       items:1,
       itemsDesktop:[1000,1],
       itemsDesktopSmall:[979,1],
       itemsTablet:[768,1],
       pagination:true,
       navigation:false,
       navigationText:["",""],
       slideSpeed:1000,
       singleItem:true,
       autoPlay:true
   });
});





$(document).ready(function(){
    $('.counter-value').each(function(){
        $(this).prop('Counter',0).animate({
            Counter: $(this).text()
        },{
            duration: 3500,
            easing: 'swing',
            step: function (now){
                $(this).text(Math.ceil(now));
            }
        });
    });
});



$('#myCarousel').carousel({
   interval: 3000,
})


window.onload = function() {
   // document.getElementById('input_field').value = '';
   document.getElementById('myform').reset();
   }
