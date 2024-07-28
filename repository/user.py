import psycopg2 as ps

class Banco_Dados_Carrinho(object):
    def __init__(self) -> None:
        self.user = "denfsjjv"
        self.password = "0sklxGgyKSz0kDe_l9H9OV2UDUmcRgT1"
        self.port = 5432
        self.host = "mahmud.db.elephantsql.com"
        self.dbname = "denfsjjv"

        self.conn = ps.connect(user=self.user,
                               password=self.password,
                               host=self.host,
                               port=self.port,
                               dbname=self.dbname)
        
        self.cursor = self.conn.cursor()

        self.conn.autocommit = True

        self.tabela_produtos = self.cursor.execute("CREATE TABLE IF NOT EXISTS carrinho (nome_produto text, preco_produto float, imagem_produto text, id_produto text) ")


    def Adicionar_Produto_Carrinho(self, nome_produto, preco_produto, imagem_produto, id_produto):
        self.cursor.execute("INSERT INTO carrinho(nome_produto, preco_produto, imagem_produto, id_produto) VALUES(%s,%s,%s,%s)", (nome_produto, preco_produto, imagem_produto, id_produto))

    def Remover_Produto_Carrinho(self, imagem_identificadora_produto):
        self.cursor.execute("DELETE FROM carrinho WHERE imagem_produto=%s ", (imagem_identificadora_produto, ))

    def Verificar_Produto_Repetido(self, imagem_identificadora_produto):
        self.cursor.execute("SELECT * FROM carrinho WHERE imagem_produto=%s", (imagem_identificadora_produto, ))

        self.verificar_produto_repetido  = list(self.cursor.fetchall())

        return self.verificar_produto_repetido

    def Dados_Produtos_Carrinho(self):
        self.cursor.execute("SELECT * FROM carrinho")

        self.dados_produtos_carrinho = list(self.cursor.fetchall())

        return self.dados_produtos_carrinho

    def Resetar_Carrinho(self):
        self.cursor.execute("DELETE FROM carrinho")
