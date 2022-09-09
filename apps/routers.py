import typing

from fastapi import APIRouter, Depends

from apps.models import file_table
from apps.schemas import FileIn, FileOut, Message
from db import database

router = APIRouter(tags=['files'])


@router.post('/', response_model=FileOut)
async def create(r: FileIn):  # = Depends()):
    query = file_table.insert().values(
        **r.dict()
    )
    record_id = await database.execute(query)
    query = file_table.select().where(file_table.c.id == record_id)
    # query = register.select().where(register.id == record_id)
    row = await database.fetch_one(query)
    return {**row}


# @router.get('/{name}', response_model=FileOut | {})
@router.get('/{name}')
async def get_one_by_name(name):
    try:
        query = file_table.select().where(file_table.c.name == name)
        row = await database.fetch_one(query)
        return row
    except:
        return {}


@router.get('/', response_model=typing.List[FileOut])
async def get_all():
    query = file_table.select()
    rows = await database.fetch_all(query)
    return rows


@router.put('/{id}', response_model=FileOut)
async def update(id: int, r: FileIn = Depends()):
    query = file_table.update().where(file_table.c.id == id).values(
        **r.dict()
    )
    record_id = await database.execute(query)
    print(record_id)
    query = file_table.select().where(file_table.c.id == record_id)
    row = await database.fetch_one(query)
    print(row)
    # return {**row}


@router.delete('/{id}')
async def delete(id: int):
    query = file_table.delete().where(file_table.c.id == id)
    await database.execute(query)
    return Message(message='Successfully deleted')
