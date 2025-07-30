-- =====================================================
--           CASSANDRA QUERY LANGUAGE (CQL) - ASTRA DB
-- =====================================================
-- Arquivo: Cassandra-Create.cql
-- Objetivo: Comandos para DataStax Astra DB
-- Data: 2025-01-17
-- IMPORTANTE: No Astra, keyspaces são criados via interface web
-- Comandos CQL é bastante parecido com comando SQL
-- =====================================================

-- 1. PRIMEIRO: Execute este comando para ver keyspaces disponíveis
-- DESCRIBE KEYSPACES;

-- 2. Use o keyspace (substitua pelo nome real do seu Astra)
-- USE default_keyspace;  -- MUDE ESTE NOME!

-- 3. Criar tabela de personagens da Fenda do Biquini
CREATE TABLE IF NOT EXISTS personagens (
    id UUID PRIMARY KEY,
    nome TEXT,
    profissao TEXT,
    endereco TEXT,
    telefone TEXT,
    data_cadastro TIMESTAMP
);

-- 4. Inserir personagens
INSERT INTO personagens (id, nome, profissao, endereco, telefone, data_cadastro)
VALUES (uuid(), 'Bob Esponja', 'Cozinheiro', 'Casa do Abacaxi', '555-KRUSTY', toTimestamp(now()));

INSERT INTO personagens (id, nome, profissao, endereco, telefone, data_cadastro)
VALUES (uuid(), 'Patrick Estrela', 'Desempregado', 'Pedra Rosa', '555-STAR', toTimestamp(now()));

INSERT INTO personagens (id, nome, profissao, endereco, telefone, data_cadastro)
VALUES (uuid(), 'Lula Molusco', 'Músico/Caixa', 'Casa da Ilha', '555-SQUID', toTimestamp(now()));

-- 5. Consultas
-- SELECT * FROM personagens;
-- SELECT nome, profissao FROM personagens;
-- SELECT * FROM personagens WHERE nome = 'Bob Esponja' ALLOW FILTERING;