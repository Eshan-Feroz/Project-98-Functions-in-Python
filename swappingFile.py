def swapFileData():
    fileName1 = input("Enter the first file name: ")
    with open(fileName1, 'r') as a:
        data_a = a.read()

    fileName2 = input("Enter the second file name: ")
    with open(fileName2, 'r') as b:
        data_b = b.read()

    with open(fileName1, 'w') as a:
        a.write(data_b)

    with open(fileName2, 'w') as b:
        b.write(data_a)

swapFileData()