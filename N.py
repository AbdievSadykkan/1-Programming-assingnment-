n = int(input())
total = 9 * 60 + n * 45 + ((n - 1) // 2) * 20 + ((n - 1) % 2) * 5
print(total // 60, total % 60)
