def palindrom(n):
    if len(n) <= 1:
        return True
    if n[0] != n[-1]:
        return False
    return palindrom(n[1:-1])
print(palindrom("radar"))
print(palindrom("apel"))
print(palindrom("kasur ini rusak"))

