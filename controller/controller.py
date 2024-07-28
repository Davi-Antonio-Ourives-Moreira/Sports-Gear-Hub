import flask
import requests
from repository import Banco_Dados_Carrinho
from services import Pesquisas, Carrinho, Pagamento

app = flask.Flask(__name__)
app.secret_key = "GeeksForGeeks"

@app.get("/")
def pagina_inicial():
    banco_dados_carrinho = Banco_Dados_Carrinho()

    verificar_produtos_carrinho = banco_dados_carrinho.Dados_Produtos_Carrinho()

    verificar_quantidade_produtos_carrinho = len(verificar_produtos_carrinho)

    informacoes_produtos_destaque = []

    produtos_carrinho = []

    preco_total_produtos_carrinho = 0
    
    produtos = [("Bola", 131, "Bola_Basquete_2.webp", "Basquete")] #requests.get("http://127.0.0.1:5000/dados_produtos_destaque")

    #produtos = produtos.json()

    for produto in produtos:
        informacoes_produtos_destaque.append((produto[0], produto[1], produto[2], produto[3]))
    
    if verificar_quantidade_produtos_carrinho > 0:
        for produto_carrinho in verificar_produtos_carrinho:
            produtos_carrinho.append((produto_carrinho[0], produto_carrinho[1], produto_carrinho[2], produto_carrinho[3]))

            preco_total_produtos_carrinho += float(produto_carrinho[1])

    return flask.render_template("index.html", 
                                 todos_produtos_destaque=informacoes_produtos_destaque,
                                 quantidade_produtos_carrinho=verificar_quantidade_produtos_carrinho,
                                 todos_produtos_carrinho=produtos_carrinho,
                                 preco_total_produtos_carrinho=round(preco_total_produtos_carrinho, 2))

@app.get("/adicionar-produtos-carrinho/<nome_p>/<preco_p>/<imagem_p>/<id_p>")
def adicionar_produto_carrinho(nome_p, preco_p, imagem_p, id_p):
    carrinho = Carrinho(nome_produto=nome_p,
                        preco_produto=preco_p,
                        imagem_produto=imagem_p,
                        id_produto=id_p)
    
    return carrinho.Adicionar_Produto_Carrinho()

@app.get("/remover-produtos-carrinho/<nome_p>/<preco_p>/<imagem_p>/<id_p>")
def remover_produto_carrinho(nome_p, preco_p, imagem_p, id_p):
    carrinho = Carrinho(nome_produto=nome_p,
                        preco_produto=preco_p,
                        imagem_produto=imagem_p,
                        id_produto=id_p)
    
    return carrinho.Remover_Produto_Carrinho()

@app.get("/categoria/<categoria>")
def categorias(categoria):
    banco_dados_carrinho = Banco_Dados_Carrinho()

    verificar_produtos_carrinho = banco_dados_carrinho.Dados_Produtos_Carrinho()

    verificar_quantidade_produtos_carrinho = len(verificar_produtos_carrinho)

    produtos_carrinho = []

    preco_total_produtos_carrinho = 0

    produtos_filtrados = requests.get(f"http://127.0.0.1:5000/categoria_produtos/{categoria}")

    produtos_filtrados = produtos_filtrados.json()

    informacoes_produtos_filtrados = []

    for produto_filtrado in produtos_filtrados:
        informacoes_produtos_filtrados.append((produto_filtrado[0], produto_filtrado[1], produto_filtrado[2], produto_filtrado[3]))

    if verificar_quantidade_produtos_carrinho > 0:
        for produto_carrinho in verificar_produtos_carrinho:
            produtos_carrinho.append((produto_carrinho[0], produto_carrinho[1], produto_carrinho[2], produto_carrinho[3]))

            preco_total_produtos_carrinho += float(produto_carrinho[1])

    return flask.render_template("categoria.html",
                                 produtos_filtrados=informacoes_produtos_filtrados,
                                 categoria=categoria,
                                 quantidade_produtos_carrinho=verificar_quantidade_produtos_carrinho,
                                 todos_produtos_carrinho=produtos_carrinho,
                                 preco_total_produtos_carrinho=round(preco_total_produtos_carrinho, 2))

@app.post("/pesquisar")
def pesquisar_produto():
    input_pesquisa = flask.request.form["pesquisa"]

    if input_pesquisa == "":
        return flask.redirect("/")

    return flask.redirect(f"/pesquisa/{input_pesquisa}")

@app.get("/pesquisa/<produto_pesquisado>")
def pesquisa(produto_pesquisado):
    pesquisa = Pesquisas(nome_produto=produto_pesquisado)

    return pesquisa.Produto_Pesquisado()

@app.post("/pagamento")
def pagamento():
    banco_carrinho = Banco_Dados_Carrinho()

    produtos = []

    preco_produtos = []

    produtos_carrinho = banco_carrinho.Dados_Produtos_Carrinho()

    for p in produtos_carrinho:
        produtos.append(p[0])
        preco_produtos.append(float(p[1]))

    pagamento = Pagamento(", ".join(produtos), sum(preco_produtos))

    return pagamento.Pagar()

@app.get("/pagamento-efetuado-sucesso")
def pagamento_efetuado_sucesso():
    banco_carrinho = Banco_Dados_Carrinho()

    banco_carrinho.Resetar_Carrinho()

    flask.flash("pagamento_feito_sucesso")

    return flask.render_template("aviso_pagamento.html")

@app.get("/pagamento-cancelado")
def pagamento_cancelado():
    flask.flash("pagamento_cancelado")

    return flask.render_template("aviso_pagamento.html")


