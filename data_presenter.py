
# problem 2 //////////////////////////////////////////////////////////////////////////
datas = open('Cupcakeinvoices.csv')


#  problem 3 /////////////////////////////////////////////////////////////////////////
# for data in datas:
#     print(data)


# problem 4 ///////////////////////////////////////////////////////////////////////////
# newD = []
# for data in datas:
#     newData = data.strip('\n').split(',')
#     newD.append(newData)

# print(newD)

# for d in newD:
#     print(d[2])


# problem 5 //////////////////////////////////////////////////////////////////////////
# newD2 = []
# for data in datas:
#     newData = data.strip('\n').split(',')
#     newD2.append(newData)

# print(newD2)

# for d in newD2:
#     print(float(d[3]) * float(d[4]))


# problem 6 //////////////////////////////////////////////////////////////////////////
# newD3 = []
# for data in datas:
#     newData = data.strip('\n').split(',')
#     newD3.append(newData)

# print(newD3)

# total = 0.00
# for d in newD3:
#     total = total + (float(d[3]) * float(d[4]))

# print(total)


#  problem 7 //////////////////////////////////////////////////////////////////////////
datas.close()