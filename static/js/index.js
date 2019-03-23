let useOT = $('#nav-pf').offset().top;
let mainNav = $('#main-nav').offset().top;
// console.log(useOT);
// console.log(docST);
$(window).scroll(() => {
    if ($(document).scrollTop() > useOT) {
        $('#nav-pf').css('position', 'fixed')
    } else {
        $('#nav-pf').css('position', 'static')
    }
    // if ($(document).scrollTop() > mainNav) {
    //     $('#main-nav').css('position', 'fixed')
    //     $('#userLogin').css('position', 'fixed')
    // } else {
    //     $('#main-nav').css('position', 'static')
    //     $('#userLogin').css('position', 'static')
    // }
})
