import pandas as pd
names = pd.Series(['Alice', 'veeresh', 'CHARLIE', 'david'])
print("Lowercase:")
print(names.str.lower())

print("uppercase")
print(names.str.upper())
print("Contains 'c':")
print(names.str.contains('c', case=True))
print("String Length:")
print(names.str.len())