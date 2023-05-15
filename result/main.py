import csv
import json

from present import JSON_USERS_PATH, CSV_BOOKS_PATH

users_list = []

with open(JSON_USERS_PATH) as f:
    users = json.load(f)

for user in users:
    user_dict = {
        "name": user["name"],
        "gender": user["gender"],
        "address": user["address"],
        "age": user["age"],
        "books": []
    }
    users_list.append(user_dict)

books_list = []
with open(CSV_BOOKS_PATH) as f:
    books = csv.DictReader(f)
    for book in books:
        books_dict = {
            "title": book["Title"],
            "author": book["Author"],
            "pages": int(book["Pages"]),
            "genre": book["Genre"]
        }
        books_list.append(books_dict)

total_users = len(users_list)
total_books = len(books_list)
books_per_user, extra_books = divmod(total_books, total_users)

id = 0
for user in users_list:

    for i in range(books_per_user):
        user['books'].append(books_list[id])
        id += 1

    if extra_books > 0:
        user['books'].append(books_list[id])
        id += 1
        extra_books -= 1

with open("result.json", "w")as f:
    result = json.dumps(users_list, indent=2)
    f.write(result)