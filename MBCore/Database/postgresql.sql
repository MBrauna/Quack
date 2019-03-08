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

















































----------------------------------------------------------------------------
----------------------------------------------------------------------------
--                          TABELAS PARA MBServer                         --
----------------------------------------------------------------------------
----------------------------------------------------------------------------
create sequence seq_cliente increment 1 start 1 minvalue 1 maxvalue 999999999;
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
  ,CONSTRAINT pk_cliente            PRIMARY KEY (id_cliente)
  ,CONSTRAINT uk_cliente_cnpjcpf    UNIQUE (cnpj_cpf)
  ,CONSTRAINT ck_cliente_vip        CHECK (vip in (0,1))
  ,CONSTRAINT ck_cliente_tppessoa   CHECK (tipo_pessoa in (0,1))
  ,CONSTRAINT ck_cliente_admin      CHECK (admin in (0,1))
);


comment on column cliente.id_cliente     is 'Código único - SEQUENCIAL DO CLIENTE';
comment on column cliente.nome           is 'Nome do cliente - Se pessoa jurídica nome real.';
comment on column cliente.nome_fantasia  is 'Nome fantasia ou apelido do cliente';
comment on column cliente.cnpj_cpf       is 'Código de cadastro à receita federal';
comment on column cliente.tipo_pessoa    is '[0] - Pessoa física, [1] - Pessoa Jurídica';
comment on column cliente.vip            is '[0] - Não, [1] - Sim';
comment on column cliente.admin          is '[0] - Não, [1] - Sim';
comment on table  cliente                is 'Tabela de clientes - Toda pessoa física ou jurídica que por algum motivo iteragir com a aplicação deverá ser cadastrada nesta tabela';


create index idx_cliente_nome          on cliente(nome asc nulls last);
create index idx_cliente_cnpj_cpf      on cliente(cnpj_cpf asc nulls last);
create index idx_cliente_tpessoa       on cliente(tipo_pessoa asc nulls last);
create index idx_cliente_dtcadastro    on cliente(data_cadastro asc nulls last);
create index idx_cliente_admin         on cliente(admin asc nulls last);
create index idx_cliente_vip           on cliente(vip asc nulls last);

CREATE FUNCTION public.tg_ins_cliente() RETURNS trigger AS
$BODY$
declare
begin
  if (TG_OP = 'INSERT') then
    new.id_cliente    := nextval('seq_cliente');
    new.data_cadastro := now();

    if new.tipo_pessoa is null then
      if length(new.cnpj_cpf) <= 11 then
        new.tipo_pessoa := 0; -- [0] - Pessoa física
      else
        new.tipo_pessoa := 1; -- [1] - Pessoa Jurídica
      end if; -- if length(new.cnpj_cpf) <= 11 then
    end if; -- if new.tipo_pessoa is null then
    
  elsif (TG_OP = 'UPDATE') then
    new.id_cliente    := old.id_cliente;
    new.data_cadastro := old.data_cadastro;
  elsif (TG_OP = 'DELETE') then
    RAISE INFO 'Não é possível remover o cliente %', now();
  end if;

  return new;
end;$BODY$
LANGUAGE plpgsql VOLATILE NOT LEAKPROOF;

CREATE TRIGGER tg_biur_cliente BEFORE INSERT OR UPDATE OR DELETE
   ON public.cliente FOR EACH ROW
   EXECUTE PROCEDURE public.tg_ins_cliente();








----------------------------------------------------------------------------
----------------------------------------------------------------------------
create sequence seq_sistema increment 1 start 1 minvalue 1 maxvalue 999999999;
CREATE TABLE sistema
(
   id_sistema           integer     NOT NULL
   hash                 text        NOT NULL
   ativo                integer     NOT NULL DEFAULT 0
   descricao            text        NOT NULL
   CONSTRAINT pk_sistema PRIMARY KEY (id_sistema)
   CONSTRAINT uk_sistema_hash UNIQUE (hash)
   CONSTRAINT ck_sistema_ativo CHECK (ativo in (0,1))
);


comment on column sistema.id_sistema    is 'Código sequencial - SISTEMAS DISPONÍVEIS';
comment on column sistema.hash          is 'Código único para uso do sistema';
comment on column sistema.ativo         is '[0] - Inativo, [1] - Ativo';
comment on column sistema.descricao     is 'Descrição do sistema vigente';
comment on table  sistema               is 'Sistemas MBrauna disponíveis para uso';

