from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from company_rest import dto
from sqlalchemy import select
from company_rest.db.session import db_session, Session
from company_rest.db import tables

router = APIRouter(tags=["skills"])


@router.get("/skills", response_model=list[dto.Skill], status_code=status.HTTP_200_OK)
def get_skills(db: Session = Depends(db_session)) -> list[dto.Skill]:
    result = select(tables.Skill)
    result = db.scalars(result).all()
    return result


@router.post("/skills", status_code=status.HTTP_201_CREATED)
def create_skill(
    request_body: dto.Skill.New, db: Session = Depends(db_session)
) -> dto.Skill:
    result = tables.Skill(name=request_body.name, description=request_body.description)
    db.add(result)
    db.commit()
    db.refresh(result)
    return result


@router.get(
    "/skills/{skill_id}", response_model=dto.Skill, status_code=status.HTTP_200_OK
)
def get_skill_id(skill_id: UUID, db: Session = Depends(db_session)) -> dto.Skill:
    result = select(tables.Skill).where(tables.Skill.id == skill_id)
    result = db.scalars(result).first()
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Skill {skill_id} not found"
        )
    return result


@router.put("/skills/{skill_id}", status_code=status.HTTP_202_ACCEPTED)
def put_skill_id(
    skill_id: UUID, request_body: dto.Skill.Update, db: Session = Depends(db_session)
) -> dto.Skill.Update:
    result = select(tables.Skill).where(tables.Skill.id == skill_id)
    result = db.scalars(result).first()
    result.name = request_body.name
    result.description = request_body.description
    db.commit()
    db.refresh(result)
    return result


@router.delete("/skills/{skill_id}", status_code=status.HTTP_200_OK)
def del_position_id(skill_id: UUID, db: Session = Depends(db_session)) -> dto.Skill:
    result = select(tables.Skill).where(tables.Skill.id == skill_id)
    result = db.scalars(result).first()
    if result:
        db.delete(result)
        db.commit()
        return result
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Skill {skill_id} not found"
    )
