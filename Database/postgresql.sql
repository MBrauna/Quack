-- Para composição da tabela de clientes - Sequencial, tabela e regras.
create sequence seq_cliente increment 1 start 1 minvalue 1 maxvalue 999999999999;
create table cliente
(
    id_cliente          integer     not null    default nextval('seq_cliente')
   ,nome                text        not null
   ,nome_fantasia       text
   ,cpf_cnpj            integer
   ,tipo_pessoa         integer     not null
   ,data_cadastro       timestamp   not null    default now()
   ,admin               integer     not null    default 0
   ,data_cria           timestamp   not null    default now()
   ,data_altera         timestamp   not null    default now()
   ,usr_cria            text        not null    default user
   ,usr_altera          text        not null    default user
   ,primary key(id_cliente)
   ,constraint ck_cliente_tipopessoa    check (tipo_pessoa in (0,1,2))
   ,constraint ck_cliente_admin         check (admin in (0,1))
   ,constraint uk_cliente_cpfcnpjtp     unique (cpf_cnpj,tipo_pessoa)
);
comment on column cliente.id_cliente     is 'Código único do cliente - Referência para posteriores informações';
comment on column cliente.nome           is 'Nome do cliente - Nome ou Nome completo da empresa';
comment on column cliente.nome_fantasia  is 'Nome fantasia ou apelido';
comment on column cliente.cpf_cnpj       is 'Registro governamental - CPF CNPJ';
comment on column cliente.tipo_pessoa    is '[0] - Pessoa Física, [1] - Pessoa Jurídica, [2] - Fornecedor';
comment on column cliente.data_cadastro  is 'Data de cadastro do cliente na base MBrauna Core';
comment on column cliente.admin          is '[0] - Normal, [1] - Administrador';


create index idx_cliente_nome          on cliente(nome asc nulls last);
create index idx_cliente_cpf_cnpj      on cliente(cpf_cnpj asc nulls last);
create index idx_cliente_tpessoa       on cliente(tipo_pessoa asc nulls last);
create index idx_cliente_dtcadastro    on cliente(data_cadastro asc nulls last);
create index idx_cliente_admin         on cliente(admin asc nulls last);







-- Composição da tabela de elementos - O elemento será referenciado a classe treinada em MBrauna Core.
create sequence seq_elemento increment 1 start 1 minvalue 1 maxvalue 999999999999;
create table elemento
(
    id_elemento         integer     not null    default nextval('seq_elemento')
   ,descricao           text        not null    default 'ELEMENTO INVÁLIDO'
   ,item_nome           text        not null    default '00000000'
   ,ativo               integer     not null    default 0
   ,primary key(id_elemento)
   ,constraint ck_elemento_ativo        check (ativo in (0,1))
   ,constraint uk_elemento_itemnome     unique (item_nome)
);
comment on column elemento.id_elemento  is 'Código único para referência do elemento';
comment on column elemento.descricao    is 'Descrição visual do elemento';
comment on column elemento.item_nome    is 'Referência do item em MBraunaCore';
comment on column elemento.ativo        is '[0] - Inativo, [1] - Ativo';

create index idx_elemento_desc          on elemento(descricao asc nulls last);
create index idx_elemento_itemnome      on elemento(item_nome asc nulls last);
create index idx_elemento_ativo         on elemento(ativo asc nulls last);

-- Composição da tabela de sistema - O HASH será o código de conexão entre as tabelas caso necessária importação
create table sistema
(
    hash                text        not null    default md5(to_char(now(),'DDMMYYYYHH24MISS') || 'MBrauna')
   ,descricao           text        not null
   ,ativo               integer     not null    default 0
   ,id_cliente          integer
   ,data_cria           timestamp   not null    default now()
   ,data_altera         timestamp   not null    default now()
   ,usr_cria            text        not null    default user
   ,usr_altera          text        not null    default user
   ,primary key(hash)
   ,constraint ck_sistema_ativo         check (ativo in (0,1))
   ,constraint fk_sistema_id_cliente    foreign key(id_cliente) references cliente(id_cliente)
);
comment on column sistema.hash          is 'Código único - HASH - de identificação do sistema';
comment on column sistema.descricao     is 'Descrição do sistema';
comment on column sistema.ativo         is '[0] - Inativo, [1] - Ativo';
comment on column sistema.id_cliente    is 'Código de referência ao cliente - Usuário responsável pelo cliente';


