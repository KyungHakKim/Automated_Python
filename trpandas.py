import pandas as pd
# s = pd.Series([1,2,3,4], index=['a','b','c','d'])

# # print(s.index)
# # print(s.values)
# # print(s.dtype)


# s2 = pd.Series(['a','b','c','d'])

# # print(s2.index)

# # print(s['c'])
# # print(s[['b','c']])

# df = pd.DataFrame

# data_dict = {
#     '이름' : ['소라', '창훈', '영미'],
#     '나이' : [20, 30, 35],
#     '거주지' : ['인천', '순천', '동해']
# }

# df_dict = pd.DataFrame(data_dict)

# # print(df_dict)


# # 파일 경로 지정
# excel_file = 'trpandas_data.csv'

# # CSV 파일을 데이터프레임으로 불러오기
# df_school_loaded = pd.read_csv(excel_file)
# print(df_school_loaded)


# 고객 데이터를 담은 딕셔너리 생성
data = {
    "이름": ["김철수", "이영희", "박민수"],
    "나이": [25, 32, 19],
    "도시": ["서울", "대전", "대구"]
}

# 딕셔너리를 사용해 데이터프레임 생성
df = pd.DataFrame(data)

# 데이터프레임 출력
# print(df)

# 데이터프레임의 shape 속성을 사용하여 행과 열의 수 확인
# print("데이터프레임의 차원:", df.shape)

# print(df.columns)

df.columns = ['A', 'B', 'C']
# print(df.columns)

print(df.info())

print(df.describe())