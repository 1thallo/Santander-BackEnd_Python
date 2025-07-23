SELECT * FROM BTCTB001_USUARIO;

SELECT * FROM BTCTB002_DESTINO;

SELECT * FROM BTCTB003_RESERVA;

-- WHERE
SELECT * FROM BTCTB001_USUARIO
WHERE ID_USUARIO = 1
OR NO_USUARIO LIKE "%R.%"

/*
1	Ithallo Leandro R. Barbosa	ithalloflu@gmail.com	Rua A, 123, Cidade A, Estado B	2004-10-01
2	Leandro R. Barbosa	leandro@gmail.com	Rua B, 456, Cidade C, Estado D	2005-01-10
*/