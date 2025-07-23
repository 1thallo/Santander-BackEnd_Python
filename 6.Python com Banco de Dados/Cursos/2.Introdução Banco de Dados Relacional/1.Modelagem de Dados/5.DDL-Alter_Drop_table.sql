/* PROBLEMA
Usuários com endereços longos não estão conseguindo realizar cadastro no sistema
	Opções:
    - Recriar a tabela, migrar os dados e excluir a tabela antiga
    - Alterar a estrutura da tabela
*/

CREATE TABLE BTCTB001_USUARIO_NOVA
(
	ID_USUARIO INT AUTO_INCREMENT COMMENT 'Identificador único serial do usuário'
,	NO_USUARIO VARCHAR(200) NOT NULL COMMENT 'Nome do usuário'
,	EE_USUARIO VARCHAR(100) NOT NULL COMMENT 'E-mail do usuário'
,	ED_USUARIO VARCHAR(255) NOT NULL COMMENT 'Endereço do usuário'          -- Antes (100), Depois (255)
,	DT_NASCIMENTO DATE	NOT NULL COMMENT 'Data de nascimento do usuário'
,	CONSTRAINT PK_BTCTB001 PRIMARY KEY (ID_USUARIO)
,	CONSTRAINT UK01_BTCTB001 UNIQUE (NO_USUARIO,EE_USUARIO)
) COMMENT = 'Tabela de usuário';

-- Migrar os dados da tabela antiga para a nova
INSERT INTO BTCTB001_USUARIO_NOVA (NO_USUARIO, EE_USUARIO, ED_USUARIO, DT_NASCIMENTO)
SELECT NO_USUARIO, EE_USUARIO, ED_USUARIO, DT_NASCIMENTO
FROM BTCTB001_USUARIO;

-- Preciso apagar a FK temporariamente para deletar a tabela
ALTER TABLE BTCTB003_RESERVA DROP FOREIGN KEY FK01_BTCTB001_BTCTB003;

DROP TABLE BTCTB001_USUARIO;

-- Renomear a tabela nova
ALTER TABLE BTCTB001_USUARIO_NOVA RENAME BTCTB001_USUARIO;
DESCRIBE BTCTB001_USUARIO;

-- ==== Opcao 2 ====
ALTER TABLE BTCTB001_USUARIO MODIFY COLUMN ED_USUARIO VARCHAR(255);