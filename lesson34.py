# BETWEEN ---> SELECT * FROM users WHERE birthday BETWEEN DATE '2000-01-10' AND '2010-10-23';
# n sanadan m sanagacha bo'lganlarini olsin

# SELECT * FROM users WHERE email LIKE '%.ru';  email ustunida .ru bilan tugagan barcha malumotlarni ol

# SELECT * FROM users WHERE email LIKE '%soz%';  orasida --> soz <-- qatnashgan barcha malumotlarni ol

#  SELECT * FROM users WHERE email LIKE '_______@%';   --> 7 ta tagchiziq bo'lgani uchun boshi 7 ta harfdan
#  iborat email manzillarni olib ber

# SELECT * FROM users WHERE country ILIKE 'd%';   --> bu bosh harf va kichik harf ahamiyatga ega bo'lmagan ' LIKE '


# SELECT country FROM users GROUP BY country ORDER BY country;  --> country bo'yicha guruhlab chiqarish


# SELECT country, COUNT(*) FROM users GROUP BY country ORDER BY country;   --> qaysi davlatdan nechta foydalanuvchi
# borligini chiqarib


#  SELECT country, COUNT(*) FROM users GROUP BY country HAVING COUNT(*)<7 ORDER BY country;
# bu COUNT(*) natijasi 7 dan kichik bo'lgan malumotlarni oladi

