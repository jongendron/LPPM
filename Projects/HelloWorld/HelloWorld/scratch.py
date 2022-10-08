data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"

print(data[::5])    # start to end by 5
print(data[1:5])    # from 1 to
print(data[0:-1:5]) # from 0 (start) to -1 (end)
print(data[:-1:5])  # start to -1 (neg index)
for i in range(1, 10):
    print(i)
    print(i)
    print(i)
    for j in range(1,20):
        print(j)
        print(j)

