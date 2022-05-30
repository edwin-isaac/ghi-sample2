# A script to generate CSVs for 2010,2013,2015,2017 drugr tables.
# It also writes to database pointed by conn variable, in this case ghi2.db.


import sqlite3
import sys

import pandas as pd
import math

def CreateDrugTable2010():

 conn = sqlite3.connect('D:\GHI\ghi_website_2021/ghi.db')

 conn.execute('''DROP TABLE IF EXISTS drugr2010''')
 #conn.execute('''DROP TABLE IF EXISTS drugpie2017''')

 conn.execute('''CREATE TABLE drugr2010
             (drug text, company text, tb real, malaria real, hiv real, roundworm real, hookworm real, whipworm real, schistosomiasis real, onchocerciasis real, lf real, total real)''')

 conn.commit()
 conn.close()

def CreateDrugTable2013():
    conn = sqlite3.connect('D:\GHI\ghi_website_2021/ghi2.db')
    conn.execute('''DROP TABLE IF EXISTS drugr2013''')
    conn.execute('''CREATE TABLE drugr2013
              (drug text, company text, tb real, malaria real, hiv real, roundworm real, hookworm real, whipworm real, schistosomiasis real, onchocerciasis real, lf real, total real)''')

    conn.commit()
    conn.close()

def CreateDrugTable2015():
    conn = sqlite3.connect('D:\GHI\ghi_website_2021/ghi2.db')
    conn.execute('''DROP TABLE IF EXISTS drugr2015''')
    conn.execute('''CREATE TABLE drugr2015
              (drug text, company text, tb real, malaria real, hiv real, roundworm real, hookworm real, whipworm real, schistosomiasis real, onchocerciasis real, lf real, total real)''')

    conn.commit()
    conn.close()

def CreateDrugTable2017():

 conn = sqlite3.connect('D:\GHI\ghi_website_2021/ghi.db')

 conn.execute('''DROP TABLE IF EXISTS drugr2017''')
 #conn.execute('''DROP TABLE IF EXISTS drugpie2017''')


 conn.execute('''CREATE TABLE drugr2017
             (drug text, company text, tb real, malaria real, hiv real, roundworm real, hookworm real, whipworm real, schistosomiasis real, onchocerciasis real, lf real, Trachoma real,  Hep_C real, total real)''')

 conn.commit()
 conn.close()


def cleanfloat(var):
    if var == '#REF!':
        var = 0
    if type(var) != float and type(var) != int:
        var = float(var.replace(',', ''))
    if var != var:
        var = 0
    return var

