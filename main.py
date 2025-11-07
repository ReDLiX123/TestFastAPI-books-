from fastapi import FastAPI, HTTPException, status, Response, Query
from schemas import Book, BookCreate, BookUpdate


app = FastAPI()


db = []


def next_id():
    if not db:
        return 1
    return db[-1]["id"] + 1


# GET-запрос на получение списка книг
@app.get("/books", response_model=list[Book], status_code=status.HTTP_200_OK, description='Получить список книг из базы данных')
def get_books(
    skip: int = Query(0, description='Кол-во книнг, которые нужно пропустить', ge=0),
    limit: int = Query(10, description='Макс. кол-во книг в ответе', gt=0, le=25),
):
    return db[skip: skip + limit]


# GET-запрос на получение одной книги по ID
@app.get("/books/{book_id}", response_model=Book, status_code=status.HTTP_200_OK, description='Получить одну книгу по ее ID из базы данных')
def read_book(book_id: int):
    for book in db:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail='Книга не найдена')



# POST-запрос на создание книге в базе данных
@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED, description='Создать книгу')
def create_book(book: BookCreate):
    book_data = book.model_dump()

    new_id = next_id()

    book_data["id"] = new_id

    db.append(book_data)
    return book_data



# PUT-запрос на обновление параметров книги по ее ID
@app.put("/books/{book_id}", response_model=Book, status_code=status.HTTP_200_OK, description='Обновление параметров книги по ее ID')
def update_book(book_id: int, book_update: BookUpdate):

    for book in db:
        if book["id"] == book_id:
            update_data = book_update.model_dump(exclude_unset=True)
            book.update(update_data)
            return book
    raise HTTPException(status_code=400, detail='Книги с таким ID не найдено')



# DELETE-запрос на удаление книги из базы данных по ее ID
@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT, description='Удаление книги из базы данных')
def delete_book(book_id: int):
    for book in db:
        if book["id"] == book_id:
            db.remove(book)
            return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=404, detail="Не нашел книгу по ID")
