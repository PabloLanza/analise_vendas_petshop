import pandas as pd
import numpy as np

#CARREGANDO OS DADOS DA TABELA DE CLIENTES

#LISTA NOMES
nomes = [
    "Lucas Araujo", "Gabriel Oliveira", "Pedro Henrique", "Matheus Silva", "Joao Carvalho", "Rafael Santos", "Gustavo Almeida",
    "Felipe Costa", "Bruno Ferreira", "Leonardo Rodrigues", "Carlos Mendes", "Thiago Ribeiro", "Andre Martins", "Daniel Barbosa",
    "Eduardo Lima", "Marcos Souza", "Vinicius Rocha", "Rodrigo Nunes", "Diego Castro", "Caio Moreira", "Henrique Lopes",
    "Fernando Dias", "Guilherme Teixeira", "Arthur Correia", "Samuel Vieira", "Murilo Cardoso", "Igor Monteiro", "Joao Vitor",
    "Enzo Ramos", "Miguel Duarte", "Davi Batista", "Bernardo Freitas", "Nicolas Mendes", "Guilherme Moraes", "Alexandre Reis",
    "Ricardo Fernandes", "Marcelo Tavares", "Wesley Martins", "Victor Hugo", "Luiz Pereira", "Mateus Goncalves", "Otavio Barbosa",
    "Diego Andrade", "Renan Carvalho", "Alan Souza", "Jonathan Melo", "Cristian Lopes", "Nathan Rodrigues", "Emanuel Santos",
    "Yuri Oliveira", "Joao Pedro", "Maria Silva", "Ana Oliveira", "Juliana Santos", "Mariana Costa", "Camila Ferreira",
    "Beatriz Almeida", "Larissa Rodrigues", "Amanda Souza", "Isabela Lima", "Leticia Ribeiro", "Gabriela Martins", "Manuela Carvalho",
    "Luana Mendes", "Rafaela Castro", "Carolina Rocha", "Fernanda Nunes", "Bruna Dias", "Bianca Teixeira", "Aline Correia",
    "Vanessa Vieira", "Natalia Cardoso", "Patricia Monteiro", "Jessica Ramos", "Renata Duarte", "Clara Batista", "Helena Freitas",
    "Laura Moraes", "Valentina Reis", "Sofia Fernandes", "Alice Tavares", "Luiza Pereira", "Yasmin Goncalves", "Eduarda Andrade",
    "Melissa Melo", "Nicole Lopes", "Heloisa Rodrigues", "Isadora Santos", "Cecilia Oliveira", "Elisa Souza", "Agatha Lima",
    "Lorena Ribeiro", "Mirella Martins", "Sarah Carvalho", "Esther Mendes", "Valeria Castro", "Raquel Rocha", "Sabrina Nunes",
    "Tatiane Teixeira"
]

#LISTA TELEFONES (GARANTINDO QUE TELEFONES REAIS NÃO SEJAM GERADOS)
telefone = [f'111222333{i:02d}' for i in range(len(nomes))]

#LISTA CPF (GARANTINDO QUE CPFS REAIS NÃO SEJAM GERADOS)
cpf = [f'000123456{i:02d}' for i in range(len(nomes))]

