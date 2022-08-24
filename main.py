import os.path
import sys
from _Repository import *
from _Repository import _Repository


def main(args):

    repo = _Repository(args[4])
    repo.create_tables()

    configFile = args[1]
    with open(configFile, 'r') as configFile:
        for line in configFile:
            line = line.split("\n")[0]
            length_splittedLine = len(line.split(","))
            splittedLine = line.split(",")
            if  length_splittedLine == 4:
                hat_ID = splittedLine[0]
                topping = splittedLine[1]
                supplier_id = splittedLine[2]
                quantity = splittedLine[3]
                hat_toInsert = Hat(hat_ID, topping, supplier_id, quantity)
                repo.hats.insert(hat_toInsert)
            else:
                if len(splittedLine[1]) > 1:
                    supplier_ID = splittedLine[0]
                    supplier_Name = splittedLine[1]
                    supplier_toInsert = Supplier(supplier_ID, supplier_Name)
                    repo.suppliers.insert(supplier_toInsert)

    orderFile = args[2]
    output = open(args[3], 'w')
    with open(orderFile, 'r') as orderFile:
        orderID = 1
        for line in orderFile:
            line = line.split("\n")[0]
            splittedLine = line.split(',')
            location = splittedLine[0]
            topping = splittedLine[1]
            orderdHat = repo.hats.findHat(topping)
            supplierName = repo.suppliers.findSupplier(orderdHat.supplier).name
            orderToInsert = Order(orderID, location, orderdHat.id)
            repo.orders.insertNewOrder(orderToInsert)
            orderID += 1
            output.write(topping + "," + supplierName + "," + location + "\n")
            repo.hats.checkQuantity(orderdHat)


    output.close()
    repo.close()
    sys.exit(1)


if __name__ == '__main__':
    main(sys.argv)