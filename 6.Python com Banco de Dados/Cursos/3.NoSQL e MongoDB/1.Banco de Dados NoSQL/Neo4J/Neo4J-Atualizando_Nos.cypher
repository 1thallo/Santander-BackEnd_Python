-- Atualizando nós
MATCH (variavel:Cliente {nome:"Patrick Estrela"}) 
SET variavel.hobbies = ["Comer hamburguer de siri"];

-- ATUALIZANDO PROPRIEDADES DE RELACIONAMENTOS

-- Adicionar propriedades ao relacionamento de Amizade
MATCH (bob:Cliente {nome: "Bob Esponja"})-[amizade:Amizade]->(patrick:Cliente {nome: "Patrick Estrela"})
SET amizade.desde = "2010-05-01",
    amizade.nivel = "melhor amigo",
    amizade.atividades = ["caçar água-viva", "fazer travessuras"];

-- Adicionar propriedades ao relacionamento de Bloqueio
MATCH (lula:Cliente {nome: "Lula Molusco"})-[bloqueio:Bloqueado]->(patrick:Cliente {nome: "Patrick Estrela"})
SET bloqueio.motivo = "muito barulhento",
    bloqueio.data_bloqueio = "2023-12-15",
    bloqueio.nivel_irritacao = 10;

-- Atualizar apenas uma propriedade específica
MATCH ()-[amizade:Amizade]->()
SET amizade.ultimo_encontro = "2025-01-17";

-- Incrementar valor numérico
MATCH (lula:Cliente {nome: "Lula Molusco"})-[bloqueio:Bloqueado]->()
SET bloqueio.nivel_irritacao = bloqueio.nivel_irritacao + 1;

-- Adicionar item a array existente
MATCH (bob:Cliente {nome: "Bob Esponja"})-[amizade:Amizade]->()
SET amizade.atividades = amizade.atividades + ["fazer bolhas"];