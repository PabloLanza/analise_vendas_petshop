--- Criando o Schema

CREATE SCHEMA dw AUTHORIZATION abc123;

--- Criação das tabelas de dimensão

CREATE TABLE dw.dim_cliente (
    id_cliente SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    telefone VARCHAR(20),
    endereco VARCHAR(255),
    bairro VARCHAR(255),
    cpf VARCHAR(14) UNIQUE NOT NULL
);

CREATE TABLE dw.dim_vendedor (
    id_vendedor SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL
);

CREATE TABLE dw.dim_categoria (
    id_categoria SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    descricao VARCHAR(255)
);

CREATE TABLE dw.dim_produto (
    id_produto SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL UNIQUE,
    precoCusto DECIMAL(10,2) NOT NULL CHECK (precoCusto >= 0),
    precoVenda DECIMAL(10,2) NOT NULL CHECK (precoVenda >= 0),
    quantidadeEstoque INT NOT NULL CHECK (quantidadeEstoque >= 0),
    id_categoria INT NOT NULL,
    FOREIGN KEY (id_categoria) REFERENCES dw.dim_categoria(id_categoria)
);

CREATE TABLE dw.dim_formapagamento (
    id_formapag SERIAL PRIMARY KEY,
    tipo VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE dw.dim_data (
    dataCompleta DATE PRIMARY KEY,
    dia INT NOT NULL CHECK (dia BETWEEN 1 AND 31),
    mes INT NOT NULL CHECK (mes BETWEEN 1 AND 12),
    nomeMes VARCHAR(15) NOT NULL,
    ano INT NOT NULL CHECK(ano > 0),
    diaSemana VARCHAR(15) NOT NULL
);

--- Criação da tabela fato

CREATE TABLE dw.fato_venda (
    id_venda SERIAL PRIMARY KEY,
    data DATE NOT NULL,
    id_cliente INT NOT NULL,
    id_vendedor INT NOT NULL,
    id_formapag INT NOT NULL,
    id_produto INT NOT NULL,
    quantidadeVendida INT NOT NULL CHECK (quantidadeVendida > 0),
    desconto DECIMAL(10,2) NOT NULL CHECK (desconto >= 0),
    custoTotal DECIMAL(10,2) NOT NULL CHECK (custoTotal >= 0),
    valorVendaBruta DECIMAL(10,2) NOT NULL CHECK (valorVendaBruta >= 0),
    FOREIGN KEY (data) REFERENCES dw.dim_data(dataCompleta),
    FOREIGN KEY (id_cliente) REFERENCES dw.dim_cliente(id_cliente),
    FOREIGN KEY (id_vendedor) REFERENCES dw.dim_vendedor(id_vendedor),
    FOREIGN KEY (id_formapag) REFERENCES dw.dim_formapagamento(id_formapag),
    FOREIGN KEY (id_produto) REFERENCES dw.dim_produto(id_produto)
);