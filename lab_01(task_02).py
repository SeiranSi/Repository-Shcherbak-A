def getProducts() :
    # dic = dict()
    dic = {}
    while True:
        inp = input('Add a product? (y/n):')
        if inp == 'y':
            product = input('Input product:')
            if product == 'exit':
                break
            amount = input('Input amount:')
            if amount == 'exit':
                break
            try:
                key = float(amount)
            except ValueError:
                print("Invalid input. Please enter a number or 'exit'.")
                continue
            dic[product] = key

            inP = input('Show inventory? (y/n):')
            if inP == 'y' :
                print(dic)
            else:
                if inP =='exit':
                    break
        else:
            inpu = input('Delete a product? (y/n):')
            if inpu == 'y':
                product = input('Input product:')
                if product == 'exit':
                    break
                del dic[product]
            inP = input('Show inventory? (y/n):')
            if inP == 'y' :
                print(dic)
            else:
                if inP =='exit':
                    break
            continue
    print('Inventory:', dic)

getProducts()