create index idx_sistema_hash   on sistema(hash asc nulls last);
create index idx_sistema_ativo  on sistema(ativo asc nulls last);


CREATE FUNCTION public.tg_sistema() RETURNS trigger AS
$BODY$begin
  if (TG_OP = 'INSERT') then
    new.id_sistema := nextval('seq_sistema');
    new.hash       := md5(to_char(now(),'DDMMYYYYHH24MISS') || new.id_sistema);
  elsif (TG_OP = 'UPDATE') then
    new.id_sistema := old.id_sistema; -- Impede alteração do ID
    new.hash       := old.hash;
  else
    RAISE INFO 'Não é possível remover o sistema %', now();
  end if;

  return new;
end;$BODY$
LANGUAGE plpgsql VOLATILE NOT LEAKPROOF;


CREATE TRIGGER tg_biur_sistema BEFORE INSERT OR UPDATE OR DELETE
   ON public.sistema FOR EACH ROW
   EXECUTE PROCEDURE public.tg_sistema();








----------------------------------------------------------------------------
----------------------------------------------------------------------------
create sequence seq_elemento increment 1 start 1 minvalue 1 maxvalue 999999999;
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








----------------------------------------------------------------------------
----------------------------------------------------------------------------
create sequence seq_sistema_acesso increment 1 start 1 minvalue 1 maxvalue 999999999;
create table public.sistema_acesso
(
  ,id_sistema_acesso        integer     not null
  ,chave_acesso             text        not null
  ,id_cliente               integer     not null
  ,id_sistema               integer     not null
  ,situacao                 integer     not null default 0
  constraint pk_sistema_acesso              primary key (id_sistema_acesso),
  constraint fk_sistema_acesso_idcliente    foreign key (id_cliente) references public.cliente (id_cliente) match simple on update no action on delete no action,
  constraint fk_sistema_acesso_idsistema    foreign key (id_sistema) references public.sistema (id_sistema) match simple on update no action on delete no action,
  constraint ck_sistema_acesso_situacao     check (situacao = any (array[0, 1]))
);

comment on table  sistema_acesso                     is 'Tabela de liberação de acessos por período';
comment on column sistema_acesso.id_sistema_acesso   is 'Código sequencial - Dado único para acesso ao sistema';
comment on column sistema_acesso.chave_acesso        is 'Chave de acesso ao sistema - Através desta chave os dados serão atualizados em MBCore';
comment on column sistema_acesso.id_cliente          is 'Chave de referência aos dados do cliente';
comment on column sistema_acesso.id_sistema          is 'Código de referência ao sistema';
comment on column sistema_acesso.situacao            is '[0] - Inativo, [1] - Ativo';

CREATE FUNCTION public.tg_sistema_acesso() RETURNS trigger AS
$BODY$declare
  v_contador integer;
begin
  select count(1)
    into v_contador
    from sistema_acesso sa
   where sa.id_cliente   = new.id_cliente
     and sa.id_sistema   = new.id_sistema
     and sa.sistuacao    = 1
        ;

  if v_contador > 0 then
    raise info 'Já existe um registro definido para o cliente %! Verifique.', new.id_cliente;
  end if;

  if (TG_OP = 'INSERT') then
    new.id_sistema_acesso := nextval('seq_sistema_acesso');
    new.chave_acesso      := md5(to_char(now(),'DDMMYYYYHH24MISS') || new.id_sistema_acesso);
  elsif (TG_OP = 'UPDATE') then
    new.id_sistema_acesso := old.id_sistema_acesso;
    new.chave_acesso      := old.chave_acesso;
    new.id_cliente        := old.id_cliente;
    new.id_sistema        := old.id_sistema;
  else
    raise info 'Não é possível remover o registro SISTEMA_ACESSO %', now();
  end if;
end;$BODY$
LANGUAGE plpgsql VOLATILE NOT LEAKPROOF;

CREATE TRIGGER tg_biur_sistema_acesso BEFORE INSERT OR UPDATE OR DELETE
   ON public.sistema_acesso FOR EACH ROW
   EXECUTE PROCEDURE public.tg_sistema_acesso();