#LISTA ENDEREÇOS
enderecos = [
    "Rua das Amoras", "Rua das Bananas", "Rua das Mangas", "Rua das Laranjas", "Rua dos Abacaxis", "Rua das Uvas", "Rua dos Morangos",
    "Rua das Goiabas", "Rua dos Limões", "Rua das Acerolas", "Rua das Jabuticabas", "Rua das Pitangas", "Rua dos Cajus", "Rua das Melancias",
    "Rua dos Maracujás", "Rua das Framboesas", "Rua dos Mirtilos", "Rua das Cerejas", "Rua dos Pêssegos", "Rua das Peras", "Rua das Maçãs",
    "Rua dos Mamões", "Rua dos Figos", "Rua das Tangerinas", "Rua dos Kiwis", "Rua das Romãs", "Rua dos Abacates", "Rua das Ameixas",
    "Rua das Carambolas", "Rua dos Cocos", "Rua das Graviolas", "Rua dos Tamarindos", "Rua das Pitaias", "Rua dos Physalis", "Rua das Groselhas",
    "Rua dos Duriões", "Rua das Nectarinas", "Rua dos Damascos", "Rua das Lichias", "Rua dos Mangostões", "Rua das Tâmaras", "Rua das Seriguelas",
    "Rua dos Ingás", "Rua das Bacabas", "Rua dos Buritis", "Rua das Pupunhas", "Rua dos Pequis", "Rua das Atemoias", "Rua dos Cambucás",
    "Rua das Grumixamas", "Rua dos Araçás", "Rua dos Jenipapos", "Rua das Mangabas", "Rua dos Muricis", "Rua das Cabeludinhas", "Rua dos Bacuris",
    "Rua das Sapotis", "Rua dos Umbus", "Rua das Pitombas", "Rua dos Oitis", "Rua das Guabirobas", "Rua dos Cajás", "Rua dos Cupuaçus",
    "Rua dos Açaís", "Rua das Castanhas", "Rua dos Pinhas", "Rua das Melões", "Rua das Laranjeiras", "Rua dos Limões-Sicilianos", "Rua das Tangerineiras",
    "Rua dos Pessegueiros", "Rua das Macieiras", "Rua das Pereiras", "Rua dos Morangueiros", "Rua das Cerejeiras", "Rua dos Abacateiros", "Rua das Mangueiras",
    "Rua dos Coqueiros", "Rua das Bananeiras", "Rua das Goiabeiras", "Rua dos Maracujazeiros", "Rua das Aceroleiras", "Rua das Pitangueiras", "Rua dos Cajueiros",
    "Rua das Jabuticabeiras", "Rua das Romãzeiras", "Rua dos Figueirais", "Rua das Ameixeiras", "Rua dos Mamoeiros", "Rua das Caramboleiras", "Rua das Frutas Vermelhas",
    "Rua dos Abacaxis Doces", "Rua das Uvas Roxas", "Rua dos Morangos Silvestres", "Rua das Mangas Rosadas", "Rua dos Limões Verdes", "Rua das Peras Doces", 
    "Rua das Maçãs Verdes", "Rua das Graviolas"
]

#LISTA DE BAIRROS
bairros = [
    "Bairro Leoes", "Bairro Lobos", "Bairro Tigres", "Bairro Ursos", "Bairro Raposas",
    "Bairro Cobras", "Bairro Aguias", "Bairro Falcões", "Bairro Onças",
    "Bairro Elefantes", "Bairro Rinocerontes", "Bairro Gorilas"
]

#CRIANDO A TABELA DE CLIENTES
dim_cliente = pd.DataFrame(
    {"id_cliente": range(1, len(nomes) + 1),
     "nome": nomes,
     "telefone": telefone,
     "endereco": enderecos,
     "bairro": np.random.choice(bairros, size=len(nomes)),
     "cpf": cpf}
)

#-------------------------------------------------------------------------------------------------------------

#CARREGANDO OS DADOS DA TABELA VENDEDORES

dim_vendedor = pd.DataFrame(
    {"id_vendedor": [1, 2, 3],
     "nome": ["Pablo", "Allysson", "Ingredi"]}
)


#-------------------------------------------------------------------------------------------------------------

#CARREGANDO DADOS DA TABELA CATEGORIA

dim_categoria = pd.DataFrame(
    {"id_categoria": [1, 2, 3, 4],
     "nome": ["Ração", "Acessórios", "Brinquedos", "Banho"],
     "descrição": ["Rações, Petiscos e Alimentos", "Comedouros, Bebedouros e Coleiras", 
                   "Bolinhas, Pelúcias e Demais", "Shampoos, Escovas e Pentes"]
}
)

#-------------------------------------------------------------------------------------------------------------

#CARREGANDO DADOS DA TABELA FORMA DE PAGAMENTO

