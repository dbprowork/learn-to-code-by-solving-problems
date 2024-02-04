# DMOJ coci18c3p1

count = 0
blocks = []

string = input()

for i in string:
    if i == 'H':
        if i not in blocks:
            blocks.append(i)
    if i == 'O':
        if i not in blocks:
            blocks.append(i)
    if i == 'N':
        if i not in blocks:
            blocks.append(i)
    if i == 'I':
        if i not in blocks:
            blocks.append(i)
    if ''.join(blocks) == 'HONI':
        count += 1
        blocks = []

print(blocks)
print(count)
