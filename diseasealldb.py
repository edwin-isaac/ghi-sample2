import sqlite3
import pandas as pd

#conn = sqlite3.connect('ghi.db')
conn = sqlite3.connect('D:\GHI\ghi_website_2021/ghi.db')

conn.execute('''DROP TABLE IF EXISTS diseaseall2010''')
conn.execute('''DROP TABLE IF EXISTS diseaseall2013''')
conn.execute('''DROP TABLE IF EXISTS diseaseall2015''')


conn.execute('''CREATE TABLE diseaseall2010
             (country string, tb real, malaria real, hiv real, roundworm real, hookworm real, whipworm real, schistosomiasis real, onchocerciasis real, lf real)''')

conn.execute('''CREATE TABLE diseaseall2013
             (country string, tb real, malaria real, hiv real, roundworm real, hookworm real, whipworm real, schistosomiasis real, onchocerciasis real, lf real)''')

conn.execute('''CREATE TABLE diseaseall2015
             (country string, tb real, malaria real, hiv real, roundworm real, hookworm real, whipworm real, schistosomiasis real, onchocerciasis real, lf real)''')

def stripdata(x,y):
    tmp = df.iloc[x,y]
    print(tmp)
    if isinstance(tmp,float) == False:
        tmp = tmp.replace(',','').replace(' ','').replace('-','').replace(' ','0')
        if tmp == "":
            tmp = 0
        tmp = float(tmp)
        return(tmp)
    elif tmp != tmp:
        return(0)
    else:
        return(tmp)

def stripdata3(x,y):
    tmp = df_2010B_2015.iloc[x,y]
    print(tmp)
    if isinstance(tmp,float) == False:
        tmp = tmp.replace(',','').replace(' ','').replace('-','').replace(' ','0')
        if tmp == "":
            tmp = 0
        tmp = float(tmp)
        return(tmp)
    elif tmp != tmp:
        return(0)
    else:
        return(tmp)
#datasrc = 'https://docs.google.com/spreadsheets/d/1IBfN_3f-dG65YbLWQbkXojUxs2PlQyo7l04Ubz9kLkU/pub?gid=1996016204&single=true&output=csv'
#datasrc = 'https://docs.google.com/spreadsheets/d/1IBfN_3f-dG65YbLWQbkXojUxs2PlQyo7l04Ubz9kLkU/pub?gid=0&single=true&output=csv' # old link 04/26
datasrc = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSijEPfCc0nHZyzbPhXA5CUSKqRMTWerwWSvAlpf2ZiFD4GAgb_HZnfo8aoBP-EvXXM8lJXxZ5Sq8ai/pub?gid=0&single=true&output=csv'
#datasrc3 = 'https://docs.google.com/spreadsheets/d/1vwMReqs8G2jK-Cx2_MWKn85MlNjnQK-UR3Q8vZ_pPNk/pub?gid=0&single=true&output=csv' # old link 04/26
datasrc3 = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSTzH6iRaiUexi_w5bfVh_y2T8I8KRrfQINlcmgkSGLEmUt9Ih6rwpcxmjqkFdtvP1CXhonGN4f5P1M/pub?gid=0&single=true&output=csv'
df = pd.read_csv(datasrc, skiprows=1)
df_2010B_2015 = pd.read_csv(datasrc3, skiprows=1)

data2010 = []
data2013 = []

for i in range(1,216):
    country = df.iloc[i,0]

    print(country)
    tb = stripdata(i,1)
    malaria = stripdata(i,2)
    hiv = stripdata(i,3)
    roundworm = stripdata(i,4)
    hookworm = stripdata(i,5)
    whipworm = stripdata(i,6)
    schistosomiasis = stripdata(i,7)
    onchocerciasis = stripdata(i,8)
    lf = stripdata(i,9)
    row = [country,tb,malaria,hiv,roundworm,hookworm,whipworm,schistosomiasis,onchocerciasis,lf]
    data2010.append(row)

for i in range(1,216):
    country = df.iloc[i,11]
    tb = stripdata(i,12)
    malaria = stripdata(i,13)
    hiv = stripdata(i,14)
    roundworm = stripdata(i,15)
    hookworm = stripdata(i,16)
    whipworm = stripdata(i,17)
    schistosomiasis = stripdata(i,18)
    onchocerciasis = stripdata(i,19)
    lf = stripdata(i,20)
    row = [country,tb,malaria,hiv,roundworm,hookworm,whipworm,schistosomiasis,onchocerciasis,lf]
    data2013.append(row)

# print(data2013)
for row in data2010:
    conn.execute(' insert into diseaseall2010 values (?,?,?,?,?,?,?,?,?,?) ', (row))

for row in data2013:
    conn.execute(' insert into diseaseall2013 values (?,?,?,?,?,?,?,?,?,?) ', (row))

data2010B = []
data2015 = []
for i in range(1,217):
    country = df_2010B_2015.iloc[i,11]
    tb = stripdata3(i,12)
    malaria = stripdata3(i,13)
    hiv = stripdata3(i,14)
    roundworm = stripdata3(i,15)
    hookworm = stripdata3(i,16)
    whipworm = stripdata3(i,17)
    schistosomiasis = stripdata3(i,18)
    onchocerciasis = stripdata3(i,19)
    lf = stripdata3(i,20)
    row2015 = [country,tb,malaria,hiv,roundworm,hookworm,whipworm,schistosomiasis,onchocerciasis,lf]
    data2015.append(row2015)

# print(data2015)

for _row2015 in data2015:
    conn.execute(' insert into diseaseall2015 values (?,?,?,?,?,?,?,?,?,?) ', (_row2015))



conn.commit()
print("Database operation complete")
