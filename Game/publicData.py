service_key = "Xjtv6KFw8W%2BCMDtypj1hZ%2BM0I1rT2crANbbQIN8L0AJDjB%2FR3Hi1aE8wOeBUFw8Lo5j2zjeyQVwlnm6pH4FCVg%3D%3D"

from PublicDataReader import TransactionPrice
api = TransactionPrice(service_key)

import PublicDataReader as pdr
sigungu_name = "분당구"
code = pdr.code_bdong()


code.loc[(code['시군구명'].str.contains(sigungu_name)) &
         (code['읍면동명']=='')]


df = api.get_data(
    property_type="아파트",
    trade_type="매매",
    sigungu_code="41135",
    year_month="202212",
    )
df.tail()

print(df)