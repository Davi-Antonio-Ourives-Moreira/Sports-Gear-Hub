function Abrir_Carrinho(){
    bg_carrinho = document.querySelector(".carrinho_aberto_bg");

    carrinho = document.querySelector(".carrinho_aberto");

    bg_carrinho.style.display = "flex";

    carrinho.style.display = "block";
}

window.addEventListener('click', function(event) {
    if (event.target == document.getElementById('modal_bg')) {
        document.getElementById('modal_bg').style.display = 'none';
        document.getElementById('modal').style.display = 'none';
    }
});