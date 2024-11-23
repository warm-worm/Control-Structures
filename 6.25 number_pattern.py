# Program that creates the following pattern:
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999
row = 10
for x in range(row):
    print(str(x) * x)
