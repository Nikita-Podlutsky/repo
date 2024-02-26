with open("scientist.txt","r", encoding="utf-8") as f:
    """
    Приводим данные из файла во вложеный список
    """
    data = list(map(lambda x: x.split("#"), f.read().split("\n")[1:-1]))


hash_data = {}

# Функция перевода даты в число
def str2data(s):
    s = s.split("-")
    n = int(s[0])*365 + int(s[1])*30 + int(s[2])
    return n

# Фильтруем лишних лжеоткрывателей
for i in sorted(data, key = lambda x: str2data(x[2]))[::-1]:
    hash_data[i[1]] = i

# Формируем строку которую запишем в файл
ans = "ScientistName#preparation#date#components\n"
for i in sorted(hash_data.items(), key = lambda x: str2data(x[1][2])):
    ans+= "#".join(i[1])+"\n"


# Запись в файл

with open("scientist_origin.txt","w", encoding="utf-8") as f:
    f.write(ans)



# Вытаскиваем данные о лжеоткрывателях
print("Разработчиками Аллопуринола были такие люди (результаты выведите в порядке возрастания даты):")
for i in sorted(data, key = lambda x: str2data(x[2])):
    if i[1] == "Аллопуринол" and i[2] != hash_data["Аллопуринол"][2]:
        print(i[0],"-",i[2])

print(f"Оригинальный рецепт принадлежит: {hash_data['Аллопуринол'][0]}")