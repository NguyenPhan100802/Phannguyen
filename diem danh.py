import pandas as pd
series_ex = {"a":[1, 4, 6, 7, 8], "b":[23, 12, 56, 8, 22], "c":[87, 65, 43, 11, 34]}
df = pd.DataFrame(dataframe_ex)

print(df)

print('in ra cot dau cua 1 dataframe')
print(df['a'])

print('In ra hàng đầu tiên của 1 data')
print(df.loc[0])

print('In ra phan tu dau cua mot series')
series_data = pd.Series([1,2,3,4,5])
