import pandas as pd
s = pd.Series([1,2,3,4], index=['a','b','c','d'])

# print(s.index)
# print(s.values)
# print(s.dtype)


s2 = pd.Series(['a','b','c','d'])

# print(s2.index)

# print(s['c'])
# print(s[['b','c']])

df = pd.DataFrame

data_dict = {
    '이름' : ['소라', '창훈', '영미'],
    '나이' : [20, 30, 35],
    '거주지' : ['인천', '순천', '동해']
}

df_dict = pd.DataFrame(data_dict)

# print(df_dict)


# 파일 경로 지정
excel_file = 'trpandas_data.csv'

# CSV 파일을 데이터프레임으로 불러오기
df_school_loaded = pd.read_csv(excel_file)
print(df_school_loaded)