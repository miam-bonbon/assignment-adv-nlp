import pandas as pd

DEV = True
data = pd.DataFrame()
data = pd.DataFrame({
    'column1': [1, 2, 3],
    'column2': ['a', 'b', 'c']
})
print(data.empty)

if (data.empty or DEV):
    print("Data is empty or DEV is True")