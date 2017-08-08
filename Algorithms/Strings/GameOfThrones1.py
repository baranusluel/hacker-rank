chars = [0]*26
str = input().strip()
odds = 0
for i in range(0, len(str)):
    chars[ord(str[i])-97] += 1
for i in range(0, 26):
    if chars[i] % 2 == 1:
        odds += 1
if odds > 1:
    print("NO")
else:
    print("YES")