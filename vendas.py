import sqlalchemy as sa

engine = sa.create_engine('sqlite:///C:/temp/PANDA/PUC/BANCO_DE_DADOS_RELACIONAL/aula02/vendas.db')

import sqlalchemy.orm as orm

base = orm.declarative_base()

#tb cliente 
class cliente(base):
    __tablename__ = "tbCliente"
    
    cpf = sa.Column(sa.CHAR(14), nullable = False, primary_key = True, index = True)
    nome = sa.Column(sa.VARCHAR(100), nullable = False)
    email = sa.Column(sa.VARCHAR(50), nullable = False)
    faixa_salarial = sa.Column(sa.DECIMAL(10,2))
    dia_mes_aniversario = sa.Column(sa.CHAR(5))
    bairro = sa.Column(sa.VARCHAR(50))
    cidade = sa.Column(sa.VARCHAR(50))
    uf = sa.Column(sa.CHAR(2))

#tb fornecedor
class fornecedor(base):
    __tablename__ = "tbFornecedor"
    
    registro_fornecedor = sa.Column(sa.INTEGER, nullable = False, primary_key = True, index = True)
    nome_fantasia = sa.Column(sa.VARCHAR(100), nullable = False)
    razao_social = sa.Column(sa.VARCHAR(100), nullable = False)
    cidade = sa.Column(sa.VARCHAR(50), nullable = False)
    uf = sa.Column(sa.CHAR(2), nullable = False)

#tb produto
class produto(base):
    __tablename__ = "tbProduto"
    
    codigo_barras = sa.Column(sa.INTEGER, nullable = False, primary_key = True, index = True)
    registro_fornecedor = sa.Column(sa.INTEGER, sa.ForeignKey("tbFornecedor.registro_fornecedor", ondelete="NO ACTION", onupdate="CASCADE"), index = True)
    dsc_produto = sa.Column(sa.VARCHAR(100), nullable = False)
    genero = sa.Column(sa.CHAR(1))

#tb vendedor
class vendedor(base):
    __tablename__ = "tbVendedor"
    
    registro_vendedor = sa.Column(sa.INTEGER, nullable = False, primary_key = True, index = True)
    cpf = sa.Column(sa.VARCHAR(14), nullable = False)
    nome = sa.Column(sa.VARCHAR(100), nullable = False)
    genero = sa.Column(sa.CHAR(1), nullable = False)
    email = sa.Column(sa.VARCHAR(50), nullable = False)

#tb venda
class venda(base):
    __tablename__ = "tbVenda"
    
    idTransacao = sa.Column(sa.INTEGER, nullable = False, primary_key = True, index = True)
    cpf = sa.Column(sa.CHAR(14), sa.ForeignKey("tbCliente.cpf", ondelete="NO ACTION", onupdate="CASCADE"), index = True)
    codigo_barras = sa.Column(sa.INTEGER, sa.ForeignKey("tbProduto.codigo_barras", ondelete="NO ACTION", onupdate="CASCADE"), index = True)
    registro_vendedor = sa.Column(sa.INTEGER, sa.ForeignKey("tbVendedor.registro_vendedor", ondelete="NO ACTION", onupdate="CASCADE"), index = True)
    vlr_venda = sa.Column(sa.DECIMAL(10,2), nullable = False)
    data_hora_venda = sa.Column(sa.DATETIME(), nullable = False)
  

try:
    base.metadata.create_all(engine)  #criar as tabelas acima
    print("Tabelas criadas.")

except ValueError:
    ValueError()