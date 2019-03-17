-- Cria o banco de dados Quack
create database quack with encoding='utf8' connection limit=-1;


-- Cria as sequencias
create sequence seq_sistema increment 1 start 1 minvalue 1 maxvalue 999999999;



-- Cria a tabela
create table sistema
(
    id_sistema      integer     not null
   ,descricao       text        not null
   ,sistema         integer     not null default 0
   ,usr_cria        text        not null
   ,usr_altera      text        not null
   ,data_cria       timestamp   not null
   ,data_altera     timestamp   not null
   ,primary key(id_sistema)
);



CREATE TABLE cliente
(
   id_cliente       integer                     NOT NULL
  ,nome             text                        NOT NULL
  ,nome_fantasia    text
  ,cnpj_cpf         integer
  ,tipo_pessoa      integer                     NOT NULL DEFAULT 0
  ,data_cadastro    timestamp without time zone NOT NULL DEFAULT now()
  ,vip              integer                     NOT NULL DEFAULT 0
  ,admin            integer                     NOT NULL DEFAULT 0
  ,chave_acesso     text                        NOT NULL
  ,CONSTRAINT pk_cliente            PRIMARY KEY (id_cliente)
  ,CONSTRAINT uk_cliente_cnpjcpf    UNIQUE (cnpj_cpf)
  ,CONSTRAINT uk_cliente_chave      UNIQUE (chave_acesso)
  ,CONSTRAINT ck_cliente_vip        CHECK (vip in (0,1))
  ,CONSTRAINT ck_cliente_tppessoa   CHECK (tipo_pessoa in (0,1))
  ,CONSTRAINT ck_cliente_admin      CHECK (admin in (0,1))
);





create table sistema_acesso
(
    id_sistema
   ,id_cliente
   ,data_inicio
   ,data_fim
);

-- Cria os comentários


-- Cria os índices