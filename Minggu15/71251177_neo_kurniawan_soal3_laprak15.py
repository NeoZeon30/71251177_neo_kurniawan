def hitungganjil(n):
    if n == 1:
        return 1
    else:
        return (2 * n - 1) + hitungganjil(n - 1)

print(hitungganjil(5))  
print(hitungganjil(3))

