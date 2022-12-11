# SQL --> MYSQL POSTGRESQL SQLITE
# NO SQL
# MONGO DB



# parolni o'zgartirish uchun sql buyruq  --> ALTER USER username WITH PASSWORD 'yangiparol';

# \l bazamizda mavjud DATABASE larni chiqarib beradi  --> bu postgresql buyrugi


# CREATE DATABASE nomi;   -- yangi database yaratish  --> bu sql tili buyrugi

# \c nomi;  -- database ga ulanish uchun --> bu postgresql buyrugi


#DROP DATABASE nomi;  database ni udalit qilish uchun  -->  bu sql tili buyrugi


# CREATE TABLE jadval_nomi(
#     ustun nomi + malumot turi + qoshimcha
# )


# jadval yaratish kodi
# CREATE TABLE users(
#     id int,
#     name VARCHAR(60),
#     email VARCHAR(100),
#     birtday TIMESTAMP
# )


# \d jadvalga kirish

# CREATE TABLE users(
#     id BIGSERIAL NOT NULL PRIMARY KEY,
#     name VARCHAR(60) NOT NULL,
#     email VARCHAR(100) NOT NULL,
#     birtday DATE NOT NULL
# )


# 4 'ali' 'ali@mail.ru' '19.08.2000'