def DrugDbUpdate2010():

    try:
        conn = sqlite3.connect('D:\GHI\ghi_website_2021/ghi2.db')
        # conn = sqlite3.connect('mysite/ghi.db')
        # conn = sqlite3.connect('ghi.db')
        # conn.execute('''DELETE FROM drugr2010_bkp''')
        # conn.execute('''DELETE FROM drugr2013_bkp''')
        # conn.execute('''DELETE FROM drugr2015_bkp''')
        #
        # conn.execute('''INSERT INTO drugr2010_bkp SELECT * FROM drugr2010''')
        # conn.execute('''INSERT INTO drugr2013_bkp SELECT * FROM drugr2013''')
        # conn.execute('''INSERT INTO drugr2015_bkp SELECT * FROM drugr2015''')
        #
        # conn.execute('''DELETE FROM drugr2010''')
        # conn.execute('''DELETE FROM drugr2013''')
        # conn.execute('''DELETE FROM drugr2015''')
        # datasrc = 'https://docs.google.com/spreadsheets/d/1IBfN_3f-dG65YbLWQbkXojUxs2PlQyo7l04Ubz9kLkU/pub?gid=1560508440&single=true&output=csv' # old link 04/24
        datasrc = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSijEPfCc0nHZyzbPhXA5CUSKqRMTWerwWSvAlpf2ZiFD4GAgb_HZnfo8aoBP-EvXXM8lJXxZ5Sq8ai/pub?gid=1560508440&single=true&output=csv'
        df = pd.read_csv(datasrc, skiprows=1)
        drugdata = []
        drugrdata = []
        drug2010 = []
        perc2010 = []


        for i in range(1, 44):
            drugr = []
            name = df.iloc[5, i]
            print(name)
            drugr.append(name)
            company = df.iloc[1, i]
            print(company)
            drugr.append(company)
            for j in range(10, 20):
                if j == 10: #TB
                    tb1 = cleanfloat(df.iloc[8, i])
                    tb2 = cleanfloat(df.iloc[9, i])
                    tb3 = cleanfloat(df.iloc[10, i])
                    temp = (tb1 + tb2 + tb3)
                    drugr.append(temp)
                elif j == 11:
                    mal1 = cleanfloat(df.iloc[11, i])
                    mal2 = cleanfloat(df.iloc[12, i])
                    temp = (mal1 + mal2)
                    drugr.append(temp)
                elif j == 19:
                    total = cleanfloat(df.iloc[j + 1, i])
                    zz = [name, total]
                    perc2010.append(zz)
                else:
                    temp = df.iloc[j + 1, i]
                    if isinstance(temp, float) == False and isinstance(temp, int) == False:
                        temp = float(temp.replace(',', ''))
                    if temp != temp:
                        temp = 0
                    drugr.append(temp)
                if int(temp) > 0:
                    if j == 10:
                        disease = 'TB'
                        color = 'FFB31C'
                    elif j == 11 or j == 12:
                        disease = 'Malaria'
                        color = '0083CA'
                    elif j == 13:
                        disease = 'HIV'
                        color = 'EF3E2E'
                    elif j == 14:
                        disease = 'Roundworm'
                        color = '003452'
                    elif j == 15:
                        disease = 'Hookworm'
                        color = '86AAB9'
                    elif j == 16:
                        disease = 'Whipworm'
                        color = 'CAEEFD'
                    elif j == 17:
                        disease = 'Schistosomiasis'
                        color = '546675'
                    elif j == 18:
                        disease = 'Onchocerasis'
                        color = '8A5575'
                    elif j == 19:
                        disease = 'LF'
                        color = '305516'
                    company = df.iloc[1, i]
                    drugrow = [name, company, disease, temp, color]
                    drug2010.append(drugrow)

            if isinstance(df.iloc[20, i], float) == False:
                score = float(df.iloc[20, i].replace(',', ''))
            else:
                score = df.iloc[20, i]
            row = [name, score]
            drugdata.append(row)
            drugrdata.append(drugr)

        unmet = ['Unmet Need', 'Unmet Need']
        unmetsum = 0
        for xx in [[8, 9, 10], [11, 12], [13], [14], [15], [16], [17], [18], [19]]:
            val = 0
            for yy in xx:
                t = df.iloc[yy, 46] #47 changed to 46
                if isinstance(t, float) == False and isinstance(t, int) == False:
                    t = float(t.replace(',', ''))
                if t != t:
                    t = 0
                val += t
            unmet.append(val)
            unmetsum += val
        # print(unmet)
        # print(drugrdata[0])
        drugrdata.append(unmet)

        for row in drugrdata:
            tot = sum(row[2:])
            row.append(tot)
            conn.execute('insert into drugr2010 values (?,?,?,?,?,?,?,?,?,?,?,?)', row)
        #drugr.to_csv('2010.csv')
        dfout = pd.DataFrame(drugrdata)

        # saving the dataframe
        dfout.to_csv('Drug_2010.csv')

        conn.commit()
        conn.close()
        print("Success")

    except Exception as e:
        error = "Drug page not updated"
        conn.rollback()
        conn.close()
        print("Error")

