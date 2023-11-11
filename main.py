# a = input("Yozuv kiriting: ")
# s = "Salomat"
# print(list(s))
# n = a.split()
# for i in range(len(n)):
#     j = n.pop(0)
#     n.append(list(j))
# print(n)
# for i in n:
#     print(i[-1]+i[1:-1]+i[0], end=" ")


# a = [(4, 45), (20, 1), (90, 40), (6, 20), (2, 10)]
# print(sorted(a, key=lambda x: x[1]))





# b = list(sorted(a, key=lambda x: x[1]))
# print(b)


# d = {
#     "ism": 20,
#     "yosh": 24,
#     "kurs": 3,
#     "univer": 50
# }
# print(sorted(d.items(), key=lambda q: q[1])[:5])
# print(sorted(list(d.items()), key=lambda h: h[1])[:5])


b = True
n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

s = sum(a[0])
for i in a:
    b = b and sum(i) == s

for i in range(n):
    u = 0
    for j in range(n):
        u += a[j][i]
    b = b and u == s
u = 0
for i in range(n):
    u += a[i][i]
b = b and u == s

u = 0
for i in range(n):
    u += a[i][n-i-1]
b = b and u == s

print(b)


# a = True
# while True:
#     n = int(input())
#     if n == -1:
#         break
#     a *= n >= 0
#
# print(a)















