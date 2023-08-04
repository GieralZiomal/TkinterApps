import requests

r = requests.get("http://api.nbp.pl/api/exchangerates/tables/C/")

data = r.json()

class Waluta:

    name = ""
    code = ""
    bid = ""
    ask = ""

    def __init__(self, name, code, bid, ask):
        self.name = name
        self.code = code
        self.bid = bid
        self.ask = ask

objsl = list()
for x in range(len(data[0]['rates'])):
    waluta = Waluta(data[0]["rates"][x]['currency'],data[0]["rates"][x]['code'],data[0]["rates"][x]['bid'],data[0]["rates"][x]['ask'])
    objsl.append(waluta)


def Values():
    for x in range(len(objsl)):
        print(f'{x+1}.Nazwa waluty: {objsl[x].name}')
    wybor = input("Jaką walute chcesz zamienienić: ")
    wybor = int(wybor) - 1
    tf = input(f'Wybrana waluta to: {objsl[wybor].name} \nCzy chcesz kontynuować? \nT/N \n')
    if tf.upper() == "T":
        print(f"Nazwa Waluty to: {objsl[wybor].name}\nKod Waluty: {objsl[wybor].code}\nCena Sprzedaży to: {objsl[wybor].bid}\nCena Zakupu to: {objsl[wybor].ask}\n")
        choice = input("1.Sprzedaż \n2.Kupno\n")
        if choice == "1":
            val = input("Podaj kwotę: ")
            result = float(val)*float(objsl[wybor].bid)
            print(f'Za Kwotę {val}PLN otrzymasz {result}{objsl[wybor].code}')
            Values()
        elif choice == "2":
            val = input("Podaj kwotę: ")
            result = float(val)*float(objsl[wybor].ask)
            print(f'Za Kwotę {val}PLN otrzymasz {result}{objsl[wybor].code}')
            Values()
    elif tf.upper() == "N":
        en = input("Czy chcesz opuścić program? T/N \n")
        if en.upper() == "T":
            exit()
        elif en.upper() == "N":
            Values()
        else:
            print("Nieprawidłowy format!")
            Values()
    else:
        print("Nieprawidłowy format!")
        Values()


Values()