def DrugDbUpdate2013():

    try:
        conn = sqlite3.connect('D:\GHI\ghi_website_2021/ghi2.db')
        # conn = sqlite3.connect('mysite/ghi.db')
        # conn = sqlite3.connect('ghi.db')
        # conn.execute('''DELETE FROM drugr2010_bkp''')
        # conn.execute('''DELETE FROM drugr2013_bkp''')
        # conn.execute('''DELETE FROM drugr2015_bkp''')
        #
        # conn.execute('''INSERT INTO drugr2010_bkp SELECT * FROM drugr2010''')
        # conn.execute('''INSERT INTO drugr2013_bkp SELECT * FROM drugr2013''')
        # conn.execute('''INSERT INTO drugr2015_bkp SELECT * FROM drugr2015''')
        #
        # conn.execute('''DELETE FROM drugr2010''')
        # conn.execute('''DELETE FROM drugr2013''')
        # conn.execute('''DELETE FROM drugr2015''')
        # datasrc = 'https://docs.google.com/spreadsheets/d/1IBfN_3f-dG65YbLWQbkXojUxs2PlQyo7l04Ubz9kLkU/pub?gid=1560508440&single=true&output=csv' # old link 04/24
        datasrc = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSijEPfCc0nHZyzbPhXA5CUSKqRMTWerwWSvAlpf2ZiFD4GAgb_HZnfo8aoBP-EvXXM8lJXxZ5Sq8ai/pub?gid=1560508440&single=true&output=csv'
        df = pd.read_csv(datasrc, skiprows=1)
        drugdata = []
        drugrdata = []
        drug2010 = []
        perc2010 = []


        for i in range(50, 95):
            drugr = []
            name = df.iloc[5, i]
            #print(name)
            drugr.append(name)
            company = df.iloc[1, i]
            # print(company)
            drugr.append(company)
            for j in range(10, 20):
                if j == 10: #TB
                    tb1 = cleanfloat(df.iloc[8, i])
                    tb2 = cleanfloat(df.iloc[9, i])
                    tb3 = cleanfloat(df.iloc[10, i])
                    temp = (tb1 + tb2 + tb3)
                    drugr.append(temp)
                elif j == 11:
                    mal1 = cleanfloat(df.iloc[11, i])
                    mal2 = cleanfloat(df.iloc[12, i])
                    temp = (mal1 + mal2)
                    drugr.append(temp)
                elif j == 19:
                    total = cleanfloat(df.iloc[j + 1, i])
                    zz = [name, total]
                    perc2010.append(zz)
                else:
                    temp = df.iloc[j + 1, i]
                    if isinstance(temp, float) == False and isinstance(temp, int) == False:
                        temp = float(temp.replace(',', ''))
                    if temp != temp:
                        temp = 0
                    drugr.append(temp)
                if int(temp) > 0:
                    if j == 10:
                        disease = 'TB'
                        color = 'FFB31C'
                    elif j == 11 or j == 12:
                        disease = 'Malaria'
                        color = '0083CA'
                    elif j == 13:
                        disease = 'HIV'
                        color = 'EF3E2E'
                    elif j == 14:
                        disease = 'Roundworm'
                        color = '003452'
                    elif j == 15:
                        disease = 'Hookworm'
                        color = '86AAB9'
                    elif j == 16:
                        disease = 'Whipworm'
                        color = 'CAEEFD'
                    elif j == 17:
                        disease = 'Schistosomiasis'
                        color = '546675'
                    elif j == 18:
                        disease = 'Onchocerasis'
                        color = '8A5575'
                    elif j == 19:
                        disease = 'LF'
                        color = '305516'
                    company = df.iloc[1, i]
                    drugrow = [name, company, disease, temp, color]
                    drug2010.append(drugrow)

            if isinstance(df.iloc[20, i], float) == False:
                score = float(df.iloc[20, i].replace(',', ''))
            else:
                score = df.iloc[20, i]
            row = [name, score]
            drugdata.append(row)
            drugrdata.append(drugr)

        unmet = ['Unmet Need', 'Unmet Need']
        unmetsum = 0
        for xx in [[8, 9, 10], [11, 12], [13], [14], [15], [16], [17], [18], [19]]:
            val = 0
            for yy in xx:
                t = df.iloc[yy, 46] #47 changed to 46
                if isinstance(t, float) == False and isinstance(t, int) == False:
                    t = float(t.replace(',', ''))
                if t != t:
                    t = 0
                val += t
            unmet.append(val)
            unmetsum += val
        # print(unmet)
        # print(drugrdata[0])
        drugrdata.append(unmet)

        for row in drugrdata:
            tot = sum(row[2:])
            row.append(tot)
            conn.execute('insert into drugr2013 values (?,?,?,?,?,?,?,?,?,?,?,?)', row)
        #drugr.to_csv('2010.csv')
        dfout = pd.DataFrame(drugrdata)

        # saving the dataframe
        dfout.to_csv('Drug_2013.csv')

        conn.commit()
        conn.close()
        print("Success")

    except Exception as e:
        error = "Drug page not updated"
        conn.rollback()
        conn.close()
        print("Error")



