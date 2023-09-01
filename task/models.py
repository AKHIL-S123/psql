from sqlalchemy import Column,Integer, String,Time,Date
from sqlalchemy.orm import relationship
from enum import Enum
from .database import Base


# class StatusEnum(Enum):
#     Completed = "Completed"
#     RFD = "RFD"
#     Inprogress = "Inprogress"


class Info(Base):
    __tablename__ = "info"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    project= Column(String)
    task_id = Column(String)
    task = Column(String)
    status = Column(String)
    start_time=Column(String, nullable=False)
    end_time=Column(String)
    duration=Column(String)
    description=Column(String)
    total_hours=Column(String)
    


