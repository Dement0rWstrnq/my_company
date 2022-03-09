"""
1. Добавить 3 департамента
        d1 = tables.Department()
        d1.name = "Отдел связи"

        d2 = tables.Department()
        d2.name = "Отдел разработки"

        d3 = tables.Department()
        d3.name = "Отдел продаж"

        session.add(d1)
        session.add(d2)
        session.add(d3)
        session.commit()

2. Добавить 3 должности
        d1 = tables.Position()
        d1.name = "Менеджер"

        d2 = tables.Position()
        d2.name = "Начальник отдела"

        d3 = tables.Position()
        d3.name = "Сисадмин"

        session.add(d1)
        session.add(d2)
        session.add(d3)
        session.commit()

3. Добавить 3 работников
        d1_pos = select(tables.Position).where(tables.Position.name == "Менеджер")
        d1_pos = session.scalars(d1_pos).first()
        d1_dep = select(tables.Department).where(tables.Department.name == "Отдел связи")
        d1_dep = session.scalars(d1_dep).first()
        d1 = tables.Worker()
        d1.name = "Василий"
        d1.surname = "Федотов"
        d1.position = d1_pos
        d1.department = d1_dep

        d2_pos = select(tables.Position).where(tables.Position.name == "Начальник отдела")
        d2_pos = session.scalars(d2_pos).first()
        d2_dep = select(tables.Department).where(tables.Department.name == "Отдел разработки")
        d2_dep = session.scalars(d2_dep).first()
        d2 = tables.Worker()
        d2.name = "Аркадий"
        d2.surname = "Меньшков"
        d2.position = d2_pos
        d2.department = d2_dep

        d3_pos = select(tables.Position).where(tables.Position.name == "Сисадмин")
        d3_pos = session.scalars(d3_pos).first()
        d3_dep = select(tables.Department).where(tables.Department.name == "Отдел продаж")
        d3_dep = session.scalars(d3_dep).first()
        d3 = tables.Worker()
        d3.name = "Аркадий"
        d3.surname = "Меньшков"
        d3.position = d3_pos
        d3.department = d3_dep

        session.add(d1)
        session.add(d2)
        session.add(d3)
        session.commit()

4. Добавить 3 навыка
        skill_1 = tables.Skill()
        skill_1.name = "Толерантность"
        skill_1.description = "Толерантное отношение к меньшинствам"

        skill_2 = tables.Skill()
        skill_2.name = "Стрессоустойчивость"
        skill_2.description = "Не унывает, когда что-то не получается"

        skill_3 = tables.Skill()
        skill_3.name = "Коммуникабельность"
        skill_3.description = "Легко найдет контакт с любым человеком"

        session.add(skill_1)
        session.add(skill_2)
        session.add(skill_3)
        session.commit()

5. Добавить 2 навыка некоторому работнику
        skill_1 = select(tables.Skill).where(tables.Skill.name == "Толерантность")
        skill_1 = session.scalars(skill_1).first()

        skill_2 = select(tables.Skill).where(tables.Skill.name == "Коммуникабельность")
        skill_2 = session.scalars(skill_2).first()

        worker = select(tables.Worker).where(tables.Worker.surname == "Федотов")
        worker = session.scalars(worker).first()

        worker.skills.append(skill_1)
        worker.skills.append(skill_2)

        session.commit()

6. Выбрать все департаменты
        all_dep = select(tables.Department)
        all_dep = session.scalars(all_dep).all()
        print(all_dep)

7. Выбрать департамент с определенным именем
        all_dep = select(tables.Department).where(tables.Department.name == "Отдел связи")
        all_dep = session.scalars(all_dep).first()
        print(all_dep)

8. Выбрать департаменты, которые были созданы позже января и отсортировать
по дате создания по убыванию
        all_dep = (
            select(tables.Department)
            .where(tables.Department.created_at > "2022.01.31")
            .order_by(desc(tables.Department.created_at))
        )
        all_dep = session.scalars(all_dep).all()
        print(all_dep)

9. Обновить название одного работника
        worker_new_name = (
            select(tables.Worker)
            .join(tables.Position, tables.Worker.position_id == tables.Position.id)
            .where(tables.Position.name == "Сисадмин")
        )
        worker_new_name = session.scalars(worker_new_name).first()
        worker_new_name.name = "Слава"
        worker_new_name.surname = "Зачетный"

10. Удалить департамент
        del_dep = select(tables.Department).where(tables.Department.name == "Отдел связи")
        del_dep = session.scalars(del_dep).first()
        print(del_dep)
        session.delete(del_dep)

11. Сделать выборку работников и какое количество навыков у него есть
        work_skill = (
            select(tables.Worker.id, func.count(tables.WorkerSkill.skill_id))
            .join(tables.WorkerSkill, tables.WorkerSkill.worker_id == tables.Worker.id)
            .group_by(tables.Worker.id)
        )
        print(session.scalars(work_skill).all())

12. Сделать выборку работников, которые владеют определенным навыком
        sel_work = (
            select(tables.Worker)
            .join(tables.WorkerSkill, tables.WorkerSkill.worker_id == tables.Worker.id)
            .join(tables.Skill, tables.Skill.id == tables.WorkerSkill.skill_id)
            .where(tables.Skill.name == "Толерантность")
        )
        session.scalars(sel_work).first()

13. Добавить в департамент человека через департамент
        sel_dep = select(tables.Department).where(tables.Department.name == "Отдел продаж")
        sel_dep = session.scalars(sel_dep).first()
        worker = tables.Worker(
            name="Вася",
            surname="Петров",
            position_id="1fb197b4-932a-11ec-882b-0242ac120002"

        )
        sel_dep.workers.append(worker)
        session.add(worker)
"""
from datetime import datetime
from uuid import UUID

from sqlalchemy.orm import with_expression

from company_rest.db import tables, session_scope
from sqlalchemy import select, desc, func
from pydantic import BaseModel


class Position(BaseModel):
    id: UUID
    name: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


if __name__ == "__main__":
    with session_scope() as session:
        result = select(tables.Position)
        result = session.scalars(result)
        print(result)

        # w = tables.Worker(
        #     name='Vasya',
        #     surname="Ivanov",
        # )
        # w.department = department
        # w.position = p
        # session.add(w)
        # session.commit()

        # result = session.query(tables.Department).all()
        # print(result)

        # result: tables.Worker = session.query(tables.Worker).first()

        # session.delete(result)