def DrugDbUpdate2017():
    try:
        conn = sqlite3.connect('D:\GHI\ghi_website_2021/ghi.db')
        datasrc2017 ='https://docs.google.com/spreadsheets/d/e/2PACX-1vQLNsp6UJVQaYMo7KUueUGGd8Mj1AkzBDcU2ksqFdTm9JfptKrLHmy2aiKbC1b_yV0qLOIy4EAOtU_m/pub?gid=1560508440&single=true&output=csv'
        df2017 = pd.read_csv(datasrc2017, skiprows=1)
        is_df2017_true = df2017.notnull()

        drugdata = []

        #2017

        drugrdata = []
        perc2017 = []
        drug2015 =[]
        for i in range(112, 158):
            drugr = []
            name = df2017.iloc[5, i]
            drugr.append(name)
            company = df2017.iloc[0, i]
            if is_df2017_true.iloc[0, i] == True:
                temp_comp = company
            else:
                company = temp_comp
            drugr.append(company)
            for j in range(11, 22):
                if j == 11:
                    tb1 = cleanfloat(df2017.iloc[8, i])
                    tb2 = cleanfloat(df2017.iloc[9, i])
                    tb3 = cleanfloat(df2017.iloc[10, i])
                    temp = (tb1 + tb2 + tb3)
                    drugr.append(temp)
                elif j == 12:
                    mal1 = cleanfloat(df2017.iloc[11, i])
                    mal2 = cleanfloat(df2017.iloc[12, i])
                    temp = (mal1 + mal2)
                    drugr.append(temp)
                elif j == 22:
                    total = cleanfloat(df2017.iloc[j, i])
                    zz = [name, total]
                    perc2017.append(zz)
                else:
                    temp = df2017.iloc[j, i]
                    if isinstance(temp, float) == False and isinstance(temp, int) == False:
                        temp = float(temp.replace(',', ''))
                    if temp != temp:
                        temp = 0
                    drugr.append(temp)
                if int(temp) > 0:
                    if j == 11:
                        disease = 'TB'
                        color = 'FFB31C'
                    elif j == 12:
                        disease = 'Malaria'
                        color = '0083CA'
                    elif j == 13:
                        disease = 'HIV'
                        color = 'EF3E2E'
                    elif j == 14:
                        disease = 'Roundworm'
                        color = '003452'
                    elif j == 15:
                        disease = 'Hookworm'
                        color = '86AAB9'
                    elif j == 16:
                        disease = 'Whipworm'
                        color = 'CAEEFD'
                    elif j == 17:
                        disease = 'Schistosomiasis'
                        color = '546675'
                    elif j == 18:
                        disease = 'Onchocerasis'
                        color = '8A5575'
                    elif j == 19:
                        disease = 'LF'
                        color = '305516'
                    elif j == 20:
                        disease = 'Trachoma'
                        color = 'EE8D7D'
                    elif j == 21:
                        disease = 'Hep_C'
                        color = 'FE8B7D'
                    company = df2017.iloc[1, i]
                    drugrow = [name, company, disease, temp, color]
                    drug2015.append(drugrow)

            if isinstance(df2017.iloc[20, i], float) == False:
                score = float(df2017.iloc[20, i].replace(',', ''))
            else:
                score = df2017.iloc[20, i]
            row = [name, score]
            drugdata.append(row)
            drugrdata.append(drugr)

        # unmet = ['Unmet Need', 'Unmet Need']
        # unmetsum = 0
        # for xx in [[8, 9, 10], [11, 12], [13], [14], [15], [16], [17], [18], [19]]:
        #     val = 0
        #     for yy in xx:
        #         t = df2017.iloc[yy, 97]  # 98 changed to 97
        #         if isinstance(t, float) == False and isinstance(t, int) == False:
        #             t = float(t.replace(',', ''))
        #         if t != t:
        #             t = 0
        #         val += t
        #     unmet.append(val)
        #     unmetsum += val
        # drugrdata.append(unmet)

        dfout = pd.DataFrame(drugrdata)

        # saving the dataframe
        dfout.to_csv('Drug_2017.csv')

        for row in drugrdata:
            tot = sum(row[2:])
            row.append(tot)
            conn.execute('insert into drugr2017 values (?,?,?,?,?,?,?,?,?,?,?,?,?,?)', row)
        perc2017.sort(key=lambda x: x[1], reverse=True)
        conn.commit()
        conn.close()
        print("Success")
    except Exception as e:
        error = "Drug page not updated"
        conn.rollback()
        conn.close()
        print("Error")

