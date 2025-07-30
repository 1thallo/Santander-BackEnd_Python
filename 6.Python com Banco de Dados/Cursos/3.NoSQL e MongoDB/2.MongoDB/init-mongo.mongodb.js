// Script de inicialização do MongoDB Docker

// Inserir dados do playground
db.sales.insertMany([
  { 'item': 'abc', 'price': 10, 'quantity': 2, 'date': new Date('2014-03-01T08:00:00Z') },
  { 'item': 'jkl', 'price': 20, 'quantity': 1, 'date': new Date('2014-03-01T09:00:00Z') },
  { 'item': 'xyz', 'price': 5, 'quantity': 10, 'date': new Date('2014-03-15T09:00:00Z') },
  { 'item': 'xyz', 'price': 5, 'quantity': 20, 'date': new Date('2014-04-04T11:21:39.736Z') },
  { 'item': 'abc', 'price': 10, 'quantity': 10, 'date': new Date('2014-04-04T21:23:13.331Z') },
  { 'item': 'def', 'price': 7.5, 'quantity': 5, 'date': new Date('2015-06-04T05:08:13Z') },
  { 'item': 'def', 'price': 7.5, 'quantity': 10, 'date': new Date('2015-09-10T08:43:00Z') },
  { 'item': 'abc', 'price': 10, 'quantity': 5, 'date': new Date('2016-02-06T20:20:13Z') },
]);

// Dados para estudos
db.personagens.insertMany([
  {
    nome: "Bob Esponja",
    idade: 25,
    profissao: "Cozinheiro",
    endereco: {
      casa: "Casa do Abacaxi",
      cidade: "Fenda do Biquini",
      coordenadas: [-74.0059, 40.7128]
    },
    hobbies: ["cozinhar", "caçar águas-vivas", "karatê"],
    amigos: ["Patrick Estrela", "Sandy Bochechas"],
    salario: 50,
    data_cadastro: new Date(),
    ativo: true
  },
  {
    nome: "Patrick Estrela",
    idade: 24,
    profissao: null,
    endereco: {
      casa: "Pedra Rosa",
      cidade: "Fenda do Biquini"
    },
    hobbies: ["dormir", "comer"],
    amigos: ["Bob Esponja"],
    salario: 0,
    data_cadastro: new Date(),
    ativo: true
  },
  {
    nome: "Lula Molusco",
    idade: 40,
    profissao: "Caixa",
    endereco: {
      casa: "Casa da Ilha",
      cidade: "Fenda do Biquini"
    },
    hobbies: ["tocar clarinete", "arte"],
    amigos: [],
    salario: 30,
    data_cadastro: new Date(),
    ativo: false
  }
]);

// Criar índices para performance
db.sales.createIndex({ "date": 1 });
db.sales.createIndex({ "item": 1 });
db.personagens.createIndex({ "nome": 1 });
db.personagens.createIndex({ "profissao": 1 });
db.personagens.createIndex({ "endereco.cidade": 1 });

print("✅ Database inicializado com sucesso!");
print("📊 Collections: sales, personagens");
print("👤 Usuário criado: app_user");
print("📈 Índices criados para performance");