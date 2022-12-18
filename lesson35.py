
# AGREGAT FUNKSIYALAR
#  SELECT MAX(narx) FROM cars;    -->  ustundagi eng katta sonni topib beradi

# SELECT MIN(narx) FROM cars;   --> ustundagi eng kichik sonni topib beradi


# SELECT AVG(narx) FROM cars;  --> ustundagi sonlarni o'rtacha qiymati
#  SELECT kompaniya, MIN(narx) FROM cars GROUP BY kompaniya;  --> kompaniya mashinalari orasidagi eng arzonlari

# SELECT kompaniya, MAX(narx) FROM cars GROUP BY kompaniya;

# SELECT SUM(narx) FROM cars;  --> ustungadi sonlarni umumiy qiymati


#  SELECT kompaniya, SUM(narx) FROM cars GROUP BY kompaniya;

#-----------------------------------



# ROUND()    -->  yaxlitlash

# SELECT id, kompaniya, model, narx,ROUND(narx * .10, 2) FROM cars;   --> narxni 10 foizini alohida ustunga chiqarish

# SELECT id, kompaniya, model, narx,ROUND(narx * .10, 2), ROUND(narx - (narx * .10),2) FROM cars;
# chegirma narxini hisoblab alohida ustunga chiqarish


#  SELECT id, kompaniya, model, narx AS asl_narxi ,ROUND(narx * .10, 2) AS chegirma, ROUND(narx - (narx * .10),2) AS chegirma_narx FROM cars;
# ustunga nom berish (AS orqali)


# SELECT COALESCE(email, 'email kirilmagan') FROM users;   --> agar malumot null (bo'sh) bo'lsa ikkinchi qiymatni qaytaradi

# SELECT NOW(); hozirgi sana va vaqtni oladi

# SELECT NOW()::DATE;  --> hozirgi sanani oladi

# SELECT NOW()::TIME;   --> hozirgi soatni oladi

# SELECT NOW() - INTERVAL 'n YEAR';  hozirgi vaqtdan n yilni ayrish


#SELECT NOW() - INTERVAL 'n MONTH';

# SELECT NOW() - INTERVAL 'n DAY';


# SELECT EXTRACT(YEAR FROM NOW());  -- Sanadan yilni olib beradi

# SELECT EXTRACT(MONTH FROM NOW());

# SELECT EXTRACT(DAY FROM NOW());

# SELECT EXTRACT(CENTURY FROM NOW());  --> asr ni olib beradi



#SELECT id, first_name, last_name, birthday, AGE(NOW(), birthday) AS yosh FROM users;
# tugilgan yil bo'yicha yoshni hisoblab beradi


# \d users; --> users tablitsaning ustunlarini ko'rish

# ALTER TABLE users DROP CONSTRAINT users_pkey;  --> takrorlanmaslik xuxusiyatini o'chirish

# ALTER TABLE users ADD PRIMARY KEY (id);  --> takrorlanmaslik xuxusiyatini id ustuniga qo'shish