def DrugDbUpdate2015():
    try:
        conn = sqlite3.connect('D:\GHI\ghi_website_2021/ghi2.db')
        datasrc2015 ='https://docs.google.com/spreadsheets/d/e/2PACX-1vSTzH6iRaiUexi_w5bfVh_y2T8I8KRrfQINlcmgkSGLEmUt9Ih6rwpcxmjqkFdtvP1CXhonGN4f5P1M/pub?gid=1560508440&single=true&output=csv'
        df2015 = pd.read_csv(datasrc2015, skiprows=1)
        is_df2015_true = df2015.notnull()

        drugdata = []

        #2015

        drugrdata = []
        perc2015 = []
        drug2015 =[]
        for i in range(50, 95):
            drugr = []
            name = df2015.iloc[5, i]
            drugr.append(name)
            company = df2015.iloc[0, i]
            if is_df2015_true.iloc[0, i] == True:
                temp_comp = company
            else:
                company = temp_comp
            drugr.append(company)
            for j in range(11, 20):
                if j == 11:
                    tb1 = cleanfloat(df2015.iloc[8, i])
                    tb2 = cleanfloat(df2015.iloc[9, i])
                    tb3 = cleanfloat(df2015.iloc[10, i])
                    temp = (tb1 + tb2 + tb3)
                    drugr.append(temp)
                elif j == 12:
                    mal1 = cleanfloat(df2015.iloc[11, i])
                    mal2 = cleanfloat(df2015.iloc[12, i])
                    temp = (mal1 + mal2)
                    drugr.append(temp)
                elif j == 22:
                    total = cleanfloat(df2015.iloc[j, i])
                    zz = [name, total]
                    perc2015.append(zz)
                else:
                    temp = df2015.iloc[j, i]
                    if isinstance(temp, float) == False and isinstance(temp, int) == False:
                        temp = float(temp.replace(',', ''))
                    if temp != temp:
                        temp = 0
                    drugr.append(temp)
                if int(temp) > 0:
                    if j == 11:
                        disease = 'TB'
                        color = 'FFB31C'
                    elif j == 12:
                        disease = 'Malaria'
                        color = '0083CA'
                    elif j == 13:
                        disease = 'HIV'
                        color = 'EF3E2E'
                    elif j == 14:
                        disease = 'Roundworm'
                        color = '003452'
                    elif j == 15:
                        disease = 'Hookworm'
                        color = '86AAB9'
                    elif j == 16:
                        disease = 'Whipworm'
                        color = 'CAEEFD'
                    elif j == 17:
                        disease = 'Schistosomiasis'
                        color = '546675'
                    elif j == 18:
                        disease = 'Onchocerasis'
                        color = '8A5575'
                    elif j == 19:
                        disease = 'LF'
                        color = '305516'
                    elif j == 20:
                        disease = 'Trachoma'
                        color = 'EE8D7D'
                    elif j == 21:
                        disease = 'Hep_C'
                        color = 'FE8B7D'
                    company = df2015.iloc[1, i]
                    drugrow = [name, company, disease, temp, color]
                    drug2015.append(drugrow)

            if isinstance(df2015.iloc[20, i], float) == False:
                score = float(df2015.iloc[20, i].replace(',', ''))
            else:
                score = df2015.iloc[20, i]
            row = [name, score]
            drugdata.append(row)
            drugrdata.append(drugr)

        # unmet = ['Unmet Need', 'Unmet Need']
        # unmetsum = 0
        # for xx in [[8, 9, 10], [11, 12], [13], [14], [15], [16], [17], [18], [19]]:
        #     val = 0
        #     for yy in xx:
        #         t = df2017.iloc[yy, 97]  # 98 changed to 97
        #         if isinstance(t, float) == False and isinstance(t, int) == False:
        #             t = float(t.replace(',', ''))
        #         if t != t:
        #             t = 0
        #         val += t
        #     unmet.append(val)
        #     unmetsum += val
        # drugrdata.append(unmet)

        dfout = pd.DataFrame(drugrdata)

        # saving the dataframe
        dfout.to_csv('Drug_2015.csv')

        for row in drugrdata:
            tot = sum(row[2:])
            row.append(tot)
            conn.execute('insert into drugr2015 values (?,?,?,?,?,?,?,?,?,?,?,?)', row)
        perc2015.sort(key=lambda x: x[1], reverse=True)
        conn.commit()
        conn.close()
        print("Success")
    except Exception as e:
        error = "Drug page not updated"
        conn.rollback()
        conn.close()
        print("Error")



if __name__ == '__main__':


    print("I'm a car!")
    print(sys.argv[1])

    if sys.argv[1] == '2010':
        CreateDrugTable2010()
        DrugDbUpdate2010()
    elif sys.argv[1] == '2013':
        CreateDrugTable2013()
        DrugDbUpdate2013()
    elif sys.argv[1] == '2015':
        CreateDrugTable2015()
        DrugDbUpdate2015()
    elif sys.argv == '2017':
        CreateDrugTable2017()
        DrugDbUpdate2017()