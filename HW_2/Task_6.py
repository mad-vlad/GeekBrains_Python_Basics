q = int(input("How many products you would like to add to the system?\n\t Quantity: "))
chr = "Name", "Price", "Quantity", "Unit"
products, names, prices, Quantity, uoms = [], [], [], [], []
for i in range(q):
    print(f"Please input product details # {i + 1} :")
    name, price, quantity, uom = input("\tName : "), input("\tPrice : "), input("\tQuantity : "), \
                                 input("\tUnit : ")
    products_up = (i + 1, {chr[0]: name, chr[1]: price, chr[2]: quantity, chr[3]: uom})
    products.append(products_up)
    names.append(products[i][1].get(chr[0]))
    prices.append(products[i][1].get(chr[1]))
    Quantity.append(products[i][1].get(chr[2]))
    uoms.append(products[i][1].get(chr[3]))
analytics ={chr[0]: names, chr[1]: prices, chr[2]: Quantity, chr[3]: uoms}
print(f"Statistics about the products can be found below: \n{analytics}")