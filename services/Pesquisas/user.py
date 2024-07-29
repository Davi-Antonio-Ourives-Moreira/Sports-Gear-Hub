import requests
import flask
from repository import Banco_Dados_Carrinho

class Pesquisas(object):
    def __init__(self, nome_produto) -> None:
        self.banco_dados_carrinho = Banco_Dados_Carrinho()

        self.verificar_produtos_carrinho = self.banco_dados_carrinho.Dados_Produtos_Carrinho()

        self.verificar_quantidade_produtos_carrinho = len(self.verificar_produtos_carrinho)

        self.produtos_carrinho = []

        self.preco_total_produtos_carrinho = 0

        self.nome_produto = nome_produto

        self.pesquisa = requests.get(f"https://sports-gear-hub-api.onrender.com/pesquisa_produtos/{self.nome_produto}")

        self.pesquisa = self.pesquisa.json()

        self.informacoes_produtos_pesquisados = []
    
    def Produto_Pesquisado(self):
        for produto_pesquisado in self.pesquisa:
            self.informacoes_produtos_pesquisados.append((produto_pesquisado[0], produto_pesquisado[1], produto_pesquisado[2], produto_pesquisado[3]))

        if self.verificar_quantidade_produtos_carrinho > 0:
            for produto_carrinho in self.verificar_produtos_carrinho:
                self.produtos_carrinho.append((produto_carrinho[0], produto_carrinho[1], produto_carrinho[2], produto_carrinho[3]))

                self.preco_total_produtos_carrinho += float(produto_carrinho[1])

        return flask.render_template("pesquisas.html",
                                     produto_pesquisados=self.informacoes_produtos_pesquisados,
                                     quantidade_produtos_carrinho=self.verificar_quantidade_produtos_carrinho,
                                     nome_pesquisa=self.nome_produto,
                                    todos_produtos_carrinho=self.produtos_carrinho,
                                    preco_total_produtos_carrinho=round(self.preco_total_produtos_carrinho, 2))