const menuBtn = document.querySelector('.menu-btn');
let menuopen = false;

menuBtn.addEventListener('click', () => {
    if(!menuopen){
        menuBtn.classList.add('open')
        menuopen = true;
    }
    else {
        menuBtn.classList.remove('open')
        menuopen = false;
    }
})


/* slider */