dim_formapagamento = pd.DataFrame(
    {"id_formapag": [1, 2, 3, 4],
     "tipo": ["Dinheiro", "PIX", "Cartão Crédito", "Cartão Débito"]}
)

#--------------------------------------------------------------------------------------------------------------

#CARREGANDO DADOS DA TABELA PRODUTO (aqui eu resolvi criar separado os produtos pra cada 
# categoria pra facilitar a inserção dos dados na tabela)

id_racoes = [1, 2, 3, 4, 5, 6, 7, 8]
prod_racoes = ["Ração de Combate", "Ração Premium", "Ração Premium Plus", "Ração Premium Especial", 
               "Ração Super Premium", "Bifinhos", "Biscoito", "Sache"]
precocusto_racoes = [40.11, 68.15, 75.24, 95.35, 154.25, 1.54, 14.50, 2.25]

id_acessorios = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
prod_acessorios = ["Comedouro/Bebedouro Peq", "Comedouro/Bebedouro Med", "Comedouro/Bebedouro Grd", "Coleira Couro",
                   "Coleira Costura", "Guia", "Peitoral", "Caminha Peq", "Caminha Med", "Caminha Grd"]
precocusto_acessorios = [2.15, 3.35, 5.75, 6.58, 5.42, 8.45, 11.58, 54.15, 65.45, 77.32]

id_brinq = [19, 20, 21, 22, 23, 24, 25, 26]
prod_brinq = ["Brinquedo Hamburguer", "Brinquedo Coxinha", "Bolinha Cravo", "Bola Tenis", "Bola Maciça", 
              "Disco", "Macaco de Pelúcia", "Urso de Pelúcia"]
precocusto_brinq = [4.54, 4.75, 2.25, 7.45, 15.59, 12.45, 12.65, 13.75]

id_banho = [27, 28, 29, 30, 31, 32, 33, 34]
prod_banho = ["Shampoo Clareador", "Shampoo Neutro", "Shampoo Melancia", "Kit Shampoo e Condicionador", 
"Escova de Plástico", "Escova de Aço", "Pente", "Colônia"]
precocusto_banho = [7.99, 7.52, 8.52, 16.45, 10.25, 12.47, 11.25, 9.89]

#INSERINDO OS PRIMEIROS DADOS NA TABELA DE PRODUTOS (pra ser fiel a uma loja real, resolvi jogar uma margem especifica sobre 
#o preço de custo pra ser o preço de venda)

dim_produto = pd.DataFrame(
    {"id_produto": id_racoes,
     "nome": prod_racoes,
     "precoCusto": precocusto_racoes,
     "precoVenda": [preco * 1.45 for preco in precocusto_racoes], 
     "quantidadeEstoque": np.random.randint(1, 101, size=len(prod_racoes)),
     "id_categoria": 1}
)


#------------------------------------------------------------------------------------------------------------

# INSERINDO A SEGUNDA PARTE DOS PRODUTOS NA TABELA DE PRODUTOS
dim_prod2 = pd.DataFrame(
    {"id_produto": id_acessorios,
     "nome": prod_acessorios,
     "precoCusto": precocusto_acessorios,
     "precoVenda": [preco * 1.75 for preco in precocusto_acessorios],
     "quantidadeEstoque": np.random.randint(1, 101, size=len(prod_acessorios)),
     "id_categoria": 2}
)

dim_produto = pd.concat([dim_produto, dim_prod2], ignore_index=True)


#--------------------------------------------------------------------------------------------------------------

#INSERINDO A TERCEIRA PARTE DOS PRODUTOS NA TABELA DE PRODUTOS
dim_prod3 = pd.DataFrame(
    {"id_produto": id_brinq,
     "nome": prod_brinq,
     "precoCusto": precocusto_brinq,
     "precoVenda": [preco * 1.75 for preco in precocusto_brinq],
     "quantidadeEstoque": np.random.randint(1, 101, size=len(prod_brinq)),
     "id_categoria": 3}
)

