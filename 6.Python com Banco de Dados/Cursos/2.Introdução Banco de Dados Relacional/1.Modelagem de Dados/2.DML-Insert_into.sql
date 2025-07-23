USE DB_BOOTCAMP;

INSERT INTO BTCTB001_USUARIO (NO_USUARIO, EE_USUARIO, ED_USUARIO, DT_NASCIMENTO) 
	VALUES 
    ("Ithallo Leandro R. Barbosa", "ithalloflu@gmail.com", "Rua A, 123, Cidade A, Estado B", '2004-10-01'),
    ("Leandro R. Barbosa", "leandro@gmail.com", "Rua B, 456, Cidade C, Estado D", '2005-01-10'),
    ("Rodrigues Barbosa", "rodrigues@gmail.com", "Rua C, 789, Cidade E, Estado F", '2003-10-10');

INSERT INTO BTCTB002_DESTINO (NO_DESTINO, DS_DESTINO) 
	VALUES 
    ("Guarujá", "Praia do Guarujá, localizada em Guarujá / São Paulo"),
    ("Cachoeira da Chapada", "Cachoeira da Chapada dos Veadeiros"),
    ("Catedral", "Catedral histórica, localizada em Brasília");

INSERT INTO BTCTB003_RESERVA (ID_USUARIO, ID_DESTINO, DT_RESERVA, IC_SITUACAO) -- IC_SITUACAO tem valor default (PE - Pendente)
	VALUES 
    (1, 1,DATE(NOW()), "PE"),
    (2, 2,DATE(NOW()), "CO"),
    (3, 3,DATE(NOW()), "CA");
