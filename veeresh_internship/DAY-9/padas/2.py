import pandas as pd
names=pd.series(['Alice','bob','CHARLIE'])
print(names.str.lower())
print(names.str.contains('a'))
