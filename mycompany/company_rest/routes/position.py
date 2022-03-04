from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from company_rest import dto
from sqlalchemy import select
from company_rest.db.session import db_session, Session
from company_rest.db import tables

router = APIRouter(tags=["positions"])


@router.get("/positions", response_model=list[dto.Position], status_code=status.HTTP_200_OK)
def get_positions(
        db: Session = Depends(db_session)
) -> list[dto.Position]:
    result = select(tables.Position)
    result = db.scalars(result).all()
    return result


@router.post("/positions", status_code=status.HTTP_201_CREATED)
def create_position(
        request_body: dto.Position.New,
        db: Session = Depends(db_session)
) -> dto.Position:
    result = tables.Position(
        name=request_body.name
    )
    db.add(result)
    db.commit()
    db.refresh(result)
    return result


@router.get("/positions/{position_id}", response_model=dto.Position, status_code=status.HTTP_200_OK)
def get_position_id(
        position_id: UUID,
        db: Session = Depends(db_session)
) -> dto.Position:
    result = select(tables.Position).where(tables.Position.id == position_id)
    result = db.scalars(result).first()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Position {position_id} not found")
    return result


@router.put("/positions/{position_id}", status_code=status.HTTP_202_ACCEPTED)
def put_position_id(
        position_id: UUID,
        request_body: dto.Position.Update,
        db: Session = Depends(db_session)
) -> dto.Position.Update:
    result = select(tables.Position).where(tables.Position.id == position_id)
    result = db.scalars(result).first()
    result.name = request_body.name
    db.commit()
    db.refresh(result)
    return result


@router.delete("/positions/{position_id}", status_code=status.HTTP_200_OK)
def del_position_id(
        position_id: UUID,
        db: Session = Depends(db_session)
) -> dto.Position:
    result = select(tables.Position).where(tables.Position.id == position_id)
    result = db.scalars(result).first()
    if result:
        db.delete(result)
        db.commit()
        return result
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Position {position_id} not found")


@router.get("/positions/{position_id}/workers", response_model=list[dto.Worker])
def get_position_workers(
        position_id: UUID,
        db: Session = Depends(db_session)
) -> list[dto.Worker]:
    result = select(tables.Worker).where(tables.Worker.position_id == position_id)
    result = db.scalars(result).all()
    return result






