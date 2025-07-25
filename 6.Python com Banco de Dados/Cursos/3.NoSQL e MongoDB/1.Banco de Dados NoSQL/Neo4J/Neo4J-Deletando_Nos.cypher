-- DELETAR RELACIONAMENTO
MATCH (lula:Cliente {nome: "Lula Molusco"})-[relaciona:Bloqueado]->() DELETE relaciona

-- DELETAR NODE
MATCH (v_lula:Cliente {nome: "Lula Molusco"}) DELETE v_lula;        -- Nó Lula deletado

-- DELETE SPECIFIC NODE
-- MATCH (c:Cliente {nome: "Patrick Estrela"}) DELETE c;

-- DELETE ALL
-- MATCH (n) DETACH DELETE n;