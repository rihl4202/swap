def swap():
    file1 = input("Enter file 1: ")
    file2 = input("Enter file 2: ")
    a = open(file1, "r")
    data1 = a.read()
    b = open(file2, "r")
    data2 = b.read()
    c = open(file1, "w")
    c.write(data2)
    d = open(file2, "w")
    d.write(data1)
swap()