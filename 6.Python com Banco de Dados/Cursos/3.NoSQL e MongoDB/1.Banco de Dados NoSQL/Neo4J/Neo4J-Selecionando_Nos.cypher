/*
================================================================================
                    NEO4J CYPHER QUERY LANGUAGE (CQL)
================================================================================

ATENÇÃO: Este arquivo contém comandos CYPHER, não SQL tradicional.
- Cypher é a linguagem de consulta específica do Neo4j
- Sintaxe e semântica diferentes do SQL relacional
- Focado em grafos (nós e relacionamentos)

EXTENSÃO RECOMENDADA: .cypher ou .cql
================================================================================
*/

-- Ver todos os relacionamentos
MATCH (a)-[r]->(b) RETURN a.nome, type(r), b.nome;

-- Ver relacionamentos do Patrick (quem se relaciona com ele)
MATCH ()-[r]->(patrick:Cliente {nome: "Patrick Estrela"}) 
RETURN r, patrick;

-- Ver relacionamentos do Bob (com quem ele se relaciona)
MATCH (bob:Cliente {nome: "Bob Esponja"})-[r]->() 
RETURN bob, r;

-- SELECT ALL NODES
MATCH (n) RETURN n;

-- SELECT SPECIFIC NODES
MATCH (c:Cliente) RETURN c;

-- SELECT RELATIONSHIPS
MATCH (a)-[r:Bloqueado]->(b) RETURN a, r, b;

-- SELECT BY PROPERTY
MATCH (c:Cliente {nome: "Bob Esponja"}) RETURN c;

-- SELECT BY AGE
MATCH (c:Cliente) WHERE c.idade > 30 RETURN c;

-- COUNT NODES
MATCH (c:Cliente) RETURN count(c);