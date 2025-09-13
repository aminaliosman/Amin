storage = {
    'cap': 5,
    'trousers': 30,
    'shirt': 15
}

balance = 200

print(f"Bizim balansda: {balance} manat var.")
print("Bizde cap 5 ₼ , trousers 30 ₼ ve shirt 15 ₼")

a = int(input("Siz ne isteyirsiniz? "))


if a == storage['cap']:
    balance -= storage['cap']
    print('Siz cap aldiz')
elif a == storage['trousers']:
    balance -= storage['trousers']
    print('Siz trouser aldiz')
elif a == storage['shirt']:
    balance -= storage['shirt']
    print('Siz shirt aldiz')
