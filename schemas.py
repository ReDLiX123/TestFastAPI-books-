from pydantic import BaseModel, Field
from datetime import datetime

class BookBase(BaseModel):
    title: str = Field(min_length=0, max_length=50)
    author: str = Field(min_length=0, max_length=25)
    year: int = Field(ge=0, le=datetime.now().year)



class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=50)
    author: str | None = Field(default=None, min_length=1, max_length=25)
    year: int | None = Field(default=None, ge=0, le=datetime.now().year)


class Book(BookBase):
    id: int = Field(ge=0)

