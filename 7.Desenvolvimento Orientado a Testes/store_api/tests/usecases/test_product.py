from typing import List
from uuid import UUID
from datetime import datetime

import pytest
from store.core.exceptions import NotFoundException, InsertionException
from store.schemas.product import ProductOut, ProductUpdateOut, ProductUpdate
from store.usecases.product import product_usecase


async def test_usecases_create_should_return_success(product_in):
    result = await product_usecase.create(body=product_in)

    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 14 Pro Max"


async def test_usecases_get_should_return_success(product_inserted):
    result = await product_usecase.get(id=product_inserted.id)

    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 14 Pro Max"


async def test_usecases_get_should_not_found():
    with pytest.raises(NotFoundException) as err:
        await product_usecase.get(id=UUID("1e4f214e-85f7-461a-89d0-a751a32e3bb9"))

    assert (
        err.value.message
        == "Product not found with filter: 1e4f214e-85f7-461a-89d0-a751a32e3bb9"
    )


@pytest.mark.usefixtures("products_inserted")
async def test_usecases_query_should_return_success():
    result = await product_usecase.query()

    assert isinstance(result, List)
    assert len(result) > 1


@pytest.mark.usefixtures("products_inserted")
async def test_usecases_query_with_price_filter_should_return_success():
    # Testa filtro de preço entre 5000 e 8000
    result = await product_usecase.query(min_price=5000, max_price=8000)

    assert isinstance(result, List)
    # Verifica se todos os produtos retornados estão na faixa de preço
    for product in result:
        assert 5000 < float(product.price) < 8000


async def test_usecases_update_should_return_success(product_up, product_inserted):
    product_up.price = "7.500"
    result = await product_usecase.update(id=product_inserted.id, body=product_up)

    assert isinstance(result, ProductUpdateOut)


async def test_usecases_update_should_update_timestamp(product_inserted):
    # Testa se updated_at é atualizado automaticamente
    update_data = ProductUpdate(quantity=10)
    result = await product_usecase.update(id=product_inserted.id, body=update_data)
    
    assert isinstance(result, ProductUpdateOut)
    assert result.updated_at > product_inserted.updated_at


async def test_usecases_update_should_not_found():
    with pytest.raises(NotFoundException) as err:
        update_data = ProductUpdate(quantity=10)
        await product_usecase.update(id=UUID("1e4f214e-85f7-461a-89d0-a751a32e3bb9"), body=update_data)

    assert "Produto não encontrado para atualização" in err.value.message


async def test_usecases_delete_should_return_success(product_inserted):
    result = await product_usecase.delete(id=product_inserted.id)

    assert result is True


async def test_usecases_delete_should_not_found():
    with pytest.raises(NotFoundException) as err:
        await product_usecase.delete(id=UUID("1e4f214e-85f7-461a-89d0-a751a32e3bb9"))

    assert (
        err.value.message
        == "Product not found with filter: 1e4f214e-85f7-461a-89d0-a751a32e3bb9"
    )
