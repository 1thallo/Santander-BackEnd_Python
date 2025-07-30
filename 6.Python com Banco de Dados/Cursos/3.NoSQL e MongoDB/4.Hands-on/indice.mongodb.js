use("fenda_biquini");

// =====================================================
//                 PREPARAR DADOS DE TESTE
// =====================================================

db.produtos.drop();

// produtos de exemplo
db.produtos.insertMany([
  {
    nome: "Hambúrguer Siri",
    categoria: "comida",
    preco: 2.50,
    ingredientes: ["pão", "hambúrguer", "alface", "tomate"],
    restaurante: "Siri Cascudo",
    avaliacao: 4.9,
    vendas: 15000,
    data_criacao: new Date("2020-01-15"),
    ativo: true,
    tags: ["popular", "barato", "delicioso"]
  },
  {
    nome: "Pizza de Algas",
    categoria: "comida",
    preco: 8.90,
    ingredientes: ["massa", "algas", "queijo", "molho"],
    restaurante: "Pizza Palace",
    avaliacao: 4.2,
    vendas: 3200,
    data_criacao: new Date("2021-05-20"),
    ativo: true,
    tags: ["vegetariano", "saudável"]
  },
  {
    nome: "Refrigerante Kelp",
    categoria: "bebida",
    preco: 1.50,
    ingredientes: ["água", "kelp", "açúcar"],
    restaurante: "Loja do Sr. Siriguejo",
    avaliacao: 3.8,
    vendas: 8500,
    data_criacao: new Date("2019-03-10"),
    ativo: true,
    tags: ["refrescante", "natural"]
  },
  {
    nome: "Sorvete de Plâncton",
    categoria: "sobremesa",
    preco: 3.75,
    ingredientes: ["leite", "açúcar", "plâncton", "essência"],
    restaurante: "Sorveteria Frozen",
    avaliacao: 4.6,
    vendas: 5800,
    data_criacao: new Date("2022-07-08"),
    ativo: false,
    tags: ["doce", "cremoso", "especial"]
  }
]);

console.log("=== DADOS INSERIDOS ===");
console.log("Total produtos:", db.produtos.countDocuments());

// =====================================================
//                 ÍNDICES SIMPLES (SINGLE FIELD)
// =====================================================

console.log("\n=== CRIANDO ÍNDICES SIMPLES ===");

// 1. Índice simples ascendente no campo 'nome'
db.produtos.createIndex({ nome: 1 });
console.log("✅ Índice criado: nome (ascendente)");

// 2. Índice simples descendente no campo 'preco'
db.produtos.createIndex({ preco: -1 });
console.log("✅ Índice criado: preco (descendente)");

// 3. Índice no campo 'categoria'
db.produtos.createIndex({ categoria: 1 });
console.log("✅ Índice criado: categoria");

// 4. Índice no campo 'avaliacao'
db.produtos.createIndex({ avaliacao: -1 });
console.log("✅ Índice criado: avaliacao (descendente)");

// =====================================================
//                 ÍNDICES COMPOSTOS (COMPOUND)
// =====================================================

console.log("\n=== CRIANDO ÍNDICES COMPOSTOS ===");

// 1. Índice composto: categoria + preco
db.produtos.createIndex({ categoria: 1, preco: 1 });
console.log("✅ Índice composto criado: categoria + preco");

// 2. Índice composto: restaurante + avaliacao (desc)
db.produtos.createIndex({ restaurante: 1, avaliacao: -1 });
console.log("✅ Índice composto criado: restaurante + avaliacao");

// 3. Índice composto triplo: categoria + ativo + vendas
db.produtos.createIndex({ categoria: 1, ativo: 1, vendas: -1 });
console.log("✅ Índice composto triplo criado: categoria + ativo + vendas");

// =====================================================
//                 LISTAR ÍNDICES
// =====================================================

console.log("\n=== ÍNDICES CRIADOS ===");
db.produtos.getIndexes().forEach(function(index) {
  console.log("Índice:", JSON.stringify(index.key), "| Nome:", index.name);
});

// =====================================================
//                 TESTAR PERFORMANCE DOS ÍNDICES
// =====================================================

console.log("\n=== TESTANDO PERFORMANCE ===");

