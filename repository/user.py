import psycopg2 as ps

class Banco_Dados_Carrinho(object):
    def __init__(self) -> None:
        self.dbname = "Sports-Gear-Hub"
        self.host = "localhost"
        self.port = "5432"
        self.user = "postgres"
        self.password = "postgres"

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
        pass

    def Dados_Produtos_Carrinho(self):
        self.cursor.execute("SELECT * FROM carrinho")

        self.dados_produtos_carrinho = list(self.cursor.fetchall())

        return self.dados_produtos_carrinho