# ===========================================================
# Yangi kodlardan kichik dastur (boshlanishi)
# ===========================================================

while True:
    buyruq1 = input('Boshlash uchu enterni bosing')
    if buyruq1 == "":
      yosh = int(input('yoshinggizni kiriting: '))
    if yosh > 40:
        print('Siz qarisiz')
    elif yosh > 17:
        print('Siz voyaga yetgansiz')
    else:
        print('Uka xali kichkinalik qilasan')

    xabar = "Uka degan maxluqot"
    xabar2 = 'Tall guy'
    xabar3 = "Kattovskiy"
    xabar_main = "Opaxonim mexribonim"

    person = input("Isminggizni kiriting: ")
    if person == "Ali":
        print(xabar)
    elif person == "Abdurazzoq":
        print(xabar2)
    elif person == "Muhammad":
        print(xabar3)
    elif person == "Nurjaxon":
        print(xabar_main)
    else:
        print('kim edi bu')

    buyruq = ["stop"]
    davom = input("Yana davom etamizmi? To'xtatish uchun 'stop' deb yozing: ")
    if davom.lower() == buyruq[0]:
        print("Dastur to'xtadi.")
        break
# ===================================================
# looks like very interesting
# ===================================================

