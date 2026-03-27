def addBinary(a, b):
        aa = 0
        bb = 0
        for i in range(len(a)):
            if a[i] == "1":
                aa += (2 ** (len(a) - 1 - i)) 
        for j in range(len(b)):
            if b[j] == "1":
                aa += (2 ** (len(b) - 1 - j)) 
        return bin(aa + bb)[2:]
a = "1010"
b = "1011"
ahoy = addBinary(a,b)
print(ahoy)