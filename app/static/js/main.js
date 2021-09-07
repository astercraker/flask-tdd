const myNav = document.querySelector("#main_navbar")
const burger = document.querySelector("#burger")
burger.addEventListener('click', ()=> {
    myNav.classList.toggle("is-active")
    burger.classList.toggle("is-active")
})