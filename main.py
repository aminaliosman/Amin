storage = {
    'cap': 5,
    'trousers': 30,
    'shirt': 15
}

balance = 200

print(f"Bizdaa balancda: {balance} manat var.")
print("Mağazamızda cap (5 manat), trousers (30 manat), və shirt (15 manat) var.")

customer_choice = input("Nə almaq istəyirsiniz? ")

if customer_choice == 'cap':
    if balance >= storage['cap']:
        balance -= storage['cap']
        print(f"Siz bir kepka aldınız. Yeni balansınız: {balance} manat.")
    else:
        print("Balansınızda kepka almaq üçün kifayət qədər vəsait yoxdur.")
elif customer_choice == 'trousers':
    if balance >= storage['trousers']:
        balance -= storage['trousers']
        print(f"Siz bir şalvar aldınız. Yeni balansınız: {balance} manat.")
    else:
        print("Balansınızda şalvar almaq üçün kifayət qədər vəsait yoxdur.")
elif customer_choice == 'shirt':
    if balance >= storage['shirt']:
        balance -= storage['shirt']
        print(f"Siz bir köynək aldınız. Yeni balansınız: {balance} manat.")
    else:
        print("Balansınızda köynək almaq üçün kifayət qədər vəsait yoxdur.")
else:
    print("Üzr istəyirik, belə bir məhsul mövcud deyil.")