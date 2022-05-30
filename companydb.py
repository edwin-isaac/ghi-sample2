import sqlite3
import pandas as pd
import math
def createTablesCompany():
    conn = sqlite3.connect('D:\GHI\ghi_website_2021/ghi.db')
    #conn = sqlite3.connect('ghi.db')

    conn.execute('''DROP TABLE IF EXISTS manudis''')
    conn.execute('''DROP TABLE IF EXISTS manudis_cost''')
    conn.execute('''DROP TABLE IF EXISTS manutot''')
    conn.execute('''DROP TABLE IF EXISTS patent2010''')
    conn.execute('''DROP TABLE IF EXISTS patent2013''')
    conn.execute('''DROP TABLE IF EXISTS patent2015''')
    conn.execute('''DROP TABLE IF EXISTS manudis2015''')
    conn.execute('''DROP TABLE IF EXISTS manutot2015''')
    conn.execute('''DROP TABLE IF EXISTS temppatent2010''')
    conn.execute('''DROP TABLE IF EXISTS company_size2010''')
    conn.execute('''DROP TABLE IF EXISTS company_size2013''')
    conn.execute('''DROP TABLE IF EXISTS company_size2015''')
    conn.execute('''DROP TABLE IF EXISTS manudis_cost_2013''')
    conn.execute('''DROP TABLE IF EXISTS manudis_cost_2015''')
    

    conn.execute('''CREATE TABLE manudis
                 (company text, disease text, daly2010 real, daly2013 real, color text)''')

    conn.execute('''CREATE TABLE manudis_cost
                 (company text, year text, cost_data real, color text)''')
    print("create copman")
    conn.execute('''CREATE TABLE company_size2010
                (company text, year text, size real, color text)''')

    conn.execute('''CREATE TABLE company_size2013
                (company text, year text, size real, color text)''')

    conn.execute('''CREATE TABLE company_size2015
                (company text, year text, size real, color text)''')

    conn.execute('''CREATE TABLE manudis_cost_2013
                (company text,  cost2013 real,  color text)''')
    conn.execute('''CREATE TABLE manudis_cost_2015
                 (company text,  cost2015 real, color text)''')

    conn.execute('''CREATE TABLE manutot
                 (company text, daly2010 real, daly2013 real, color text)''')

    conn.execute('''CREATE TABLE manudis2015
                 (company text, disease text, daly2010B real, daly2015 real, color text)''')
    conn.execute('''CREATE TABLE manutot2015
                 (company text, daly2010B real, daly2015 real, color text)''')
    conn.execute('''CREATE TABLE patent2010
                (company text, tb real, malaria real, hiv real, roundworm real, hookworm real, whipworm real, schistosomiasis real, onchocerciasis real, lf real, total real, color text)''')
    conn.execute('''CREATE TABLE patent2013
                (company text, tb real, malaria real, hiv real, roundworm real, hookworm real, whipworm real, schistosomiasis real, onchocerciasis real, lf real, total real, color text)''')
    conn.execute('''CREATE TABLE patent2015
                (company text, tb real, malaria real, hiv real, roundworm real, hookworm real, whipworm real, schistosomiasis real, onchocerciasis real, lf real, total real, color text)''')
    conn.execute('''CREATE TABLE temppatent2010
                (company text, year, tb real, malaria real, hiv real, roundworm real, hookworm real, whipworm real, schistosomiasis real, onchocerciasis real, lf real, total real, color text)''')

    # datasrc = 'https://docs.google.com/spreadsheets/d/1IBfN_3f-dG65YbLWQbkXojUxs2PlQyo7l04Ubz9kLkU/pub?gid=1560508440&single=true&output=csv'
    # datasrc20102015 = 'https://docs.google.com/spreadsheets/d/1vwMReqs8G2jK-Cx2_MWKn85MlNjnQK-UR3Q8vZ_pPNk/pub?gid=1560508440&single=true&output=csv'
    conn.commit()
    conn.close()


