from pydantic import BaseModel
from typing import Optional, List


class Employee(BaseModel):
    id: int
    name: str
    department: str | None = None