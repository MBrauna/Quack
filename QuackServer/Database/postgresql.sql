-----------------------------------------------------------------------------------------
create database quackserver with encoding='utf8' connection limit=-1;
-----------------------------------------------------------------------------------------
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
  ,chave_acesso     text                        NOT NULL
  ,CONSTRAINT pk_cliente            PRIMARY KEY (id_cliente)
  ,CONSTRAINT uk_cliente_cnpjcpf    UNIQUE (cnpj_cpf)
  ,CONSTRAINT uk_cliente_chave      UNIQUE (chave_acesso)
  ,CONSTRAINT ck_cliente_vip        CHECK (vip in (0,1))
  ,CONSTRAINT ck_cliente_tppessoa   CHECK (tipo_pessoa in (0,1))
  ,CONSTRAINT ck_cliente_admin      CHECK (admin in (0,1))
);

comment on column cliente.id_cliente    is 'Código único - SEQUENCIAL DO CLIENTE';
comment on column cliente.nome          is 'Nome do cliente - Se pessoa jurídica nome real.';
comment on column cliente.nome_fantasia is 'Nome fantasia ou apelido do cliente';
comment on column cliente.cnpj_cpf      is 'Código de cadastro à receita federal';
comment on column cliente.tipo_pessoa   is '[0] - Pessoa física, [1] - Pessoa Jurídica';
comment on column cliente.vip           is '[0] - Não, [1] - Sim';
comment on column cliente.admin         is '[0] - Não, [1] - Sim';
comment on column cliente.chave_acesso  is 'Chave de acesso do cliente - Código único';
comment on table  cliente               is 'Tabela de clientes - Toda pessoa física ou jurídica que por algum motivo iteragir com a aplicação deverá ser cadastrada nesta tabela';

create index idx_cliente_nome           on cliente(nome asc nulls last);
create index idx_cliente_cnpj_cpf       on cliente(cnpj_cpf asc nulls last);
create index idx_cliente_tpessoa        on cliente(tipo_pessoa asc nulls last);
create index idx_cliente_dtcadastro     on cliente(data_cadastro asc nulls last);
create index idx_cliente_admin          on cliente(admin asc nulls last);
create index idx_cliente_vip            on cliente(vip asc nulls last);
create index idx_cliente_chaveacesso    on cliente(chave_acesso asc nulls last);

CREATE FUNCTION public.tg_cliente() RETURNS trigger AS
$BODY$
declare
begin
  if (TG_OP = 'INSERT') then
    new.id_cliente      :=  nextval('seq_cliente');
    new.data_cadastro   :=  now();
    new.chave_acesso    :=  md5(to_char(now(),'DDMMYYYYHH24MISS') || new.id_cliente);

    if new.tipo_pessoa is null then
      if length(new.cnpj_cpf) <= 11 then
        new.tipo_pessoa := 0; -- [0] - Pessoa física
      else
        new.tipo_pessoa := 1; -- [1] - Pessoa Jurídica
      end if; -- if length(new.cnpj_cpf) <= 11 then
    end if; -- if new.tipo_pessoa is null then
    
  elsif (TG_OP = 'UPDATE') then
    new.id_cliente      :=  old.id_cliente;
    new.data_cadastro   :=  old.data_cadastro;
    new.chave_acesso    :=  old.chave_acesso;
  elsif (TG_OP = 'DELETE') then
    RAISE INFO 'Não é possível remover o cliente %', now();
  end if;

  return new;
end;$BODY$
LANGUAGE plpgsql VOLATILE NOT LEAKPROOF;

CREATE TRIGGER tg_biur_cliente BEFORE INSERT OR UPDATE OR DELETE
   ON public.cliente FOR EACH ROW
   EXECUTE PROCEDURE public.tg_cliente();
























































































































































































































































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
  ,chave_acesso         text        NOT NULL
  ,ativo                integer     NOT NULL DEFAULT 0
  ,descricao            text        NOT NULL
  ,CONSTRAINT pk_sistema PRIMARY KEY (id_sistema)
  ,CONSTRAINT uk_sistema_hash UNIQUE (chave_acesso)
  ,CONSTRAINT ck_sistema_ativo CHECK (ativo in (0,1))
);


comment on column sistema.id_sistema    is 'Código sequencial - SISTEMAS DISPONÍVEIS';
comment on column sistema.chave_acesso  is 'Código único para uso do sistema';
comment on column sistema.ativo         is '[0] - Inativo, [1] - Ativo';
comment on column sistema.descricao     is 'Descrição do sistema vigente';
comment on table  sistema               is 'Sistemas MBrauna disponíveis para uso';

create index idx_sistema_hash   on sistema(chave_acesso asc nulls last);
create index idx_sistema_ativo  on sistema(ativo asc nulls last);


CREATE FUNCTION public.tg_sistema() RETURNS trigger AS
$BODY$begin
  if (TG_OP = 'INSERT') then
    new.id_sistema    := nextval('seq_sistema');
    new.chave_acesso  := md5(to_char(now(),'DDMMYYYYHH24MISS') || new.id_sistema);
  elsif (TG_OP = 'UPDATE') then
    new.id_sistema    := old.id_sistema; -- Impede alteração do ID
    new.chave_acesso  := old.chave_acesso;
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
   id_sistema_acesso        integer     not null
  ,chave_acesso             text        not null
  ,id_cliente               integer     not null
  ,id_sistema               integer     not null
  ,situacao                 integer     not null default 0
  ,constraint pk_sistema_acesso              primary key (id_sistema_acesso)
  ,constraint fk_sistema_acesso_idcliente    foreign key (id_cliente) references public.cliente (id_cliente) match simple on update no action on delete no action
  ,constraint fk_sistema_acesso_idsistema    foreign key (id_sistema) references public.sistema (id_sistema) match simple on update no action on delete no action
  ,constraint ck_sistema_acesso_situacao     check (situacao = any (array[0, 1]))
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
     and sa.situacao    = 1
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