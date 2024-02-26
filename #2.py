with open("scientist.txt","r", encoding="utf-8") as f:
    """
    Приводим данные из файла во вложеный список
    """
    data = list(map(lambda x: x.split("#"), f.read().split("\n")[1:-1]))



# Функция перевода даты в число
def str2data(s):
    s = s.split("-")
    n = int(s[0])*365 + int(s[1])*30 + int(s[2])
    return n


ndata = []

for i in data:
    ndata.append((i[0],str2data(i[2]),i[1]))




# Сортировка
def sor(l):
    lind = 0
    nl = [l[0]]
    for i in l[1:]:
        j = 0
        try:
            while i[1]<nl[j][1]:
                j+=1
        except:
            pass
        nl = nl[:j] + [i] + nl[j:]
            

    return nl


ndata = sor(ndata)

for i in range(1,6):
    print(f"{ndata[-i][0]}: {ndata[-i][2]}")



# Сортировка

def sor(l):
    lind = 0
    nl = [l[0]]
    # li = l[0][1]
    for i in l[1:]:
        j = 0
        try:
            while str2data(i[2])<str2data(nl[j][2]):
                j+=1
        except:
            pass
        nl = nl[:j] + [i] + nl[j:]

    return nl




# Формируем строку которую запишем в файл
ans = "ScientistName#preparation#date#components\n"
for i in sor(data)[::-1]:
    ans+= "#".join(i[1])+"\n"


# Запись в файл

with open("scientist.txt","w", encoding="utf-8") as f:
    f.write(ans)