create index idx_sistema_desc          on sistema(descricao asc nulls last);
create index idx_sistema_idcli         on sistema(id_cliente asc nulls last);
create index idx_sistema_ativo         on sistema(ativo asc nulls last);





-- Composição da tabela de sistema_camera - Será interligada à tabela Sistema.
create sequence seq_sistema_camera increment 1 start 1 minvalue 1 maxvalue 999999999999;
create table sistema_camera
(
    id_sistema_camera   integer     not null    default nextval('seq_sistema_camera')
   ,hash_sistema        text        not null
   ,url_camera          text        not null
   ,ponto_corte         integer     not null    default 50
   ,descricao           text        not null
   ,ativo               integer     not null    default 0
   ,data_cria           timestamp   not null    default now()
   ,data_altera         timestamp   not null    default now()
   ,usr_cria            text        not null    default user
   ,usr_altera          text        not null    default user
   ,primary key(id_sistema_camera)
   ,constraint fk_sistema_camera_hash   foreign key (hash_sistema) references sistema(hash)
   ,constraint ck_sistema_camera_ativo  check (ativo in (0,1))
);
comment on column sistema_camera.id_sistema_camera  is 'Código único sequencial para cadastro de câmeras';
comment on column sistema_camera.hash_sistema       is 'Hash do sistema';
comment on column sistema_camera.url_camera         is 'Caminho para a câmera IP ou DVR e seu respectivo canal';
comment on column sistema_camera.ativo              is '[0] - Inativo, [1] - Ativo';


create index idx_sistema_camera_hash   on sistema_camera(hash_sistema asc nulls last);
create index idx_sistema_camera_url    on sistema_camera(url_camera asc nulls last);
create index idx_sistema_camera_corte  on sistema_camera(ponto_corte asc nulls last);
create index idx_sistema_camera_desc   on sistema_camera(descricao asc nulls last);
create index idx_sistema_camera_ativo  on sistema_camera(ativo asc nulls last);


-- Composição da tabela de logs das câmeras
create sequence seq_camera_deteccao increment 1 start 1 minvalue 1 maxvalue 999999999999;
create table camera_deteccao
(
    id_camera_deteccao  integer             not null default nextval('seq_camera_deteccao')
   ,id_sistema_camera   integer
   ,id_elemento         integer             not null
   ,probabilidade       double precision    not null
   ,dimensao_sup_esq    integer             not null
   ,dimensao_sup_dir    integer             not null
   ,dimensao_inf_esq    integer             not null
   ,dimensao_inf_dir    integer             not null
   ,base64              text
   ,data_deteccao       timestamp           not null default now()
   ,id_cam_deteccao_ant integer
   ,primary key(id_camera_deteccao)
   ,constraint fk_camera_deteccao_sistcam   foreign key(id_sistema_camera)    references sistema_camera(id_sistema_camera)
   ,constraint fk_camera_deteccao_elemento  foreign key(id_elemento)          references elemento(id_elemento)
   ,constraint fk_camera_deteccao_anterior  foreign key(id_cam_deteccao_ant)  references camera_deteccao(id_camera_deteccao)
);

create index idx_camera_deteccao_siscam   on camera_deteccao(id_sistema_camera asc nulls last);
create index idx_camera_deteccao_elemento on camera_deteccao(id_elemento asc nulls last);
create index idx_camera_deteccao_probab   on camera_deteccao(probabilidade asc nulls last);
create index idx_camera_deteccao_dsupesq  on camera_deteccao(dimensao_sup_esq asc nulls last);
create index idx_camera_deteccao_dsupdir  on camera_deteccao(dimensao_sup_dir asc nulls last);
create index idx_camera_deteccao_dinfesq  on camera_deteccao(dimensao_inf_esq asc nulls last);
create index idx_camera_deteccao_dinfdir  on camera_deteccao(dimensao_inf_dir asc nulls last);
create index idx_camera_deteccao_data     on camera_deteccao(data_deteccao asc nulls last);
create index idx_camera_deteccao_idant    on camera_deteccao(id_cam_deteccao_ant asc nulls last);