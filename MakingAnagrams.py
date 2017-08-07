a = input().strip()
b = input().strip()
diff = 0
for i in range(ord('a'), ord('z')+1):
    diff += abs(a.count(chr(i)) - b.count(chr(i)))
print(diff)