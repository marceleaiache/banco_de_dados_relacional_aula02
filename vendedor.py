import pandas as pd
import sqlalchemy as sa
import sqlalchemy.orm as orm
import vendas as vd

endereco = "C:\\temp\\PANDA\\PUC\\BANCO_DE_DADOS_RELACIONAL\\aula02\\"

vendedor = pd.read_csv(endereco + "vendedor.csv", sep=";")
tbVendedor = pd.DataFrame(vendedor)

engine = sa.create_engine("sqlite:///C:/temp/PANDA/PUC/BANCO_DE_DADOS_RELACIONAL/aula02/vendas.db")

sessao = orm.sessionmaker(bind=engine)
sessao = sessao()

for i in range(len(tbVendedor)):
    dados_vendedor = vd.vendedor(
        registro_vendedor = int(tbVendedor["registro_vendedor"][i]),
        cpf = vendedor["cpf"][i],
        nome = vendedor["nome"][i],
        genero = vendedor["genero"][i],
        email = vendedor["email"][i]
    )
    try:
        sessao.add(dados_vendedor)
        sessao.commit()
        
    except ValueError:
        ValueError()
        sessao.rollback()
       
print("Dados inseridos na tabela vendedor")

produto = pd.read_excel(endereco + "produto.xlsx")

tbProduto = pd.DataFrame(produto)

conn = engine.connect()

# metodo descontinuado -> metadata = sa.schema.MetaData(bind=engine)

metadata = sa.schema.MetaData()
metadata.bind = engine

DadosProduto = tbProduto.to_dict(orient="records")

tabela_produto = sa.Table(vd.produto.__tablename__, metadata, autoload_with=engine) # descontinuado -> autoload=True

try:
    conn.execute(tabela_produto.insert(), DadosProduto)
    sessao.commit()
except ValueError:
    ValueError()
    
print("Dados inseridos na tabela tbProduto")

sessao.close_all()
    