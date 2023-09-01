from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from .import  models, schema
from .database import SessionLocal, engine
from task.crud import create_report,get_info,update_info,delete_info,get_all_info
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/progress')
def create_progress(data:schema.InfoBase,db:Session=Depends(get_db)):
    return create_report(db,data)

@app.get('/info/{info_id}')
def read_info(info_id: int, db: Session = Depends(get_db)):
    db_info = get_info(db, info_id)
    return db_info

@app.get('/get_all_info')
def get_all(db: Session=Depends(get_db)):
    db_info = get_all_info(db)
    return db_info


@app.put('/info/{info_id}')
def update_info_endpoint(info_id: int, info_update: schema.InfoBase, db: Session = Depends(get_db)):
    db_info = update_info(db, info_id, info_update)
    return db_info

@app.delete('/info/{info_id}', response_model=schema.InfoBase)
def delete_info_endpoint(info_id: int, db: Session = Depends(get_db)):
    db_info = delete_info(db, info_id)
    return db_info

