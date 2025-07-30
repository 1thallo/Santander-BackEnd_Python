
use ("fenda_biquini")

db.createCollection("teste", {capped: true, max: 2, size: 2}); // Criando collection - "tabela"

// show collections; -> No mongosh

db.teste.insertOne({"nome": "Teste 1"});

/* 
{
  "acknowledged": true,
  "insertedId": {
    "$oid": "688970048b1a28ac6a0ef242"
  }
} 
*/

db.teste.find({});
/*
[
  {
    "_id": {
      "$oid": "688970048b1a28ac6a0ef242"
    },
    "nome": "Teste 1"
  }
]
*/

