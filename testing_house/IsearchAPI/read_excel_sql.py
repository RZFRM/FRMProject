import pandas as pd
import numpy as np

sql_info = pd.read_excel(r'C:\Users\HipWang\Desktop\case_modules.xlsx')
data_x = np.array(sql_info)

# print(data_x.tolist())
for i in data_x:
    # print(tuple(i))
    i[3] = str(i[3])
    i[7] = str(i[7])
    i[5] = str(i[5])
    i[8] = str(i[8])
    i[9] = str(i[9])
    i[10] = str(i[10])
    i[13] = str(i[13])
    i[12]  =str(i[12]).split(' ')[0:9][0]
    # i[13]  =str(i[13]).split(' ')[0:9][0]
    # i[16]  =str(i[16]).split(' ')[0:9][0]
    i[15]  =str(i[15]).split(' ')[0:9][0]
    i[17]  =str(i[17]).split(' ')[0:9][0]
    # i[19]  =str(i[19]).split(' ')[0:9][0]
    # i[18]  =str(i[18]).split(' ')[0:9][0]


    print(tuple(i),',')



