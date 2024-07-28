function Abrir_Menu(){
    menu_bg = document.querySelector(".menu_aberto_bg");

    menu = document.querySelector(".menu_aberto");

    menu_bg.style.display = "flex";

    menu.style.display = "block";
}

function Fechar_Menu(){
    menu_bg = document.querySelector(".menu_aberto_bg");

    menu = document.querySelector(".menu_aberto");

    menu_bg.style.display = "none";

    menu.style.display = "none";
}
