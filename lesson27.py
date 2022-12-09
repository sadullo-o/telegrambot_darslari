import datetime as dt

# hozir = dt.datetime.now()

# print(hozir)  hozirgi sana va vaqt
# print(hozir.date())  hozirgi sana

# print(hozir.time()) hozirgi vaqt

# print(hozir.hour) soat ni o'zini oladi

# print(hozir.minute)

# print(hozir.second)

# print(f"Bugun sana: {hozir.date()}")

# print(f"Hozir soat: {hozir.time()}")

# keyingiSoat = dt.time(22, 46, 24)

# print(keyingiSoat)

# bugun = dt.date.today()
#
# yangi_yil = dt.date(2023, 1, 1)

# farq = yangi_yil - bugun
#
# oy = int(farq.days/30)
# kun = farq.days - (oy * 30)
# print(oy)
#
# print(f"Yangi yilga {oy} oy va {kun} kun qoldi")

# datetime dan datetime ni ayrib bo'ladi lekin date ni emas. date dan date ni ayrib bo'ladi lekin datetime ni emas


# hozir = dt.datetime.now()
#
# futbol = dt.datetime(2022, 12, 17, 20, 0, 0)
#
# farq = futbol - hozir
#
# print(farq.days)
# print(farq.seconds)
#
# minut = farq.seconds/60
#
# print(f"Futbolga {farq.days} kun va {minut} daqiqa qoldi")

# hozir = dt.datetime.now()

# vaqt = hozir.strftime("%H:%M:%S")

# sana =  hozir.strftime("%d-%m-%Y, %H:%M")
#
# print(sana)

# print(vaqt)
# print(hozir)


# AMALIYOT VAZIFASI

# tugilgan (kun, oy, yil) --> hozirgacha nechi kun nechi oy va nechi yil yashaganini chiqarib beruvchi dastur

# t_kun = input('Tugilgan kuningizni kiriting (24.8.1999)')
#
# t_kun = t_kun.split('.')
#
# print(t_kun)
#
# a = int(t_kun[0])
# b = int(t_kun[1])
# c = int(t_kun[2])


# now = dt.datetime.now()
# kun = now.date()
# a=input("kunni kiriting: ")
# b=input("Oyni kiriting(raqamda): ")
# c=input("Yilni kiriting: ")
# tyil = dt.date(int(c),int(b),int(a))
# fq = kun-tyil
# # sfq = fq.strftime("%Y-%M-%D")
#
# kun = fq.days
#
# oy = kun/30
#
# yil = oy/12
#
# print(kun)
# print(oy)
# print(yil)


