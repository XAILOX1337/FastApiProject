
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated

from core.models.product import Product
from . import crud
from fastapi import Depends, HTTPException, Path, status

from core.models import db_helper


async def product_by_id(
    product_id: Annotated[int, Path], 
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
    ) -> Product:
    product = await crud.get_product(product_id= product_id,session=session) 
    if product:
        return product

    raise HTTPException(
        status_code= status.HTTP_404_NOT_FOUND,
        detail = f"Product {product_id} not found!"
    )
