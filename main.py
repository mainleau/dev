import sys

def readProducts(path=''):
    File = open(path, 'r')
    FileContent = File.read()
    File.close()

    FileContent = FileContent.split('\n')
    FileContent.pop()

    result = {}

    for i in FileContent:
        a, b = i.split(' ', 1)
        dic[a] = b

    return result

def readBill(path=''):
    File = open(path, 'r')
    FileContent = File.read()
    File.close()

    FileContent = FileContent.split('\n')
    FileContent.pop()

    result = []

    for i in FileContent:
        result.append(i.split(' '))
    result.pop()

    products = readProducts('products.txt')
    array = []

    for a, b in FileContent:
        array.append(a, products[b], c)

    return arrays

def main():
    File = open('facture.txt')
    FileContent = File.read()
    File.close()

    FileContent = FileContent.split('\n')

    array = []

    for i in FileContent:
        array.append(i.split(' '))
    array.pop()

    price = 0

    for i in array:
        price += int(i[2])

    print(f'Prix des produits cumulés : {price}€')

    File = open('products.txt', 'r')
    FileContent = File.read()
    File.close()

    FileContent = FileContent.split('\n')
    FileContent.pop()

    result = {}

    for i in FileContent:
        a, b = i.split(' ', 1)
        result[a] = b

    beurre, sel = False, False

    for _, i, _ in array:
        if result[i] == 'Beurre doux':
            beurre = True
            if result[i] == 'Sel':
                sel = True
    
    print(f"Beurre doux : {'présent' if beurre else 'non présent'}, sel : {'présent' if beurre else 'non présent'}")

    enlightened = ''

    for a, b, c in array:
        enlightened = f"{b} {result[b]} {a} x {c}€ = {int(a)*int(c)}€\n"

    File = open('enlightenedBill.txt', 'w')
    File.write(enlightened)
    File.close()

if __name__ == "__main__":
        main()
