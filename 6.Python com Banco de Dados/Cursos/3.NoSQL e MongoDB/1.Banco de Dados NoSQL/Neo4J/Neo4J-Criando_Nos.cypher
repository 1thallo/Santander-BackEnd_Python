/*
================================================================================
                        NEO4J - BANCO DE DADOS DE GRAFOS
================================================================================

ESTRUTURA DO GRAFO:
┌─────────────┐                    ┌─────────────┐
│ Lula Molusco│ ──[Bloqueado]──▶  │Patrick Estrela│
└─────────────┘                    └─────────────┘

        ┌─────────────┐
        │ Bob Esponja │ (nó isolado)
        └─────────────┘

RELACIONAMENTOS:
- Lula Molusco bloqueia Patrick Estrela
- Bob Esponja não possui relacionamentos

================================================================================
*/

-- CREATE NODES
CREATE (:Cliente {
    nome: "Bob Esponja",
    idade: 20,
    hobbies: [
        "Caçar agua-viva",
        "Comer hamburguer de siri"
    ]
})

-- SELECT
MATCH (bob_esponja) RETURN bob_esponja;

-- RELACIONAMENTO (NODE)
CREATE (:Cliente {
    nome: "Lula Molusco",
    idade: 40,
    hobbies: ['Tocar Clarinete']})
    -[:Bloqueado]->                     -- Relacionamento com a label Bloqueado
    (:Cliente {
        nome: "Patrick Estrela",
        hobbies: ['Caçar agua-viva']
    })

-- CRIANDO RELACIONAMENTO COM NÓS JÁ EXISTENTES
MATCH (z:Cliente {nome: "Bob Esponja"}), (x:Cliente {nome:"Patrick Estrela"}) 
CREATE (z)-[:Amizade]->(x);
