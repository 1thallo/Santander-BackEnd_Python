-- UPDATE e DELETE
UPDATE BTCTB001_USUARIO
	SET EE_USUARIO = "rodrigues@hotmail.com"
    WHERE NO_USUARIO = "Rodrigues Barbosa";

SELECT * FROM BTCTB001_USUARIO;

--
DELETE FROM BTCTB002_DESTINO
WHERE NO_DESTINO LIKE "%Guaruj%";

SELECT * FROM BTCTB002_DESTINO;