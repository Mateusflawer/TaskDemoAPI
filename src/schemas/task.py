from pydantic import BaseModel
from typing import List

class Task(BaseModel):
    id: int
    title: str
    description: str
    completed: bool = False

class TaskList(BaseModel):
    tasks: List[Task]