import flask
import requests

from repository import Banco_Dados_Carrinho

app = flask.Flask(__name__)

@app.get("/")
def pagina_inicial():
    banco_dados_carrinho = Banco_Dados_Carrinho()

    verificar_quantidade_produtos_carrinho = banco_dados_carrinho.Dados_Produtos_Carrinho()

    verificar_quantidade_produtos_carrinho = len(verificar_quantidade_produtos_carrinho)

    informacoes_produtos_destaque = []
    
    produtos = requests.get("http://127.0.0.1:5000/dados_produtos_destaque")

    produtos = produtos.json()

    for produto in produtos:
        informacoes_produtos_destaque.append((produto[0], produto[1], produto[2], produto[3]))

    

    return flask.render_template("index.html", 
                                 todos_produtos_destaque=informacoes_produtos_destaque,
                                 quantidade_produtos_carrinho=verificar_quantidade_produtos_carrinho)

@app.get("/adicionar-produtos-carrinho/<nome_p>/<preco_p>/<imagem_p>/<id_p>")
def adicionar_produto_carrinho(nome_p, preco_p, imagem_p, id_p):
    return nome_p

@app.get("/categoria/<categoria>")
def categorias(categoria):
    banco_dados_carrinho = Banco_Dados_Carrinho()

    verificar_quantidade_produtos_carrinho = banco_dados_carrinho.Dados_Produtos_Carrinho()

    verificar_quantidade_produtos_carrinho = len(verificar_quantidade_produtos_carrinho)

    produtos_filtrados = requests.get(f"http://127.0.0.1:5000/categoria_produtos/{categoria}")

    produtos_filtrados = produtos_filtrados.json()

    informacoes_produtos_filtrados = []

    for produto_filtrado in produtos_filtrados:
        informacoes_produtos_filtrados.append((produto_filtrado[0], produto_filtrado[1], produto_filtrado[2], produto_filtrado[3]))

    return flask.render_template("categoria.html",
                                 produtos_filtrados=informacoes_produtos_filtrados,
                                 categoria=categoria,
                                 quantidade_produtos_carrinho=verificar_quantidade_produtos_carrinho)


