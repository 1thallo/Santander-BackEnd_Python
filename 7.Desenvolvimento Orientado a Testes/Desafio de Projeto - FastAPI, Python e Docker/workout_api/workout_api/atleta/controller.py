from datetime import datetime
from uuid import uuid4
from typing import Optional
from fastapi import APIRouter, Body, status, Depends, Query, HTTPException
from fastapi_pagination import Page, paginate
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
from pydantic import UUID4

from workout_api.atleta.schemas import AtletaIn, AtletaOut, AtletaUpdate
from workout_api.atleta.models import AtletaModel
from workout_api.categorias.models import CategoriaModel
from workout_api.centro_treinamento.models import CentroTreinamentoModel
from workout_api.contrib.dependencies import DatabaseDependency

router = APIRouter()

@router.post(
    '/', 
    summary='Criar novo atleta',
    status_code=status.HTTP_201_CREATED,
    response_model=AtletaOut
)
async def post(
    db_session: DatabaseDependency, 
    atleta_in: AtletaIn = Body(...)
):
    try:
        # Verificar se categoria existe
        categoria = await db_session.scalar(
            select(CategoriaModel).where(CategoriaModel.pk_id == atleta_in.categoria_id)
        )
        if not categoria:
            raise HTTPException(
                status_code=400, 
                detail=f"Categoria com id {atleta_in.categoria_id} não encontrada"
            )
        
        # Verificar se centro de treinamento existe
        centro = await db_session.scalar(
            select(CentroTreinamentoModel).where(CentroTreinamentoModel.pk_id == atleta_in.centro_treinamento_id)
        )
        if not centro:
            raise HTTPException(
                status_code=400, 
                detail=f"Centro de treinamento com id {atleta_in.centro_treinamento_id} não encontrado"
            )

        atleta_out = AtletaOut(id=uuid4(), **atleta_in.model_dump())
        atleta_model = AtletaModel(**atleta_out.model_dump())
        
        db_session.add(atleta_model)
        await db_session.commit()
        await db_session.refresh(atleta_model)
        
        return atleta_model
        
    except IntegrityError:
        await db_session.rollback()
        raise HTTPException(
            status_code=303,
            detail=f"Já existe um atleta cadastrado com o cpf: {atleta_in.cpf}"
        )

@router.get(
    '/', 
    summary='Consultar todos os atletas',
    status_code=status.HTTP_200_OK,
    response_model=Page[AtletaOut]
)
async def query(
    db_session: DatabaseDependency,
    nome: Optional[str] = Query(None, description="Filtrar por nome do atleta"),
    cpf: Optional[str] = Query(None, description="Filtrar por CPF do atleta")
) -> Page[AtletaOut]:
    # Construir query base com joins
    query = select(AtletaModel).join(CategoriaModel).join(CentroTreinamentoModel)
    
    # Aplicar filtros se fornecidos
    if nome:
        query = query.where(AtletaModel.nome.ilike(f"%{nome}%"))
    
    if cpf:
        query = query.where(AtletaModel.cpf == cpf)
    
    result = await db_session.execute(query)
    atletas = result.scalars().all()
    
    # Converter para response customizado
    atletas_out = [
        AtletaOut(
            id=atleta.pk_id,
            nome=atleta.nome,
            centro_treinamento=atleta.centro_treinamento.nome,
            categoria=atleta.categoria.nome,
            cpf=atleta.cpf,
            idade=atleta.idade,
            peso=atleta.peso,
            altura=atleta.altura,
            sexo=atleta.sexo
        )
        for atleta in atletas
    ]
    
    return paginate(atletas_out)

@router.get(
    '/{atleta_id}', 
    summary='Consulta um atleta por id',
    status_code=status.HTTP_200_OK,
    response_model=AtletaOut
)
async def get(atleta_id: UUID4, db_session: DatabaseDependency) -> AtletaOut:
    atleta = await db_session.scalar(
        select(AtletaModel)
        .join(CategoriaModel)
        .join(CentroTreinamentoModel)
        .where(AtletaModel.pk_id == atleta_id)
    )
    
    if not atleta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f'Atleta não encontrado no id: {atleta_id}'
        )
    
    return AtletaOut(
        id=atleta.pk_id,
        nome=atleta.nome,
        centro_treinamento=atleta.centro_treinamento.nome,
        categoria=atleta.categoria.nome,
        cpf=atleta.cpf,
        idade=atleta.idade,
        peso=atleta.peso,
        altura=atleta.altura,
        sexo=atleta.sexo
    )
