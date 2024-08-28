import pandas as pd

data = [[1,10,100],[2,20,200],[3,30,300]]
col = ['col1','col2','col3']
row = ['row1','row2','row3']

df = pd.DataFrame(data=data, index=row, columns=col)
print(df)

result = df.add(1)

print(type(result))
print(result)
print("="*100)

# 다른 DataFrame객체를 더하기

data2 = [[3],[4],[5]]
df2 = pd.DataFrame(data=data2,index=['row1','row2','row3'], columns=['col1'])

print("========= df2 =============")
print(df2)

print("========= df.add(df2) =============")
result = df.add(df2, fill_value=0)
print(result)