// 1. Busca simples com índice
console.log("\n--- Query 1: Busca por nome ---");
console.log("Query: db.produtos.find({ nome: 'Hambúrguer Siri' })");
db.produtos.find({ nome: "Hambúrguer Siri" }).explain("executionStats");

// 2. Busca com índice composto
console.log("\n--- Query 2: Busca por categoria + preço ---");
console.log("Query: db.produtos.find({ categoria: 'comida', preco: { $lte: 5 } })");
db.produtos.find({ categoria: "comida", preco: { $lte: 5 } }).explain("executionStats");

// 3. Busca com ordenação
console.log("\n--- Query 3: Busca ordenada por avaliação ---");
console.log("Query: db.produtos.find().sort({ avaliacao: -1 })");
db.produtos.find().sort({ avaliacao: -1 }).explain("executionStats");

// =====================================================
//                 EXEMPLOS DE QUERIES OTIMIZADAS
// =====================================================

console.log("\n=== QUERIES OTIMIZADAS COM ÍNDICES ===");

// 1. Busca produtos ativos de uma categoria, ordenados por vendas
db.produtos.find({ 
  categoria: "comida", 
  ativo: true 
}).sort({ vendas: -1 }).limit(5);

// 2. Busca produtos por faixa de preço
db.produtos.find({ 
  preco: { $gte: 2.00, $lte: 5.00 } 
}).sort({ preco: 1 });

// 3. Busca produtos de um restaurante com boa avaliação
db.produtos.find({ 
  restaurante: "Siri Cascudo", 
  avaliacao: { $gte: 4.5 } 
}).sort({ avaliacao: -1 });

// 4. Busca produtos que contêm ingrediente específico
db.produtos.find({ 
  ingredientes: "hambúrguer" 
});


// =====================================================
//                 ANÁLISE DE PERFORMANCE
// =====================================================

console.log("\n=== ANÁLISE DE PERFORMANCE ===");

// medir tempo de execução
function medirPerformance(query, descricao) {
  console.log(`\n--- ${descricao} ---`);
  const inicio = new Date();
  const resultado = query();
  const fim = new Date();
  const tempo = fim - inicio;
  console.log(`⏱️ Tempo: ${tempo}ms`);
  return resultado;
}

// Comparar queries com e sem índice
medirPerformance(
  () => db.produtos.find({ categoria: "comida" }).toArray(),
  "Busca por categoria (com índice)"
);

medirPerformance(
  () => db.produtos.find({ categoria: "comida", preco: { $lte: 5 } }).toArray(),
  "Busca composta categoria + preço (com índice)"
);

// =====================================================
//                 MANUTENÇÃO DE ÍNDICES
// =====================================================

console.log("\n=== MANUTENÇÃO DE ÍNDICES ===");

// Estatísticas dos índices
console.log("\nEstatísticas dos índices:");
db.produtos.stats().indexSizes;

// Verificar uso dos índices
console.log("\nVerificar uso de índices específicos:");
db.produtos.find({ categoria: "comida" }).hint({ categoria: 1 }).explain("executionStats");


// =====================================================
//                 MELHORES PRÁTICAS
// =====================================================

console.log("\n=== MELHORES PRÁTICAS ===");

console.log(`
RESUMO DE MELHORES PRÁTICAS:

✅ DO'S (Faça):
1. Crie índices para campos frequentemente consultados
2. Use índices compostos para queries com múltiplos campos
3. Ordene campos do mais seletivo para o menos seletivo
4. Monitore performance com .explain()
5. Use índices sparse para campos opcionais
6. Implemente índices TTL para dados temporários

❌ DON'TS (Não faça):
1. Não crie índices desnecessários (impacta writes)
2. Não ignore a ordem em índices compostos
3. Não use muitos índices em collections com writes frequentes
4. Não esqueça de remover índices não utilizados
5. Não crie índices em campos com poucos valores únicos

TIPOS DE ÍNDICES:
- Single Field: { campo: 1 }
- Compound: { campo1: 1, campo2: -1 }
- Text: { campo: "text" }
- Multikey: automático para arrays
- TTL: { data: 1 }, { expireAfterSeconds: 3600 }
- Sparse: { campo: 1 }, { sparse: true }
- Unique: { campo: 1 }, { unique: true }
`);
