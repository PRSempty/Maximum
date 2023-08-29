a = input()
b = ''.join(reversed(a))
if str(b) == str(a):
    print(True)
else:
    print(False)
