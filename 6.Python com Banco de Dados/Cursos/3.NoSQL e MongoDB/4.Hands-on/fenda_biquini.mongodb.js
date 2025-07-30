use ("fenda_biquini")

db.clientes.insertMany([{"nome": "Bob Esponja", "idade": 20}, {"nome": "Patrick"}]);

// {"acknowledged": true,"insertedIds": {"0": {"$oid": "6889717a6ceba16e6a17dbc2"},"1": {"$oid": "6889717a6ceba16e6a17dbc3"}}}

db.clientes.find({});

// [{_id: ObjectId('6889717a6ceba16e6a17dbc2'),nome: 'Bob Esponja',idade: 20},{ _id: ObjectId('6889717a6ceba16e6a17dbc3'), nome: 'Patrick' }]

// insertOne() para inserir
db.clientes.insertOne({
  nome: "Sandy Bochechas", 
  idade: 23,
  profissao: "Cientista"
});

// insertMany() para múltiplos
db.clientes.insertMany([
  { nome: "Lula Molusco", idade: 40, profissao: "Caixa" },
  { nome: "Sr. Siriguejo", idade: 50, profissao: "Gerente" }
]);

// updateOne() para atualizar
db.clientes.updateOne(
  { _id: ObjectId("68898217898fe1fe48b85649") },
  { 
    $set: { 
      nome: "Patrick Estrela",
      idade: 24,
      profissao: "Desempregado"
    }
  }
);

// replaceOne() para substituir documento completo
db.clientes.replaceOne(
  { _id: ObjectId("6889717a6ceba16e6a17dbc3") },
  {
    nome: "Patrick Estrela",
    idade: 24,
    profissao: "Desempregado",
    endereco: "Pedra Rosa"
  }
);

// =====================================================
//                 CONSULTAS COM $IN
// =====================================================

console.log("=== OPERADOR $IN ===");

// buscar clientes com nomes específicos
db.clientes.find({ 
  nome: { $in: ["Bob Esponja", "Patrick Estrela", "Sandy Bochechas"] } 
});

// buscar clientes com idades específicas
db.clientes.find({ 
  idade: { $in: [20, 23, 24] } 
});

// buscar clientes com profissões específicas
db.clientes.find({ 
  profissao: { $in: ["Cozinheiro", "Cientista", "Desempregado"] } 
});

// =====================================================
//                 CONSULTAS COM $OR
// =====================================================

console.log("\n=== OPERADOR $OR ===");

// buscar clientes que são jovens OU têm profissão específica
db.clientes.find({
  $or: [
    { idade: { $lt: 25 } },
    { profissao: "Cientista" }
  ]
});

// buscar clientes que são Bob Esponja OU Patrick Estrela
db.clientes.find({
  $or: [
    { nome: "Bob Esponja" },
    { nome: "Patrick Estrela" }
  ]
});

// combinar $or com outras condições
db.clientes.find({
  idade: { $gte: 20 },  // E idade >= 20
  $or: [
    { profissao: "Cozinheiro" },
    { profissao: "Cientista" }
  ]
});

// =====================================================
//              CONSULTAS COM $LT e $LTE
// =====================================================

console.log("\n=== OPERADORES $LT e $LTE ===");

// $lt - menor que (less than)
db.clientes.find({ idade: { $lt: 25 } });  // idade < 25

// $lte - menor ou igual (less than or equal)
db.clientes.find({ idade: { $lte: 24 } }); // idade <= 24

// $gt - maior que (greater than)
db.clientes.find({ idade: { $gt: 30 } });  // idade > 30

// $gte - maior ou igual (greater than or equal)
db.clientes.find({ idade: { $gte: 40 } }); // idade >= 40

// combinar operadores de comparação
db.clientes.find({ 
  idade: { $gte: 20, $lt: 30 } // 20 <= idade < 30
});

// =====================================================
//                 UPDATE MANY
// =====================================================

console.log("\n=== OPERADOR updateMany ===");

// atualizar multiplos documentos - Adicionar campo categoria
db.clientes.updateMany(
  { idade: { $lt: 30 } },  // condição: idade < 30
  { 
    $set: { 
      categoria: "jovem",
      data_atualizacao: new Date()
    }
  }
);

// atualizar todos os clientes sem profissão
db.clientes.updateMany(
  { profissao: { $exists: false } },  // Sem campo profissão
  { 
    $set: { 
      profissao: "Não informado",
      status: "incompleto"
    }
  }
);

// incrementar idade de todos os clientes em 1 ano
db.clientes.updateMany(
  {},  // Condição vazia = todos os documentos
  { 
    $inc: { idade: 1 },  // Incrementar idade
    $set: { ultimo_aniversario: new Date() }
  }
);

// adicionar hobby para clientes da Fenda do Biquini
db.clientes.updateMany(
  { nome: { $in: ["Bob Esponja", "Patrick Estrela", "Sandy Bochechas"] } },
  { 
    $addToSet: { 
      hobbies: "viver na Fenda do Biquini" 
    }
  }
);

// =====================================================
//                 VERIFICAR RESULTADOS
// =====================================================

console.log("\n=== RESULTADOS FINAIS ===");

// contar documentos por categoria
console.log("Jovens:", db.clientes.countDocuments({ idade: { $lt: 30 } }));
console.log("Adultos:", db.clientes.countDocuments({ idade: { $gte: 30 } }));
console.log("Com profissão:", db.clientes.countDocuments({ profissao: { $exists: true, $ne: "Não informado" } }));

// mostrar todos os documentos atualizados
db.clientes.find({}).forEach(function(doc) {
  printjson(doc);
});

// =====================================================
//              AGREGAÇÕES COM OPERADORES
// =====================================================

console.log("\n=== AGREGAÇÕES ===");

// Agrupar por faixa etária
db.clientes.aggregate([
  {
    $addFields: {
      faixa_etaria: {
        $switch: {
          branches: [
            { case: { $lt: ["$idade", 25] }, then: "Jovem" },
            { case: { $lt: ["$idade", 40] }, then: "Adulto" },
            { case: { $gte: ["$idade", 40] }, then: "Senior" }
          ],
          default: "Indefinido"
        }
      }
    }
  },
  {
    $group: {
      _id: "$faixa_etaria",
      count: { $sum: 1 },
      idade_media: { $avg: "$idade" },
      nomes: { $push: "$nome" }
    }
  },
  {
    $sort: { count: -1 }
  }
]);
