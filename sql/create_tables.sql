-- 1: CRIAÇÃO DAS TABELAS

CREATE TABLE IF NOT EXISTS dados(
	id_dados serial PRIMARY KEY,
	datas_dados date not null,
	valor_dados numeric not null
);

select * from dados;
drop table calculos;

delete from dados where id_dados in ()

CREATE TABLE IF NOT EXISTS logs(
	id_log serial PRIMARY KEY,
	usuario_log varchar not null,
	data_registro_log varchar not null,
	alteracao_log varchar not null
);

select * from logs;

CREATE TABLE IF NOT EXISTS calculos(
	id_calculo serial PRIMARY KEY,
	media numeric not null,
	mediana numeric not null,
	moda numeric not null,
	desvio_padrao numeric not null,
	maior_valor numeric not null,
	menor_valor numeric not null,
	data_inicio date not null,
	data_fim date not null
);

select * from calculos;

-- 2: DEFINIÇÃO DOS TRIGGERS FUNCTIONS

-- 2.1: Trigger function dos calculos:

CREATE OR REPLACE FUNCTION tgr_log_calc() RETURNS TRIGGER AS $$
	BEGIN
	-- Aqui temos um bloco IF que confirmará o tipo de operação
		IF(TG_OP = 'INSERT') THEN
			INSERT INTO logs(usuario_log, data_registro_log, alteracao_log)
			VALUES (CURRENT_USER, CURRENT_TIMESTAMP, ' Cálculo realizado e registrado com sucesso!
					O cálculo ' || NEW.* || ' foi inserido');
			RETURN NEW;
	-- Aqui temos um bloco IF que confirmará o tipo de operação de Atualização
		ELSIF (TG_OP = 'UPDATE') THEN
			INSERT INTO logs(usuario_log, data_registro_log, alteracao_log)
			VALUES (CURRENT_USER, CURRENT_TIMESTAMP, ' Alteração de resultado de cálculo realizado com sucesso!
					Os cálculo ' || NEW.* || ' teve seus valores modificados '
					|| OLD.* || ' com ' || NEW.* || ' .');
			RETURN NEW;	
	-- Aqui temos um bloco IF que confirmará o tipo de operação de Exclusão
		ELSIF (TG_OP = 'DELETE') THEN
			INSERT INTO logs(usuario_log, data_registro_log, alteracao_log)
			VALUES (CURRENT_USER, CURRENT_TIMESTAMP, ' Resultado de cálculo excluído!
					Os seguintes Resultados foram excluidos: ' || OLD.* || ' .');
			RETURN OLD;
		END IF;
		RETURN NULL;		
 	END;
$$
LANGUAGE 'plpgsql';

-- 2.2: Trigger function dos dados:

CREATE OR REPLACE FUNCTION tgr_log_dados() RETURNS TRIGGER AS $$
	BEGIN
	-- Aqui temos um bloco IF que confirmará o tipo de operação
		IF(TG_OP = 'INSERT') THEN
			INSERT INTO logs(usuario_log, data_registro_log, alteracao_log)
			VALUES (CURRENT_USER, CURRENT_TIMESTAMP, ' Dado registrado com sucesso!
					O dado ' || NEW.* || ' foi inserido');
			RETURN NEW;
	-- Aqui temos um bloco IF que confirmará o tipo de operação de Atualização
		ELSIF (TG_OP = 'UPDATE') THEN
			INSERT INTO logs(usuario_log, data_registro_log, alteracao_log)
			VALUES (CURRENT_USER, CURRENT_TIMESTAMP, ' Alteração de dado realizado com sucesso!
					O dado ' || NEW.* || ' teve seus valores modificados '
					|| OLD.* || ' com ' || NEW.* || ' .');
			RETURN NEW;	
	-- Aqui temos um bloco IF que confirmará o tipo de operação de Exclusão
		ELSIF (TG_OP = 'DELETE') THEN
			INSERT INTO logs(usuario_log, data_registro_log, alteracao_log)
			VALUES (CURRENT_USER, CURRENT_TIMESTAMP, ' Dados excluídos!
					Os seguintes dados foram excluidos: ' || OLD.* || ' .');
			RETURN OLD;
		END IF;
		RETURN NULL;		
 	END;
$$
LANGUAGE 'plpgsql';

-- 3: CRIAR OS TRIGGERS QUE ACIONARÃO OS T.F.

-- 3.1: Trigger dos calculos:

CREATE TRIGGER log_calc
	AFTER INSERT OR UPDATE OR DELETE ON calculos
		FOR EACH ROW
			EXECUTE PROCEDURE tgr_log_calc();
			
-- 3.2: Trigger dos dados
			
CREATE TRIGGER log_dados
	AFTER INSERT OR UPDATE OR DELETE ON dados
		FOR EACH ROW
			EXECUTE PROCEDURE tgr_log_dados();