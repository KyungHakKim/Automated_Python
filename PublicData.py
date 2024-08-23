import pandas as pd

file_path1 = '한국전력공사_지역별 전기차 현황정보.csv'
file_path2 = '한국전력공사_지역별 전기차 현황정보_20240731.csv'
file_path3 = '한국전력공사_지역별 전기차 충전소 현황정보_20231231.csv'

df1 = pd.read_csv(file_path1,encoding='cp949')
df2 = pd.read_csv(file_path2)

station = pd.read_csv(file_path3)

# print("df1 : ", df1.head(2))
# print("-----------" * 10)
# print("df2 : ", df2.head(2))
# print("-----------" * 10)
# print("station : ", station.head(2))

# print(df1.loc[[2, 1, 0], '기준일':'경기'])
# print(df2.loc[0:2, '기준일':'경기'])

#df1에서 중복된 데이터 제거하기
df1.drop([0,1,2], axis=0, inplace=True)
print(df1.loc[0:5,'기준일':'경기'])

#df1과 df2병합하기
ev = pd.concat([df1, df2])


#option_context()로 처음과 끝 행/열을 각 4개씩 출력하여 병합결과 확인
with pd.option_context('display.max_rows', 8, 'display.max_columns', 8):
    pd.set_option('show_dimensions', False)
    print(ev)