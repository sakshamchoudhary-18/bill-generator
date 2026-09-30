import os
from datetime import datetime

#input quantity 
def get_number(text):
    while True:
        n = input(text)
        if n.isdigit():
            return int(n)
        else:
            print("Enter proper number please")

#input price
def get_price(text):
    while True:
        try:
            p = float(input(text))
            if p >= 0:
                return p
            else:
                print("Amount can't be negative")
        except:
            print("Invalid amount")

#what is you give you discount 
def get_discount(text):
    while True:
        try:
            d = float(input(text))
            if d >= 0 and d <= 100:
                return d
            else:
                print("Discount must be between 0 and 100")
        except:
            print("Invalid discount")

#bill making 
def make_bill():
    print("====== SHOP BILLING ======")

    count = get_number("How many items? : ")

    if count == 0:
        print("Nothing to bill.")
        return

    names = []
    qty = []
    price = []
    total = []

    for i in range(count):
        print("\nItem", i + 1)

        name = input("Name: ").strip()

        if name == "":
            name = "Item_" + str(i + 1)

        q = get_number("Qty: ")
        p = get_price("Price: ")

        names.append(name)
        qty.append(q)
        price.append(p)
        total.append(q * p)

    discount = get_discount("\nDiscount % (0 if none): ")
#print bill and save 
    print(" BILL ")
    print("Name            Qty   Price   Total")

    grand = 0

    for i in range(count):
        print(names[i].ljust(15), qty[i], "  ", price[i], "   ", total[i])
        grand += total[i]

    discount_amount = round(grand * discount / 100, 2)
    final = round(grand - discount_amount, 2)


    print("Grand Total =", grand)

    if discount > 0:
        print("Discount (" + str(discount) + "%) =", discount_amount)
        print("Final Amount =", final)


    folder = "bills"
    os.makedirs(folder, exist_ok=True)

    filename = "bill_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".txt"
    fullpath = os.path.join(folder, filename)

    f = open(fullpath, "w", encoding="utf-8")

    f.write("BILL RECEIPT\n")
    f.write("Date: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n\n")
    f.write("Name            Qty   Price   Total\n")

    for i in range(count):
        f.write(names[i].ljust(15) + str(qty[i]) + "   " +
                str(price[i]) + "   " + str(total[i]) + "\n")

    f.write("\nGrand Total = " + str(grand))

    if discount > 0:
        f.write("\nDiscount (" + str(discount) + "%) = " + str(discount_amount))
        f.write("\nFinal Amount = " + str(final))

    f.close()

    print("Bill saved:", filename)


if __name__ == "__main__":
    make_bill()