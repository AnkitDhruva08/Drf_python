# Drf_python

INSERT USER 

http://127.0.0.1:8000/api/users/

METHOD : POST
{
  "username": "rinku",
  "password": "password123"
}

======================================================================================
BY THIS WE WILL GET ACCESS AND REFRESH TOKEN 
FOR API TOKEN 
http://127.0.0.1:8000/api/token/

METHOD : POST
{
  "username": "rinku",
  "password": "password123"
}




=============================================================
ADD Authorization IN HEADER 
ADD ACEES TOEKN IN HEADER 
KEY                             VALUE
Authorization : Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQzNDM2NzAyLCJpYXQiOjE3NDM0MzY0MDIsImp0aSI6IjQ5M2RmNTA3NGRjMzQzM2Q5YzNjYzgzYzgyNDc2OTdkIiwidXNlcl9pZCI6MiwidXNlcm5hbWUiOiJyaW5rdSJ9.GynWy2pdCLYlQR7df0qSzRnMee2GW-HNGUnJEwGXeps
add category

http://127.0.0.1:8000/api/categories/

METHOD : POST
{
    "name": "Science Fiction"
}


=============================================================


ADD BOOK 

http://127.0.0.1:8000/api/books/

METHOD : POST



{
    "title": "Hindi",
    "author": "Ankit",
    "published_date": "1965-06-01",
    "ISBN": "9780441013593",
    "category": 1  
}


====================================================================
Books API
List all books: GET /api/books/

Retrieve a book by ID: GET /api/books/{id}/

Create a new book: POST /api/books/

Update a book: PUT /api/books/{id}/

