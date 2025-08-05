"""
Script para cadastrar produtos com preços diferentes para testar os filtros
"""
import asyncio
from decimal import Decimal
from store.usecases.product import ProductUsecase
from store.schemas.product import ProductIn


async def seed_products():
    """Cadastra produtos com preços diferentes para testar filtros"""
    usecase = ProductUsecase()
    
    products = [
        ProductIn(
            name="iPhone 13",
            quantity=10,
            price=Decimal("4500.00"),
            status=True
        ),
        ProductIn(
            name="iPhone 14",
            quantity=8,
            price=Decimal("6000.00"),
            status=True
        ),
        ProductIn(
            name="iPhone 15",
            quantity=5,
            price=Decimal("7500.00"),
            status=True
        ),
        ProductIn(
            name="MacBook Air",
            quantity=3,
            price=Decimal("8500.00"),
            status=True
        ),
        ProductIn(
            name="iPad Pro",
            quantity=12,
            price=Decimal("3000.00"),
            status=True
        ),
        ProductIn(
            name="Apple Watch",
            quantity=20,
            price=Decimal("2500.00"),
            status=True
        ),
    ]
    
    for product in products:
        try:
            result = await usecase.create(body=product)
            print(f"✅ Produto criado: {result.name} - R$ {result.price}")
        except Exception as e:
            print(f"❌ Erro ao criar produto {product.name}: {e}")


if __name__ == "__main__":
    print("Cadastrando produtos com preços diferentes...")
    asyncio.run(seed_products())
    print("Concluído!")
    print("\nTeste os filtros:")
    print("GET /products/?min_price=5000&max_price=8000")
    print("Deve retornar: iPhone 14 (6000) e iPhone 15 (7500)")
