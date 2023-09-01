from sqlalchemy.orm import Session
from datetime import  datetime
from . import  schema,models
from fastapi import HTTPException

def create_report(db:Session,info:schema.InfoBase):
    start = datetime.fromisoformat(f'{info.date}T{info.start_time}')
    end = datetime.fromisoformat(f'{info.date}T{info.end_time}')
    a= end-start

    db_info=models.Info(
        date = info.date,
        project= info.project,
        task_id = info.task_id,
        task = info.task,
        status = info.status,
        start_time= info.start_time,
        end_time= info.end_time,
        duration= end - start,
        description= info.description,
        total_hours= info.total_hours,
    )
    db.add(db_info)
    db.commit()
    db.refresh(db_info)
    return db_info

def get_info(db: Session, info_id: int):
    db_info = db.query(models.Info).filter(models.Info.id == info_id).first()
    if db_info is None:
        raise HTTPException(status_code=404, detail="Info not found")
    return db_info

def get_all_info(db: Session):
    db_info=db.query(models.Info).all()
    return db_info

def update_info(db: Session, info_id: int, info_update: schema.InfoBase):
    db_info = get_info(db, info_id)

    for field, value in info_update.__dict__.items():
        setattr(db_info, field, value)
    db.commit()
    db.refresh(db_info)
    return db_info


def delete_info(db: Session, info_id: int):
    db_info = get_info(db, info_id)
    db.delete(db_info)
    db.commit()
    return db_info

