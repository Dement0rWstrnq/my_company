from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from company_rest import dto
from sqlalchemy import select
from company_rest.db.session import db_session, Session
from company_rest.db import tables

router = APIRouter(tags=["workers"])


@router.get("/workers", response_model=list[dto.Worker], status_code=status.HTTP_200_OK)
def get_workers(
        db: Session = Depends(db_session)
) -> list[dto.Worker]:
    result = select(tables.Worker)
    result = db.scalars(result).all()
    return result


@router.post("/workers", status_code=status.HTTP_201_CREATED)
def post_worker(
    request_body: dto.Worker.New,
    db: Session = Depends(db_session)
) -> dto.Worker:
    result = tables.Worker(
        name=request_body.name,
        surname=request_body.surname,
        department_id=request_body.department_id,
        position_id=request_body.position_id,
        skills=request_body.skills
    )
    db.add(result)
    db.commit()
    db.refresh(result)
    return result


@router.get("/workers/{worker_id}", response_model=dto.Worker, status_code=status.HTTP_200_OK)
def get_worker_id(
        worker_id: UUID,
        db: Session = Depends(db_session)
) -> dto.Worker:
    result = select(tables.Worker).where(tables.Worker.id == worker_id)
    result = db.scalars(result).first()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Worker {worker_id} not found")
    return result


@router.put("/workers/{worker_id}", status_code=status.HTTP_202_ACCEPTED)
def put_position_id(
        worker_id: UUID,
        request_body: dto.Worker.Update,
        db: Session = Depends(db_session)
) -> dto.Worker.Update:
    result = select(tables.Worker).where(tables.Worker.id == worker_id)
    result = db.scalars(result).first()
    result.name = request_body.name
    result.surname = request_body.surname
    result.department_id = request_body.department_id
    result.position_id = request_body.position_id
    result.skills = request_body.skills
    db.commit()
    db.refresh(result)
    return result


@router.delete("/workers/{worker_id}", status_code=status.HTTP_200_OK)
def del_position_id(
        worker_id: UUID,
        db: Session = Depends(db_session)
) -> dto.Worker:
    result = select(tables.Worker).where(tables.Worker.id == worker_id)
    result = db.scalars(result).first()
    if result:
        db.delete(result)
        db.commit()
        return result
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Worker {worker_id} not found")
