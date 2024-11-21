import pandas as pd
import sqlalchemy as sa
import sqlalchemy.orm as orm
import vendas as vd

endereco = "C:\\temp\\PANDA\\PUC\\BANCO_DE_DADOS_RELACIONAL\\aula02\\"

vendedor = pd.read_csv(endereco + "vendedor.csv", sep=";")
vendedor = pd.DataFrame(vendedor)

engine = sa.create_engine('sqlite:///C:/temp/PANDA/PUC/BANCO_DE_DADOS_RELACIONAL/vendas.db')

sessao = orm.sessionmaker(bind=engine)
sessao = sessao()

for i in range(len(vendedor)):
    dados_vendedor = vd.vendedor(
        registro_vendedor = int(vendedor["registro_vendedor"][i]),
        cpf = vendedor["cpf"][i],
        nome = vendedor["nome"],
        genero = vendedor["genero"][i],
        email = vendedor["email"][i]
    )
    try:
        sessao.add(dados_vendedor)
        sessao.commit
    except ValueError:
        ValueError()
        
        
print("Dados inseridos na tabela vendedor")


