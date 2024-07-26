import requests
import flask
from repository import Banco_Dados_Carrinho

class Pesquisas(object):
    def __init__(self, nome_produto) -> None:
        self.banco_dados_carrinho = Banco_Dados_Carrinho()

        self.verificar_quantidade_produtos_carrinho = self.banco_dados_carrinho.Dados_Produtos_Carrinho()

        self.verificar_quantidade_produtos_carrinho = len(self.verificar_quantidade_produtos_carrinho)

        self.nome_produto = nome_produto

        self.pesquisa = requests.get(f"http://127.0.0.1:5000/pesquisa_produtos/{self.nome_produto}")

        self.pesquisa = self.pesquisa.json()

        self.informacoes_produtos_pesquisados = []
    
    def Produto_Pesquisado(self):
        for produto_pesquisado in self.pesquisa:
            self.informacoes_produtos_pesquisados.append((produto_pesquisado[0], produto_pesquisado[1], produto_pesquisado[2], produto_pesquisado[3]))

        return flask.render_template("pesquisas.html",
                                     produto_pesquisados=self.informacoes_produtos_pesquisados,
                                     quantidade_produtos_carrinho=self.verificar_quantidade_produtos_carrinho,
                                     nome_pesquisa=self.nome_produto)