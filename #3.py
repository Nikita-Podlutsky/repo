with open("scientist.txt","r", encoding="utf-8") as f:
    """
    Приводим данные из файла во вложеный список
    """
    data = list(map(lambda x: x.split("#"), f.read().split("\n")[1:-1]))




f = False

while :
if not f:
    print("В этот день ученые отдыхали")