# Normalização do modelo para a 1FN
/* O campo "endereco" contem multiplos valores e deve ser normalizado, 
ou seja, divido em colunas separadas, mantendo atomicidade dos dados 

Obs: Cenário de abstração simplificado onde um usuário só tem um endereço */

ALTER TABLE BTCTB001_USUARIO
	ADD NO_RUA VARCHAR(100) NULL
    , ADD NR_ENDERECO VARCHAR(10)
    , ADD NO_CIDADE VARCHAR(50)
    , ADD NO_ESTADO VARCHAR(20);

UPDATE BTCTB001_USUARIO
	SET	NO_RUA = TRIM(SUBSTRING_INDEX(ED_USUARIO, ',', 1)),
		NR_ENDERECO = TRIM(SUBSTRING_INDEX(SUBSTRING_INDEX(ED_USUARIO, ',', 2), ',', -1)),
		NO_CIDADE = TRIM(SUBSTRING_INDEX(SUBSTRING_INDEX(ED_USUARIO, ',', 3), ',', -1)),
		NO_ESTADO = TRIM(SUBSTRING_INDEX(ED_USUARIO, ',', -1));

SELECT * FROM BTCTB001_USUARIO;
/*
1	Ithallo Leandro R. Barbosa	ithalloflu@gmail.com	Rua A, 123, Cidade A, Estado B	2004-10-01	Rua A	123	Cidade A	Estado B
2	Leandro R. Barbosa	leandro@gmail.com	Rua B, 456, Cidade C, Estado D	2005-01-10	Rua B	456	Cidade C	Estado D
3	Rodrigues Barbosa	rodrigues@gmail.com	Rua C, 789, Cidade E, Estado F	2003-10-10	Rua C	789	Cidade E	Estado F 
*/

--
ALTER TABLE BTCTB001_USUARIO
	DROP COLUMN ED_USUARIO;

DESCRIBE BTCTB001_USUARIO; -- EE_USUARIO DELETADO