def companydbUpdate():
    try:
        conn = sqlite3.connect('D:\GHI\ghi_website_2021/ghi.db')
        #conn = sqlite3.connect('ghi_cost_test.db')
        #fconn = sqlite3.connect('ghi.db')
        # conn.execute('''DELETE FROM manudis_bkp''')
        # conn.execute('''DELETE FROM manutot_bkp''')
        # conn.execute('''DELETE FROM patent2010_bkp''')
        # conn.execute('''DELETE FROM patent2013_bkp''')
        # conn.execute('''DELETE FROM manudis2015_bkp''')
        # conn.execute('''DELETE FROM manutot2015_bkp''')
        # conn.execute('''DELETE FROM patent2015_bkp''')
        # conn.execute('''insert into manudis_bkp select * from manudis''')
        # conn.execute('''CREATE TABLE IF NOT EXISTS  manudis_cost (company text, year text, cost_data real, color text)''')
        # conn.execute('''CREATE TABLE IF NOT EXISTS company_size2010 (company text, year text, size real, color text)''')
        # conn.execute('''CREATE TABLE IF NOT EXISTS company_size2013 (company text, year text, size real, color text)''')
        # conn.execute('''CREATE TABLE IF NOT EXISTS company_size2015 (company text, year text, size real, color text)''')
        # #conn.execute('''insert into manudis_cost_bkp select * from manudis_cost_2010''')
        # #conn.execute('''insert into manudis_cost_bkp select * from manudis_cost_2013''')
        # #conn.execute('''insert into manudis_cost_bkp select * from manudis_cost_2015''')
        # conn.execute('''insert into manutot_bkp select * from manutot''')
        # conn.execute('''insert into patent2010_bkp select * from patent2010''')
        # conn.execute('''insert into patent2013_bkp select * from patent2013''')
        # conn.execute('''insert into manudis2015_bkp select * from manudis2015''')
        # conn.execute('''insert into manutot2015_bkp select * from manutot2015''')
        # conn.execute('''insert into patent2015_bkp select * from patent2015''')
        # # conn.execute('''DELETE FROM manufacturer2010''')
        # # conn.execute('''DELETE FROM manufacturer2013''')
        # conn.execute('''DELETE FROM manudis''')
        # conn.execute('''DELETE FROM manudis_cost''')
        # conn.execute('''DELETE FROM company_size2010''')
        # conn.execute('''DELETE FROM company_size2013''')
        # conn.execute('''DELETE FROM company_size2015''')
        # conn.execute('''DELETE FROM manutot''')
        # conn.execute('''DELETE FROM patent2010''')
        # conn.execute('''DELETE FROM patent2013''')
        # conn.execute('''DELETE FROM manudis2015''')
        # conn.execute('''DELETE FROM manutot2015''')
        # conn.execute('''DELETE FROM patent2015''')
        # #datasrc = 'https://docs.google.com/spreadsheets/d/1IBfN_3f-dG65YbLWQbkXojUxs2PlQyo7l04Ubz9kLkU/pub?gid=1560508440&single=true&output=csv' # old link 04/26
        datasrc = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSijEPfCc0nHZyzbPhXA5CUSKqRMTWerwWSvAlpf2ZiFD4GAgb_HZnfo8aoBP-EvXXM8lJXxZ5Sq8ai/pub?gid=1560508440&single=true&output=csv'
        #datasrc20102015 = 'https://docs.google.com/spreadsheets/d/1vwMReqs8G2jK-Cx2_MWKn85MlNjnQK-UR3Q8vZ_pPNk/pub?gid=1560508440&single=true&output=csv' # old link 04/26
        datasrc20102015 = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSTzH6iRaiUexi_w5bfVh_y2T8I8KRrfQINlcmgkSGLEmUt9Ih6rwpcxmjqkFdtvP1CXhonGN4f5P1M/pub?gid=1560508440&single=true&output=csv'
        dataCost='https://docs.google.com/spreadsheets/d/e/2PACX-1vTNh8UgKblwRqKKgkWyzen-8sk3QnBTFB0zMUpbiQhc1JenQw97i6bZxPXhF2AaID1HSqFGvwTHL1kK/pub?output=csv&single=true'
        dataSize='https://docs.google.com/spreadsheets/d/e/2PACX-1vQ0poDYIcl-aLMt7qKlhE0iVEzkitZ-iiLs06IKVQSXQILiDkUuCTtdd64m4Li1h0WHNiDTdg3uJxys/pub?gid=1932314227&single=true&output=csv'
        # datasrc = 'ORS_GlobalBurdenDisease_2010_2013.csv'
        # datasrc20102015 = 'ORS_GlobalBurdenDisease_2010B_2015.csv'
        url2010B2017 = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQLNsp6UJVQaYMo7KUueUGGd8Mj1AkzBDcU2ksqFdTm9JfptKrLHmy2aiKbC1b_yV0qLOIy4EAOtU_m/pub?gid=0&single=true&output=csv'
        df2017 = pd.read_csv(url2010B2017, skiprows=1)
        is_df2017_true = df2017.notnull()
        df = pd.read_csv(datasrc20102015, skiprows=1).fillna(value=0)
        df2015 = pd.read_csv(datasrc20102015, skiprows=1).fillna(value=0)
        dfCost = pd.read_csv(dataCost, skiprows=1).fillna(value=0)
        dfSize = pd.read_csv(dataSize, skiprows=0).fillna(value=0)

        #is_dfCost_true = dfCost.notnull()
        is_df2015_true = df2015.notnull()
        is_df_true = df.notnull()
        i = 0
        colorlist = []
        colors = ['FFB31C', '0083CA', 'EF3E2E', '003452', '86AAB9', 'CAEEFD', '546675', '8A5575', '305516', 'B78988',
                  'BAE2DA', 'B1345D', '5B75A7', '906F76', 'C0E188', 'DE9C2A', 'F15A22', '8F918B', 'F2C2B7', 'F7C406',
                  'B83F98', '548A9B', 'D86375', 'F1DBC6', '0083CA', '7A80A3', 'CA8566', 'A3516E', '1DF533', '510B95',
                  'DFF352', 'F2C883', 'E3744D', '26B2BE', '5006BA', 'B99BCF', 'DC2A5A', 'D3D472', '2A9DC4', 'C25C90',
                  '65A007', 'FE3289', 'C6DAB5', 'DDF6AC', 'B7E038', '1ADBBD', '3BC6D5', '0ACD57', '22419F', 'D47C5B',
                  '139A97', '1CDDD8', 'FF033D', '004444', 'C25C7D', 'B5A28F', 'C25C7D', '90BA3E', 'DA8709', 'B0B0CE',
                  '2D00DD', 'DD2D00', 'FAFDFD', ' F5FD2F', '0DC4E0', 'FFD700', 'CC263C', 'F5F5DC', '3D9C35', '00CC00',
                  'EAEAFF']
        for x in colors:
            y = '#' + x
            colorlist.append(y)

        # print(colorlist)

        def cleanfloat(var):
            # print(var)
            if var == '#REF!' or var == '-' or var == 'nan' or var == 0:
                var = 0
            elif type(var) != float:
                var = float(var.replace(',', ''))
            if var != var:
                var = 0
            return var

        def FloatOrZero(value):
            try:
                strVal = str(value)
                if '-' in strVal:
                    resVal = strVal.replace('-', '0')
                elif ',' in strVal:
                    resVal = strVal.replace(',', '')
                else:
                    resVal = strVal
                resVal = float(resVal)
                return resVal
            except:
                return 0

        patentdata = []
        i = 0
        for k in range(0, 20):
            companyName = dfSize.iloc[k,0]
            companySize2010 = dfSize.iloc[k,4]
            if companySize2010 == False:
                companySize2010 = 0
            else:
                companySize2010 = float(FloatOrZero(companySize2010))
            yr = '2010'
            if companySize2010 > 0:
                color = colors[i]
                row = [companyName, yr, companySize2010, color]
                patentdata.append(row)
              #  conn.execute(' INSERT INTO company_size2010 VALUES (?,?,?,?) ', row)

            companyName = dfSize.iloc[k, 6]
            companySize2013 = dfSize.iloc[k, 10]
            if companySize2013 == False:
                companySize2013 = 0
            else:
                companySize2013 = float(FloatOrZero(companySize2013))
            yr = '2013'
            if companySize2013 > 0:
                color = colors[i]
                row = [companyName, yr, companySize2013, color]
                patentdata.append(row)
                # conn.execute(' INSERT INTO company_size2013 VALUES (?,?,?,?) ', row)

            companyName = dfSize.iloc[k, 12]
            companySize2015 = dfSize.iloc[k,16]
            if companySize2015 == False:
                companySize2015 = 0
            else:
                companySize2015 = float(FloatOrZero(companySize2015))            
            yr = '2015'
            if companySize2015 > 0:
                color = colors[i]
                row = [companyName, yr, companySize2015, color]
                patentdata.append(row)
                # conn.execute(' INSERT INTO company_size2015 VALUES (?,?,?,?) ', row)
            i += 1   
            #conn.commit()
        
        manudata = []
        manutotal = []
        manu2015total = []

        i = 0
        for k in range(0, 63):
            companyCost = dfCost.iloc[k, 0]
            #print(companyCost)
            _k3 = dfCost.iloc[k, 1]
            if dfCost.iloc[k, 1] == False:
                temp1 = 0
            else:
                temp1 = FloatOrZero(_k3)

            tbdaly2010 = float(temp1)
            yr="2010"

            if tbdaly2010 > 0:
                color = colors[i]
                row = [companyCost, yr, tbdaly2010, color]
                manudata.append(row)
                #i += 1
                # conn.execute('insert into manudis_cost values (?,?,?,?)', row)

            companyCost = dfCost.iloc[k, 3]
            # print(companyCost)
            _k3 = dfCost.iloc[k, 4]
            if dfCost.iloc[k, 4] == False:
                temp1 = 0
            else:
                temp1 = FloatOrZero(_k3)

            tbdaly2013 = float(temp1)
            yr="2013"

            if tbdaly2013 > 0:
                color = colors[i]
                row = [companyCost, yr, tbdaly2013, color]
                manudata.append(row)
                #i += 1
                # conn.execute('insert into manudis_cost values (?,?,?,?)', row)

            companyCost = dfCost.iloc[k, 6]
            #print(companyCost)
            #print(k)
            _k3 = dfCost.iloc[k, 7]
            #print(_k3)
            if dfCost.iloc[k, 7] == False:
                temp1 = 0
            else:
                temp1 = FloatOrZero(_k3)

            tbdaly2015 = float(temp1)
            yr="2015"

            if tbdaly2015 > 0:
                color = colors[i]
                row = [companyCost, yr, tbdaly2015, color]
                manudata.append(row)
                # conn.execute('insert into manudis_cost values (?,?,?,?)', row)
            i += 1
            # for item in manudata:
            #     print(item)


        i = 0
        for k in range(25, 50):
            company = df.iloc[k, 2]
            companyCost = dfCost.iloc[k, 2]
            # print(company)
            # print(companyCost)
            if isinstance(company, float):
                if math.isnan(company):
                    break
            disease = 'TB'

            _k3 = df.iloc[k, 3]
            if is_df_true.iloc[k, 3] == False:
                temp1 = 0
            else:
                temp1 = FloatOrZero(_k3)

            tbdaly2010 = float(temp1)

            _k4 = df.iloc[k, 4]
            if is_df_true.iloc[k, 4] == False:
                temp2 = 0
            else:
                temp2 = FloatOrZero(_k4)

            tbdaly2013 = float(temp2)

            if tbdaly2010 > 0 or tbdaly2013 > 0:
                color = colors[i]
                row = [company, disease, tbdaly2010, tbdaly2013, color]
                manudata.append(row)
                i += 1
                # conn.execute('insert into manudis values (?,?,?,?,?)', row)

            # for item in manudata:
            #     print(item)

        i = 0
        for k in range(25, 50):
            company = df.iloc[k, 5]
            if isinstance(company, float):
                if math.isnan(company):
                    break
            disease = 'HIV'
            _k10 = df.iloc[k, 6]
            if is_df_true.iloc[k, 6] == False:
                temph = 0
            else:
                temph = FloatOrZero(_k10)

            hivdaly2010 = float(temph)

            k11 = str(df.iloc[k, 7])
            if is_df_true.iloc[k, 7] == False:
                temph1 = 0
            else:
                temph1 = FloatOrZero(k11)

            hivdaly2013 = float(temph1)
            if hivdaly2010 > 0 or hivdaly2013 > 0:
                color = colors[i]
                row = [company, disease, hivdaly2010, hivdaly2013, color]
                i += 1
                manudata.append(row)
                # conn.execute('insert into manudis values (?,?,?,?,?)', row)

        i = 0
        for k in range(25, 66):
            company = df.iloc[k, 8]
            if isinstance(company, float):
                if math.isnan(company):
                    break
            disease = 'Malaria'
            _k10 = df.iloc[k, 9]
            if is_df_true.iloc[k, 9] == False:
                temph = 0
            else:
                temph = FloatOrZero(_k10)

            hivdaly2010 = float(temph)

            k11 = df.iloc[k, 10]
            if is_df_true.iloc[k, 10] == False:
                temph1 = 0
            else:
                temph1 = FloatOrZero(k11)

            hivdaly2013 = float(temph1)
            if hivdaly2010 > 0 or hivdaly2013 > 0:
                color = colors[i]
                row = [company, disease, hivdaly2010, hivdaly2013, color]
                i += 1
                manudata.append(row)
                # conn.execute('insert into manudis values (?,?,?,?,?)', row)

        for j in range(8, 14):
            if j == 8:
                unmet = ['Unmet Need']
                disease = 'TB'
                unmet.append(disease)
                tb1 = cleanfloat(df.iloc[8, 46])
                tb2 = cleanfloat(df.iloc[9, 46])
                tb3 = cleanfloat(df.iloc[10, 46])
                tb = [tb1, tb2, tb3]
                temp = (tb1 + tb2 + tb3)
                unmet.append(temp)
                # this is just a temporary value because I dont know what to put here as database is taking 5 values
                unmet.append(0)
                unmet.append('a6a6a6')
                # conn.execute('insert into manudis values (?,?,?,?,?)', unmet)
            elif j == 9 or j == 10 or j == 12:
                aa = 1
            elif j == 11:
                unmet = ['Unmet Need']
                disease = 'Malaria'
                unmet.append(disease)
                mal1 = cleanfloat(df.iloc[11, 46])
                mal2 = cleanfloat(df.iloc[12, 46])
                mal = [mal1, mal2]
                temp = (mal1 + mal2)
                unmet.append(temp)
                # this is just a temporary value because I dont know what to put here as database is taking 5 values
                unmet.append(0)
                unmet.append('a6a6a6')
                # conn.execute('insert into manudis values (?,?,?,?,?)', unmet)
            elif j == 13:
                unmet = ['Unmet Need']
                disease = 'HIV'
                unmet.append(disease)
                hivtemp = cleanfloat(df.iloc[13, 46])
                unmet.append(hivtemp)
                # this is just a temporary value because I dont know what to put here as database is taking 5 values
                unmet.append(0)
                unmet.append('a6a6a6')
                # conn.execute('insert into manudis values (?,?,?,?,?)', unmet)

        for j in range(8, 14):
            if j == 8:
                unmet = ['Unmet Need']
                disease = 'TB'
                unmet.append(disease)
                tb1 = cleanfloat(df.iloc[8, 97])
                tb2 = cleanfloat(df.iloc[9, 97])
                tb3 = cleanfloat(df.iloc[10, 97])
                tb = [tb1, tb2, tb3]
                temp = (tb1 + tb2 + tb3)
                unmet.append(0)
                unmet.append(temp)
                # this is just a temporary value because I dont know what to put here as database is taking 5 values
                unmet.append('a6a6a6')
                # conn.execute('insert into manudis values (?,?,?,?,?)', unmet)
            elif j == 9 or j == 10 or j == 12:
                aa = 1
            elif j == 11:
                unmet = ['Unmet Need']
                disease = 'Malaria'
                unmet.append(disease)
                mal1 = cleanfloat(df.iloc[11, 97])
                mal2 = cleanfloat(df.iloc[12, 97])
                mal = [mal1, mal2]
                temp = (mal1 + mal2)
                unmet.append(0)
                unmet.append(temp)
                # this is just a temporary value because I dont know what to put here as database is taking 5 values
                unmet.append('a6a6a6')
                # conn.execute('insert into manudis values (?,?,?,?,?)', unmet)
            elif j == 13:
                unmet = ['Unmet Need']
                disease = 'HIV'
                unmet.append(disease)
                hivtemp = cleanfloat(df.iloc[13, 97])
                unmet.append(0)
                unmet.append(hivtemp)
                # this is just a temporary value because I dont know what to put here as database is taking 5 values
                unmet.append('a6a6a6')
                # conn.execute('insert into manudis values (?,?,?,?,?)', unmet)
        i = 0
        for k in range(26, 50):
            company = df2015.iloc[k, 2]
            if isinstance(company, float):
                if math.isnan(company):
                    break
            disease = 'TB'

            _k3 = df2015.iloc[k, 3]
            if is_df2015_true.iloc[k, 3] == False:
                temp1 = 0
            else:
                temp1 = FloatOrZero(_k3)

            tbdaly2010B = float(temp1)

            _k4 = df2015.iloc[k, 4]
            if is_df2015_true.iloc[k, 4] == False:
                temp2 = 0
            else:
                temp2 = FloatOrZero(_k4)

            tbdaly2015 = float(temp2)

            if tbdaly2010B > 0 or tbdaly2015 > 0:
                color = colors[i]
                row = [company, disease, tbdaly2010B, tbdaly2015, color]
                manudata.append(row)
                i += 1
                # conn.execute('insert into manudis2015 values (?,?,?,?,?)', row)
        i = 0
        for k in range(26, 52):
            company = df2015.iloc[k, 5]
            if isinstance(company, float):
                if math.isnan(company):
                    break
            disease = 'HIV'
            _k6 = df2015.iloc[k, 6]
            if is_df2015_true.iloc[k, 6] == False:
                temph = 0
            else:
                temph = FloatOrZero(_k6)

            hivdaly2010B = float(temph)

            k7 = df2015.iloc[k, 7]
            if is_df2015_true.iloc[k, 7] == False:
                temph1 = 0
            else:
                temph1 = FloatOrZero(k7)

            hivdaly2015 = float(temph1)
            if hivdaly2010B > 0 or hivdaly2015 > 0:
                color = colors[i]
                row = [company, disease, hivdaly2010B, hivdaly2015, color]
                i += 1
                manudata.append(row)
                # conn.execute('insert into manudis2015 values (?,?,?,?,?)', row)

        for k in range(25, 66):
            company = df2015.iloc[k, 8]
            if isinstance(company, float):
                if math.isnan(company):
                    break
            disease = 'Malaria'
            _k10 = df2015.iloc[k, 9]
            if is_df_true.iloc[k, 9] == False:
                temph = 0
            else:
                temph = FloatOrZero(_k10)

            malariaDaly2010 = float(temph)

            k11 = df2015.iloc[k, 10]
            if is_df_true.iloc[k, 10] == False:
                temph1 = 0
            else:
                temph1 = FloatOrZero(k11)

            malariadaly2013 = float(temph1)
            if malariaDaly2010 > 0 or malariadaly2013 > 0:
                color = colors[i]
                row = [company, disease, malariaDaly2010, malariadaly2013, color]
                i += 1
                manudata.append(row)
                # conn.execute('insert into manudis2015 values (?,?,?,?,?)', row)

        for j in range(8, 14):
            if j == 8:
                unmet = ['Unmet Need']
                disease = 'TB'
                unmet.append(disease)
                tb1 = cleanfloat(df2015.iloc[8, 97]) #98 changed to 97
                tb2 = cleanfloat(df2015.iloc[9, 97]) #98 changed to 97
                tb3 = cleanfloat(df2015.iloc[10, 97]) #98 changed to 97
                tb = [tb1, tb2, tb3]
                temp = (tb1 + tb2 + tb3)
                unmet.append(0)
                unmet.append(temp)
                # this is just a temporary value because I dont know what to put here as database is taking 5 values
                unmet.append('a6a6a6')
                # conn.execute('insert into manudis2015 values (?,?,?,?,?)', unmet)
            elif j == 9 or j == 10 or j == 12:
                aa = 1
            elif j == 11:
                unmet = ['Unmet Need']
                disease = 'Malaria'
                unmet.append(disease)
                mal1 = cleanfloat(df2015.iloc[11, 97])  #98 changed to 97
                mal2 = cleanfloat(df2015.iloc[12, 97])  #98 changed to 97
                mal = [mal1, mal2]
                temp = (mal1 + mal2)
                unmet.append(0)
                unmet.append(temp)
                # this is just a temporary value because I dont know what to put here as database is taking 5 values
                unmet.append('a6a6a6')
                # conn.execute('insert into manudis2015 values (?,?,?,?,?)', unmet)
            elif j == 13:
                unmet = ['Unmet Need']
                disease = 'HIV'
                unmet.append(disease)
                hivtemp = cleanfloat(df2015.iloc[13, 97])  #98 changed to 97
                unmet.append(0)
                unmet.append(hivtemp)
                # this is just a temporary value because I dont know what to put here as database is taking 5 values
                unmet.append('a6a6a6')
                # conn.execute('insert into manudis2015 values (?,?,?,?,?)', unmet)

        ###############################PATENT PATENT PATENT CODE BELOW ######################################################################
        ###############################PATENT PATENT PATENT CODE BELOW ######################################################################

        oldrow = ['']
        pat2010 = []
        for i in range(1, 43):
            prow = []
            comp = df.iloc[1, i]
            prow.append(comp)
            for j in range(8, 21):
                if j == 8:
                    tb1 = cleanfloat(df.iloc[8, i])
                    tb2 = cleanfloat(df.iloc[9, i])
                    tb3 = cleanfloat(df.iloc[10, i])
                    tb = [tb1, tb2, tb3]
                    temp = (tb1 + tb2 + tb3)
                    prow.append(temp)
                elif j == 9 or j == 10 or j == 12:
                    aa = 1
                elif j == 11:
                    mal1 = cleanfloat(df.iloc[11, i])
                    mal2 = cleanfloat(df.iloc[12, i])
                    mal = [mal1, mal2]
                    temp = (mal1 + mal2)
                    prow.append(temp)
                elif j == 20:
                    total = cleanfloat(df.iloc[j, i])
                    prow.append(total)
                else:
                    temp = df.iloc[j, i]
                    if isinstance(temp, float) == False and isinstance(temp, int) == False:
                        temp = float(temp.replace(',', ''))
                    if temp != temp:
                        temp = 0
                    prow.append(temp)
            if prow[0] == oldrow[0]:
                for ind in range(1, len(prow)):
                    prow[ind] += oldrow[ind]
            oldrow = prow
            if comp != df.iloc[1, i + 1]:
                pat2010.append(prow)
        unmet = ['Unmet Need']
        for j in range(8, 21):
            if j == 8:
                # print(df.iloc[7,46])
                tb1 = cleanfloat(df.iloc[8, 46])
                tb2 = cleanfloat(df.iloc[9, 46])
                tb3 = cleanfloat(df.iloc[10, 46])
                tb = [tb1, tb2, tb3]
                temp = (tb1 + tb2 + tb3)
                unmet.append(temp)
            elif j == 9 or j == 10 or j == 11:
                aa = 1
            elif j == 12:
                mal1 = cleanfloat(df.iloc[11, 46])
                mal2 = cleanfloat(df.iloc[12, 46])
                mal = [mal1, mal2]
                temp = (mal1 + mal2)
                unmet.append(temp)
            elif j == 20:
                total = cleanfloat(df.iloc[j, 46])
                unmet.append(total)
            else:
                temp = df.iloc[j, 46]
                if isinstance(temp, float) == False and isinstance(temp, int) == False:
                    temp = float(temp.replace(',', ''))
                if temp != temp:
                    temp = 0
                unmet.append(temp)
        pat2010.append(unmet)
        colind = 0
        for item in pat2010:
            if item[0] == 'Unmet Need':
                item.append('a6a6a6')
            else:
                item.append(colors[colind])
                # print(colors[colind])
            colind += 1
            conn.execute(' insert into patent2010 values (?,?,?,?,?,?,?,?,?,?,?,?) ', item)
        # print(pat2010)

        oldrow = ['']
        pat2013 = []
        for i in range(50, 96):
            prow = []
            comp = df.iloc[1, i]
            prow.append(comp)
            for j in range(8, 21):
                if j == 8:
                    tb1 = cleanfloat(df.iloc[8, i])
                    tb2 = cleanfloat(df.iloc[9, i])
                    tb3 = cleanfloat(df.iloc[10, i])
                    tb = [tb1, tb2, tb3]
                    temp = (tb1 + tb2 + tb3)
                    prow.append(temp)
                elif j == 9 or j == 10 or j == 12:
                    aa = 1
                elif j == 11:
                    mal1 = cleanfloat(df.iloc[11, i])
                    mal2 = cleanfloat(df.iloc[12, i])
                    mal = [mal1, mal2]
                    temp = (mal1 + mal2)
                    prow.append(temp)
                elif j == 20:
                    total = cleanfloat(df.iloc[j, i])
                    prow.append(total)
                else:
                    temp = df.iloc[j, i]
                    if isinstance(temp, float) == False and isinstance(temp, int) == False:
                        temp = float(temp.replace(',', ''))
                    if temp != temp:
                        temp = 0
                    prow.append(temp)
            if prow[0] == oldrow[0]:
                for ind in range(1, len(prow)):
                    prow[ind] += oldrow[ind]
            oldrow = prow
            if comp != df.iloc[1, i + 1]:
                pat2013.append(prow)
        unmet = ['Unmet Need']
        for j in range(8, 21):
            if j == 8:
                # print(df.iloc[8,93])
                tb1 = cleanfloat(df.iloc[8, 97])
                tb2 = cleanfloat(df.iloc[9, 97])
                tb3 = cleanfloat(df.iloc[10, 97])
                tb = [tb1, tb2, tb3]
                temp = (tb1 + tb2 + tb3)
                unmet.append(temp)
            elif j == 11:
                mal1 = cleanfloat(df.iloc[11, 97])
                mal2 = cleanfloat(df.iloc[12, 97])
                mal = [mal1, mal2]
                temp = (mal1 + mal2)
                unmet.append(temp)
            elif j == 20:
                total = cleanfloat(df.iloc[j, 97])
                unmet.append(total)
            elif j == 9 or j == 10 or j == 12:
                aa = 1
            else:
                temp = df.iloc[j, 97]
                if isinstance(temp, float) == False and isinstance(temp, int) == False:
                    temp = float(temp.replace(',', ''))
                if temp != temp:
                    temp = 0
                unmet.append(temp)
        pat2013.append(unmet)
        colind = 0
        for item in pat2013:
            if item[0] == 'Unmet Need':
                item.append('a6a6a6')
            else:
                item.append(colors[colind])
                # print(colors[colind])
            colind += 1
            # conn.execute(' insert into patent2013 values (?,?,?,?,?,?,?,?,?,?,?,?) ', item)
        # print(pat2013)

        oldrow = ['']
        pat2015 = []
        for i in range(50, 98):
            prow = []
            comp = df2015.iloc[1, i]
            prow.append(comp)
            for j in range(8, 21):
                if j == 8:
                    if is_df2015_true.iloc[8, i] == True:
                        tb1 = cleanfloat(df2015.iloc[8, i])
                    else:
                        tb1 = 0
                    if is_df2015_true.iloc[9, i] == True:
                        tb2 = cleanfloat(df2015.iloc[9, i])
                    else:
                        tb2 = 0
                    if is_df2015_true.iloc[10, i] == True:
                        tb3 = cleanfloat(df2015.iloc[10, i])
                    else:
                        tb3 = 0
                    tb = [tb1, tb2, tb3]
                    temp = (tb1 + tb2 + tb3)
                    prow.append(temp)
                elif j == 9 or j == 10 or j == 12:
                    aa = 1
                elif j == 11:
                    if is_df2015_true.iloc[11, i] == True:
                        mal1 = cleanfloat(df2015.iloc[11, i])
                    else:
                        mal1 = 0
                    if is_df2015_true.iloc[12, i] == True:
                        mal2 = cleanfloat(df2015.iloc[12, i])
                    else:
                        mal2 = 0
                    mal = [mal1, mal2]
                    temp = (mal1 + mal2)
                    prow.append(temp)
                elif j == 20:
                    if is_df2015_true.iloc[j, i] == True:
                        total = cleanfloat(df2015.iloc[j, i])
                    else:
                        total = 0
                    prow.append(total)
                else:
                    temp = df2015.iloc[j, i]
                    if temp == '-' or temp == '#REF!':
                        temp = 0
                    if isinstance(temp, float) == False and isinstance(temp, int) == False:
                        temp = float(temp.replace(',', ''))
                    if temp != temp:
                        temp = 0
                    prow.append(temp)
            if prow[0] == oldrow[0]:
                for ind in range(1, len(prow)):
                    prow[ind] += oldrow[ind]
            oldrow = prow
            if comp != df2015.iloc[1, i + 1]:
                pat2015.append(prow)
        unmet = ['Unmet Need']
        for j in range(8, 21):
            if j == 8:
                # print(df2015.iloc[8, 97]) #98 changed to 97
                if is_df2015_true.iloc[8, 97] == True: #98 changed to 97
                    tb1 = cleanfloat(df2015.iloc[8, 97])
                else:
                    tb1 = 0
                if is_df2015_true.iloc[9, 97] == True: #98 changed to 97
                    tb2 = cleanfloat(df2015.iloc[9, 97]) #98 changed to 97
                else:
                    tb2 = 0
                if is_df2015_true.iloc[10, 97] == True: #98 changed to 97
                    tb3 = cleanfloat(df2015.iloc[10, 97]) #98 changed to 97
                else:
                    tb3 = 0
                tb = [tb1, tb2, tb3]
                temp = (tb1 + tb2 + tb3)
                unmet.append(temp)
            elif j == 9 or j == 10 or j == 12:
                aa = 1
            elif j == 11:
                if is_df2015_true.iloc[11, 97] == True: #98 changed to 97
                    mal1 = cleanfloat(df2015.iloc[11, 97]) #98 changed to 97
                else:
                    mall = 0
                if is_df2015_true.iloc[12, 97] == True: #98 changed to 97
                    mal2 = cleanfloat(df2015.iloc[12, 97]) #98 changed to 97
                else:
                    mal2 = 0
                mal = [mal1, mal2]
                temp = (mal1 + mal2)
                unmet.append(temp)
            elif j == 20:
                if is_df2015_true.iloc[j, 97] == True: #98 changed to 97
                    total = cleanfloat(df2015.iloc[j, 97]) #98 changed to 97
                else:
                    total = 0
                unmet.append(total)
            else:
                temp = df2015.iloc[j, 97] #98 changed to 97
                if temp == '-' or temp == '#REF!':
                    temp = 0
                if isinstance(temp, float) == False and isinstance(temp, int) == False:
                    temp = float(temp.replace(',', ''))
                if temp != temp:
                    temp = 0
                unmet.append(temp)
        pat2015.append(unmet)
        colind = 0
        for item in pat2015:
            if item[0] == 'Unmet Need':
                item.append('a6a6a6')
            else:
                item.append(colors[colind])
                # print(colors[colind])
            colind += 1
            # conn.execute(' insert into patent2015 values (?,?,?,?,?,?,?,?,?,?,?,?) ', item)
        # This is to calculate data for 2010B and 2015

        ##############   END OF PATENT CODE  ############################################################################
        ##############   END OF PATENT CODE  ############################################################################

        conn.commit()
        # pat2015 = []
        # for i in range(112, 158):
        #     prow = []
        #     comp = df2017.iloc[1, i]
        #     prow.append(comp)
        #     for j in range(8, 21):
        #         if j == 8:
        #             if is_df2017_true.iloc[8, i] == True:
        #                 tb1 = cleanfloat(df2015.iloc[8, i])
        #             else:
        #                 tb1 = 0
        #             if is_df2017_true.iloc[9, i] == True:
        #                 tb2 = cleanfloat(df2015.iloc[9, i])
        #             else:
        #                 tb2 = 0
        #             if is_df2017_true.iloc[10, i] == True:
        #                 tb3 = cleanfloat(df2015.iloc[10, i])
        #             else:
        #                 tb3 = 0
        #             tb = [tb1, tb2, tb3]
        #             temp = (tb1 + tb2 + tb3)
        #             prow.append(temp)
        #         elif j == 9 or j == 10 or j == 12:
        #             aa = 1
        #         elif j == 11:
        #             if is_df2017_true.iloc[11, i] == True:
        #                 mal1 = cleanfloat(df2015.iloc[11, i])
        #             else:
        #                 mal1 = 0
        #             if is_df2017_true.iloc[12, i] == True:
        #                 mal2 = cleanfloat(df2015.iloc[12, i])
        #             else:
        #                 mal2 = 0
        #             mal = [mal1, mal2]
        #             temp = (mal1 + mal2)
        #             prow.append(temp)
        #         elif j == 20:
        #             if is_df2017_true.iloc[j, i] == True:
        #                 total = cleanfloat(df2015.iloc[j, i])
        #             else:
        #                 total = 0
        #             prow.append(total)
        #         else:
        #             temp = df2017.iloc[j, i]
        #             if temp == '-' or temp == '#REF!':
        #                 temp = 0
        #             if isinstance(temp, float) == False and isinstance(temp, int) == False:
        #                 temp = float(temp.replace(',', ''))
        #             if temp != temp:
        #                 temp = 0
        #             prow.append(temp)
        #     if prow[0] == oldrow[0]:
        #         for ind in range(1, len(prow)):
        #             prow[ind] += oldrow[ind]
        #     oldrow = prow
        #     if comp != df2017.iloc[1, i + 1]:
        #         pat2015.append(prow)
        # unmet = ['Unmet Need']
        # for j in range(8, 21):
        #     if j == 8:
        #         # print(df2015.iloc[8, 97]) #98 changed to 97
        #         if is_df2017_true.iloc[8, 97] == True: #98 changed to 97
        #             tb1 = cleanfloat(df2015.iloc[8, 97])
        #         else:
        #             tb1 = 0
        #         if is_df2017_true.iloc[9, 97] == True: #98 changed to 97
        #             tb2 = cleanfloat(df2015.iloc[9, 97]) #98 changed to 97
        #         else:
        #             tb2 = 0
        #         if is_df2017_true.iloc[10, 97] == True: #98 changed to 97
        #             tb3 = cleanfloat(df2015.iloc[10, 97]) #98 changed to 97
        #         else:
        #             tb3 = 0
        #         tb = [tb1, tb2, tb3]
        #         temp = (tb1 + tb2 + tb3)
        #         unmet.append(temp)
        #     elif j == 9 or j == 10 or j == 12:
        #         aa = 1
        #     elif j == 11:
        #         if is_df2017_true.iloc[11, 97] == True: #98 changed to 97
        #             mal1 = cleanfloat(df2015.iloc[11, 97]) #98 changed to 97
        #         else:
        #             mall = 0
        #         if is_df2017_true.iloc[12, 97] == True: #98 changed to 97
        #             mal2 = cleanfloat(df2015.iloc[12, 97]) #98 changed to 97
        #         else:
        #             mal2 = 0
        #         mal = [mal1, mal2]
        #         temp = (mal1 + mal2)
        #         unmet.append(temp)
        #     elif j == 20:
        #         if is_df2017_true.iloc[j, 97] == True: #98 changed to 97
        #             total = cleanfloat(df2015.iloc[j, 97]) #98 changed to 97
        #         else:
        #             total = 0
        #         unmet.append(total)
        #     else:
        #         temp = df2017.iloc[j, 97] #98 changed to 97
        #         if temp == '-' or temp == '#REF!':
        #             temp = 0
        #         if isinstance(temp, float) == False and isinstance(temp, int) == False:
        #             temp = float(temp.replace(',', ''))
        #         if temp != temp:
        #             temp = 0
        #         unmet.append(temp)
        # pat2015.append(unmet)
        # colind = 0
        # for item in pat2015:
        #     if item[0] == 'Unmet Need':
        #         item.append('a6a6a6')
        #     else:
        #         item.append(colors[colind])
        #         # print(colors[colind])
        #     colind += 1
        #     # conn.execute(' insert into patent2015 values (?,?,?,?,?,?,?,?,?,?,?,?) ', item)
        # # This is to calculate data for 2010B and 2015
        #
        # ##############   END OF PATENT CODE  ############################################################################
        # ##############   END OF PATENT CODE  ############################################################################
        # dfout = pd.DataFrame(pat2015)
        #
        # # saving the dataframe
        # dfout.to_csv('patent2017.csv')
        # conn.commit()
        conn.close()
        return 'success'
    except Exception as e:
        error = "Company page not updated"
        print(e)
        conn.rollback()
        conn.close()
        return e

#createTablesCompany()
#companydbUpdate()