dim_produto = pd.concat([dim_produto, dim_prod3], ignore_index=True)


#--------------------------------------------------------------------------------------------------------------

#INSERINDO A QUARTA E ÚLTIMA PARTE DOS PRODUTOS NA TABELA DE PRODUTOS
dim_prod4 = pd.DataFrame(
    {"id_produto": id_banho,
     "nome": prod_banho,
     "precoCusto": precocusto_banho,
     "precoVenda": [preco * 1.75 for preco in precocusto_banho],
     "quantidadeEstoque": np.random.randint(1, 101, size=len(prod_banho)),
     "id_categoria": 4}
)

dim_produto = pd.concat([dim_produto, dim_prod4], ignore_index=True) #VERSÃO FINAL

print(dim_produto.head())
print(dim_produto.tail())

#--------------------------------------------------------------------------------------------------------------

#CARREGANDO DADOS NA TABELA DE DATA

datas = pd.date_range(start="2026-01-01", end="2026-08-31", freq="D")

dias_semana = {
    0: "Segunda",
    1: "Terça",
    2: "Quarta",
    3: "Quinta",
    4: "Sexta",
    5: "Sábado",
    6: "Domingo"
}

meses = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro"
}

dim_data = pd.DataFrame(
    {"dataCompleta": datas,
     "dia": datas.day,
     "mes": datas.month,
     "nomeMes": datas.month.map(meses),
     "ano": datas.year,
     "diaSemana": datas.dayofweek.map(dias_semana)}
)


#-----------------------------------------------------------------------------------------------------------

#CARREGANDO DADOS NA TABELA FATO (VENDAS)

diasUteis = dim_data[dim_data["diaSemana"] != "Domingo"]["dataCompleta"]
#AQUI ESTOU GARANTINDO QUE VENDAS NÃO SEJAM FEITAS AOS DOMINGOS

#INSERINDO 5000 TRANSAÇÕES
fato_venda = pd.DataFrame(
    {"id_venda": range(1, 5001),
     "data": np.random.choice(diasUteis, size=5000, replace=True),
     "id_cliente": np.random.choice(dim_cliente["id_cliente"], 5000, replace=True),
     "id_vendedor": np.random.choice(dim_vendedor["id_vendedor"], 5000, replace=True),
     "id_formapag": np.random.choice(dim_formapagamento["id_formapag"], 5000, replace=True),
     "id_produto": np.random.choice(dim_produto["id_produto"], 5000, replace=True),
     "quantidadeVendida": np.random.randint(1, 5, size=5000),
     "desconto": np.round(np.random.uniform(0, 0.05, size=5000), 2)
     }
)

#INSERINDO A COLUNA DE CUSTO TOTAL (CUSTO DO PRODUTO * QUANTIDADE)
fato_venda["custoTotal"] = (
    fato_venda["id_produto"].map(
        dim_produto.set_index("id_produto")["precoCusto"]
    )
    * fato_venda["quantidadeVendida"]
)

#INSERINDO A COLUNA DE VALOR DE VENDA (PREÇO VENDA DO PRODUTO * QUANTIDADE)
fato_venda["valorVendaBruta"] = (
    fato_venda["id_produto"].map(
        dim_produto.set_index("id_produto")["precoVenda"]
    )
    * fato_venda["quantidadeVendida"]
)

#-------------------------------------------------------------------------------------------------------------

#SALVANDO AS TABELAS EM ARQUIVOS CSV

dim_cliente.to_csv("../data/dim_cliente.csv", index=False)
dim_produto.to_csv("../data/dim_produto.csv", index=False)
dim_vendedor.to_csv("../data/dim_vendedor.csv", index=False)
dim_formapagamento.to_csv("../data/dim_formapagamento.csv", index=False)
dim_data.to_csv("../data/dim_data.csv", index=False)
dim_categoria.to_csv("..data/dim_categoria.csv", index=False)
fato_venda.to_csv("../data/fato_venda.csv", index=False)

