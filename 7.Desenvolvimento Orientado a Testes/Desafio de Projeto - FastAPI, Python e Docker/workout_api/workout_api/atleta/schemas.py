from typing import Annotated, Optional
from pydantic import Field, PositiveFloat
from pydantic_settings import BaseSettings
from workout_api.contrib.schemas import BaseSchema, OutMixin
from uuid import UUID


class Atleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do atleta', example='João', max_length=50)]
    cpf: Annotated[str, Field(description='CPF do atleta', example='12345678901', max_length=11)]
    idade: Annotated[int, Field(description='Idade do atleta', example=25)]
    peso: Annotated[PositiveFloat, Field(description='Peso do atleta', example=75.5)]
    altura: Annotated[PositiveFloat, Field(description='Altura do atleta', example=1.70)]
    sexo: Annotated[str, Field(description='Sexo do atleta', example='M', max_length=1)]
    categoria_id: Annotated[UUID, Field(description='ID da categoria')]
    centro_treinamento_id: Annotated[UUID, Field(description='ID do centro de treinamento')]


class AtletaIn(Atleta):
    pass


class AtletaOut(BaseSchema, OutMixin):
    nome: Annotated[str, Field(description='Nome do atleta', example='João')]
    # Response customizado - retorna nomes em vez de IDs
    centro_treinamento: Annotated[str, Field(description='Nome do centro de treinamento', example='Centro Olímpico')]
    categoria: Annotated[str, Field(description='Nome da categoria', example='Scale')]
    cpf: Annotated[str, Field(description='CPF do atleta', example='12345678901')]
    idade: Annotated[int, Field(description='Idade do atleta', example=25)]
    peso: Annotated[PositiveFloat, Field(description='Peso do atleta', example=75.5)]
    altura: Annotated[PositiveFloat, Field(description='Altura do atleta', example=1.70)]
    sexo: Annotated[str, Field(description='Sexo do atleta', example='M')]


class AtletaUpdate(BaseSchema):
    nome: Annotated[Optional[str], Field(None, description='Nome do atleta', example='João', max_length=50)]
    idade: Annotated[Optional[int], Field(None, description='Idade do atleta', example=25)]
    peso: Annotated[Optional[PositiveFloat], Field(None, description='Peso do atleta', example=75.5)]
    altura: Annotated[Optional[PositiveFloat], Field(None, description='Altura do atleta', example=1.70)]