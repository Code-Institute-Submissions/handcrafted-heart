$(document).ready(function () {
    
    /* Initializes the carousel and cycles through the items from lesft to right */
    
    $('.carousel').carousel({
        interval: 5000,
        touch: true
    });
    
    $('.carousel').carousel('cycle');
    
})