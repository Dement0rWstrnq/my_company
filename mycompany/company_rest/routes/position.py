from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from company_rest import dto
from company_rest.db.session import db_session, Session
from company_rest.db import tables

router = APIRouter(tags=["positions"])


@router.get("/positions", response_model=list[dto.Position])
def fetch_positions(
        db: Session = Depends(db_session)
) -> list[dto.Position]:
    result = db.select(tables.Position)
    result = db.scalars(result).all()
    return result
