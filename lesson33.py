# table ga yangi malumot kiritish

# INSERT INTO users(
#     name,
#     email,
#     birthday)
#
# VALUES ('Ali', 'ali@mail.ru', DATE '2000-08-19')

#https://www.mockaroo.com/


# \i C:/users.sql; (manzil)  ---> sql fayldan malumotlarni avtomatik bazaga kiritish

# SELECT * FROM users;    Barcha ustunlarni olish

# SELECT first_name, gender, country FROM users;  --> aniq bir ustunlardagi malumotlarni olish



# SELECT * FROM users ORDER BY country;   --> davlatlar bo'yicha tartiblab olish

#  SELECT * FROM users ORDER BY country, first_name; davlatlar bo'yicha va ism bo'yicha tartiblab olish


# SELECT * FROM users ORDER BY id DESC;  --> teskari tarzda tartiblab beradi


# SELECT DISTINCT country FROM users ORDER BY country;   --> guruhlab beradi


# SELECT * FROM users WHERE country='Brazil';   --> shart bo'yicha malumot olib beradi



# SELECT * FROM users WHERE country='China' AND gender = 'Male';   --> bir nechta shart bilan olish  (AND)



# SELECT * FROM users WHERE country='China' OR country='Argentina' OR country='Japan';  bir nechta shart bilan olish  (OR)



# SELECT id, first_name, email FROM users LIMIT 25;   --> nechta malumot olishni o'zimiz belgilaymiz


# SELECT * FROM users OFFSET n;  n (son) tasini tashlab qolganini olishni belgilash



# SELECT * FROM users OFFSET 20 LIMIT 15;   --> 20 tasini tashlab 15 tasini ol



# SELECT * FROM users FETCH FIRST 18 ROW ONLY;   ---> 18 tasini olish  (LIMIT ga o'xshaydi)



# SELECT * FROM users WHERE country IN ('Russia', 'Brasil', 'Indonesia', 'China');  --> OR ni qulay varianti





