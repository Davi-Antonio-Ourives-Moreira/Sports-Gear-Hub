from repository import Banco_Dados_Carrinho
import flask

class Carrinho(object):
    def __init__(self, nome_produto, preco_produto, imagem_produto, id_produto) -> None:
        self.nome_produto = nome_produto
        self.preco_produto = preco_produto
        self.imagem_produto = imagem_produto
        self.id_produto = id_produto

        self.banco_dados_carrinho = Banco_Dados_Carrinho()
    
    def Adicionar_Produto_Carrinho(self):
        self.verificar_produto_repetido = self.banco_dados_carrinho.Verificar_Produto_Repetido(imagem_identificadora_produto=self.imagem_produto)

        if self.verificar_produto_repetido ==  []:
            self.banco_dados_carrinho.Adicionar_Produto_Carrinho(nome_produto=self.nome_produto,
                                                                 preco_produto=self.preco_produto,
                                                                 imagem_produto=self.imagem_produto,
                                                                 id_produto=self.id_produto)
            
            return flask.redirect(flask.request.referrer)
        
        flask.flash("produto_existente_carrinho")
        
        return flask.redirect(flask.request.referrer)

    def Remover_Produto_Carrinho(self):
        self.banco_dados_carrinho.Remover_Produto_Carrinho(imagem_identificadora_produto=self.imagem_produto)

        flask.flash("deixar_carrinho_aberto")

        return flask.redirect(flask.request.referrer)