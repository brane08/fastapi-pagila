from datetime import datetime
from typing import TypeVar, Optional, List

from pydantic import BaseModel

T = TypeVar('T')


class ApiResponse(BaseModel):
    success: bool = True
    message: Optional[str] = None
    page: Optional[int] = None
    size: Optional[int] = None
    total: Optional[int] = None
    data: Optional[List[T]] = None


class Actor(BaseModel):
    id: int
    first_name: str
    last_name: str
    last_update: datetime

    class Config:
        orm_mode = True
