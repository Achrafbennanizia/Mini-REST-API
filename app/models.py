from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field

class TaskBase(SQLModel):
title: str = Field(min_length=1, max_length=200)
done: bool = False

class Task(TaskBase, table=True):
id: Optional[int] = Field(default=None, primary_key=True)
created_at: datetime = Field(default_factory=datetime.utcnow)

class TaskCreate(TaskBase):
pass

class TaskRead(TaskBase):
id: int
created_at: datetime

class TaskUpdate(SQLModel):
title: Optional[str] = Field(default=None, min_length=1, max_length=200)
done: Optional[bool] = None

class SensorBase(SQLModel):
value: float
unit: str = Field(min_length=1, max_length=16)

class Sensor(SensorBase, table=True):
id: Optional[int] = Field(default=None, primary_key=True)
recorded_at: datetime = Field(default_factory=datetime.utcnow)

class SensorCreate(SensorBase):
pass

class SensorRead(SensorBase):
id: int
recorded_at: datetime