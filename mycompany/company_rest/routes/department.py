from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from company_rest import dto
from sqlalchemy import select
from company_rest.db.session import db_session, Session
from company_rest.db import tables

router = APIRouter(tags=["departments"])


@router.get(
    "/departments", response_model=list[dto.Department], status_code=status.HTTP_200_OK
)
def get_departments(db: Session = Depends(db_session)) -> list[dto.Department]:
    result = select(tables.Department)
    result = db.scalars(result).all()
    return result


@router.post("/departments", status_code=status.HTTP_201_CREATED)
def create_department(
    request_body: dto.Department.New, db: Session = Depends(db_session)
) -> dto.Department:
    result = tables.Department(name=request_body.name)
    db.add(result)
    db.commit()
    db.refresh(result)
    return result


@router.get(
    "/departments/{department_id}",
    response_model=dto.Department,
    status_code=status.HTTP_200_OK,
)
def get_department_id(
    department_id: UUID, db: Session = Depends(db_session)
) -> dto.Department:
    result = select(tables.Department).where(tables.Department.id == department_id)
    result = db.scalars(result).first()
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Department {department_id} not found",
        )
    return result


@router.put("/departments/{department_id}", status_code=status.HTTP_202_ACCEPTED)
def put_department_id(
    department_id: UUID,
    request_body: dto.Position.Update,
    db: Session = Depends(db_session),
) -> dto.Department.Update:
    result = select(tables.Department).where(tables.Department.id == department_id)
    result = db.scalars(result).first()
    result.name = request_body.name
    db.commit()
    db.refresh(result)
    return result


@router.delete("/departments/{department_id}", status_code=status.HTTP_200_OK)
def del_department_id(
    department_id: UUID, db: Session = Depends(db_session)
) -> dto.Department:
    result = select(tables.Department).where(tables.Department.id == department_id)
    result = db.scalars(result).first()
    if result:
        db.delete(result)
        db.commit()
        return result
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Position {department_id} not found",
    )


@router.get("/departments/{department_id}/workers", response_model=list[dto.Worker])
def get_position_workers(
    department_name: str, db: Session = Depends(db_session)
) -> list[dto.Worker]:
    result = (
        select(tables.Worker)
        .join(tables.Department, tables.Worker.department_id == tables.Department.id)
        .where(tables.Department.name == department_name)
    )
    result = db.scalars(result).all()
    return result
