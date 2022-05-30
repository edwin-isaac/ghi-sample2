import sqlite3
import pandas as pd

def CreateDiseae():
    conn = sqlite3.connect('ghi.db')
    conn = sqlite3.connect('D:\GHI\ghi_website_2021/ghi.db')
    conn.execute('''DROP TABLE IF EXISTS disease2010''')
    conn.execute('''DROP TABLE IF EXISTS disease2013''')
    conn.execute('''DROP TABLE IF EXISTS disease2015''')
    conn.execute('''DROP TABLE IF EXISTS disbars''')
    conn.execute('''DROP TABLE IF EXISTS distypes''')
    conn.execute('''DROP TABLE IF EXISTS disbars2010B2015''')
    conn.execute('''DROP TABLE IF EXISTS distypes2010B2015''')

    conn.execute('''CREATE TABLE disease2013
                (disease text, distype text, impact real, daly real, need text, color text)''')

    conn.execute('''CREATE TABLE disease2010
                (disease text, distype text, impact real, daly real, need text, color text)''')

    conn.execute('''CREATE TABLE disease2015
                (disease text, distype text, impact real, daly real, need text, color text)''')

    conn.execute('''CREATE TABLE disbars
               (disease text, color text, efficacy2010 real, efficacy2013 real, coverage2010 real, coverage2013 real, need2010 real, need2013 real)''')

    conn.execute('''CREATE TABLE distypes
               (disease text,distype text, color text, efficacy2010 real, efficacy2013 real, coverage2010 real, coverage2013 real,position real)''')

    conn.execute('''CREATE TABLE disbars2010B2015
               (disease text, color text, efficacy2010 real, efficacy2013 real, coverage2010 real, coverage2013 real, need2010 real, need2013 real)''')

    conn.execute('''CREATE TABLE distypes2010B2015
               (disease text,distype text, color text, efficacy2010 real, efficacy2013 real, coverage2010 real, coverage2013 real,position real)''')
    conn.commit()
    conn.close()

def DiseaseDbUpdate():
    try:
        #conn = sqlite3.connect('ghi.db')
        # conn = sqlite3.connect('D:\GHI\ghi_website_2021/ghi.db')
        # conn.execute('''DELETE FROM disease2010_bkp''')
        # conn.execute('''DELETE FROM disease2013_bkp''')
        # conn.execute('''DELETE FROM disease2015_bkp''')
        # conn.execute('''DELETE FROM disbars_bkp''')
        # conn.execute('''DELETE FROM distypes_bkp''')
        # conn.execute('''DELETE FROM disbars2010B2015_bkp''')
        # conn.execute('''DELETE FROM distypes2010B2015_bkp''')
        #
        # # conn.execute('''insert into disease2010_bkp select * from disease2010''')
        # # conn.execute('''insert into disease2013_bkp select * from disease2013''')
        # # conn.execute('''insert into disease2015_bkp select * from disease2015''')
        # conn.execute(
        #     '''insert into disease2010_bkp select * from disease2010''')
        # conn.execute(
        #     '''insert into disease2013_bkp select * from disease2013''')
        # conn.execute(
        #     '''insert into disease2015_bkp select * from disease2015''')
        # conn.execute('''insert into disbars_bkp select * from disbars''')
        # conn.execute('''insert into distypes_bkp select * from distypes''')
        #
        # # conn.execute('''insert into disbars2010B2015_bkp select * from disbars2010B2015''')
        # # conn.execute('''insert into distypes2010B2015_bkp select * from distypes2010B2015''')
        # conn.execute(
        #     '''insert into disbars2010B2015_bkp select * from disbars2010B2015''')
        # conn.execute(
        #     '''insert into distypes2010B2015_bkp select * from distypes2010B2015''')
        # conn.execute('''DELETE FROM disease2010''')
        # conn.execute('''DELETE FROM disease2013''')
        # conn.execute('''DELETE FROM disease2015''')
        # conn.execute('''DELETE FROM disbars''')
        # conn.execute('''DELETE FROM distypes''')
        # conn.execute('''DELETE FROM disbars2010B2015''')
        # conn.execute('''DELETE FROM distypes2010B2015''')

        #datasrc = 'https://docs.google.com/spreadsheets/d/1IBfN_3f-dG65YbLWQbkXojUxs2PlQyo7l04Ubz9kLkU/pub?gid=1560508440&single=true&output=csv' # old link 04/26
        datasrc = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSijEPfCc0nHZyzbPhXA5CUSKqRMTWerwWSvAlpf2ZiFD4GAgb_HZnfo8aoBP-EvXXM8lJXxZ5Sq8ai/pub?gid=1560508440&single=true&output=csv'
        # datasrc = 'ORS_GlobalBurdenDisease_2010_2013.csv'
        df = pd.read_csv(datasrc, skiprows=1)
        # datasrc2 = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQI7j2NartMCCF_N-OCkFqAyD67N9Q32yybE21x-zaRPrETsszdZep91dVVVSCjeXXbPjPfZVdE-odE/pub?gid=1560508440&single=true&output=csv'
        #datasrc2 = 'https://docs.google.com/spreadsheets/d/1IBfN_3f-dG65YbLWQbkXojUxs2PlQyo7l04Ubz9kLkU/pub?gid=1560508440&single=true&output=csv' # old link 04/26
        datasrc2 = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSijEPfCc0nHZyzbPhXA5CUSKqRMTWerwWSvAlpf2ZiFD4GAgb_HZnfo8aoBP-EvXXM8lJXxZ5Sq8ai/pub?gid=1560508440&single=true&output=csv'
        #datasrc3 = 'https://docs.google.com/spreadsheets/d/1vwMReqs8G2jK-Cx2_MWKn85MlNjnQK-UR3Q8vZ_pPNk/pub?gid=1560508440&single=true&output=csv' # old link 04/26
        datasrc3 = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSTzH6iRaiUexi_w5bfVh_y2T8I8KRrfQINlcmgkSGLEmUt9Ih6rwpcxmjqkFdtvP1CXhonGN4f5P1M/pub?gid=1560508440&single=true&output=csv'
        df2 = pd.read_csv(datasrc2, skiprows=1)
        df_2010B_2015 = pd.read_csv(datasrc3, skiprows=1)

        disease2010db = []
        disease2013db = []
        disease2015db = []
        i = 0
        for k in range(8, 20):
            distypes = ['TB', 'TB', 'TB', 'Malaria', 'Malaria', 'HIV', 'Roundworm', 'Hookworm', 'Whipworm',
                        'Schistosomiasis', 'Onchoceriasis', 'LF']
            colors = ['#FFB31C', '#FFB31C', '#FFB31C', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9', '#CAEEFD',
                      '#546675', '#8A5575', '#305516']
            dis = ['Drug Susceptable TB', 'MDR-TB', 'XDR-TB', 'p. falc Malaria', 'p. vivax Malaria', 'HIV', 'Roundworm',
                   'Hookworm', 'Whipworm', 'Schistosomiasis', 'Onchoceriasis', 'LF']
            color = colors[i]
            disease = dis[i]
            distype = distypes[i]
            temp = df.iloc[k, 44]
            print(temp)
            temp1 = df.iloc[k, 46]
            print(temp1)
            temp2 = df.iloc[k, 47]
            print(temp2)
            if type(temp) != float and type(temp1) != float and type(temp2) != float:
                impact = float(temp.replace(',', ''))
                daly = float(temp1.replace(',', ''))
                need = float(temp2.replace(',', ''))
                i += 1
                row = [disease, distype, impact, daly, need, color]
                disease2010db.append(row)
            #    conn.execute('insert into disease2010 values (?,?,?,?,?,?)', row)

        i = 0
        for k in range(8, 20):
            distypes = ['TB', 'TB', 'TB', 'Malaria', 'Malaria', 'HIV', 'Roundworm', 'Hookworm', 'Whipworm',
                        'Schistosomiasis', 'Onchoceriasis', 'LF']
            colors = ['#FFB31C', '#FFB31C', '#FFB31C', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9', '#CAEEFD',
                      '#546675', '#8A5575', '#305516']
            dis = ['Drug Susceptable TB', 'MDR-TB', 'XDR-TB', 'p. falc Malaria', 'p. vivax Malaria', 'HIV', 'Roundworm',
                   'Hookworm', 'Whipworm', 'Schistosomiasis', 'Onchoceriasis', 'LF']
            color = colors[i]
            disease = dis[i]
            distype = distypes[i]
            temp = df.iloc[k, 95]
            temp1 = df.iloc[k, 97]
            temp2 = df.iloc[k, 98]
            print(temp)
            print(temp1)
            print(temp2)
            print(distype)
            print(disease)
            if type(temp) != float and type(temp1) != float and type(temp2) != float:
                impact = float(temp.replace(',', ''))
                daly = float(temp1.replace(',', ''))
                need = float(temp2.replace(',', ''))
                i += 1
                row = [disease, distype, impact, daly, need, color]
                disease2013db.append(row)
             #   conn.execute('insert into disease2013 values (?,?,?,?,?,?)', row)
        i = 0
        for k in range(8, 20):
            distypes = ['TB', 'TB', 'TB', 'Malaria', 'Malaria', 'HIV', 'Roundworm', 'Hookworm', 'Whipworm',
                        'Schistosomiasis', 'Onchoceriasis', 'LF']
            colors = ['#FFB31C', '#FFB31C', '#FFB31C', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9', '#CAEEFD',
                      '#546675', '#8A5575', '#305516']
            dis = ['Drug Susceptable TB', 'MDR-TB', 'XDR-TB', 'p. falc Malaria', 'p. vivax Malaria', 'HIV', 'Roundworm',
                   'Hookworm', 'Whipworm', 'Schistosomiasis', 'Onchoceriasis', 'LF']
            color = colors[i]
            disease = dis[i]
            distype = distypes[i]
            temp = df_2010B_2015.iloc[k, 95]
            temp1 = df_2010B_2015.iloc[k, 97]
            temp2 = df_2010B_2015.iloc[k, 98]
            print(temp)
            print(temp1)
            print(temp2)
            print(distype)
            print(disease)
            if type(temp) != float and type(temp1) != float and type(temp2) != float:
                impact = float(temp.replace(',', ''))
                daly = float(temp1.replace(',', ''))
                need = float(temp2.replace(',', ''))
                i += 1
                row = [disease, distype, impact, daly, need, color]
                disease2013db.append(row)
            #    conn.execute('insert into disease2015 values (?,?,?,?,?,?)', row)

        def stripdata(x, y):
            try:
                tmp = df.iloc[x, y]
                if tmp == "#DIV/0!" or tmp == "nan":
                    return (0)
                if tmp == 'No Data':
                    return (0)
                if isinstance(tmp, float) == False:
                    return (float(tmp.replace(',', '').replace(' ', '0').replace('%', '')))
                else:
                    return (0)
            except:
                return 0


        def stripdata3(x, y):
            try:
                tmp = df_2010B_2015.iloc[x, y]
                if tmp == "#DIV/0!" or tmp == "nan" or tmp == "#REF!":
                    return (0)
                if tmp == 'No Data':
                    return (0)
                if isinstance(tmp, float) == False:
                    return (float(tmp.replace(',', '').replace(' ', '0').replace('%', '')))
                else:
                    return (0)
            except:
                return 0


        def stripdata2(x, y):
            tmp = df2.iloc[x, y]
            if tmp == "#DIV/0!" or tmp == "nan" or tmp == "#REF!":
                return (0)
            if tmp == 'No Data':
                return (0)
            if isinstance(tmp, float) == False:
                res = float(tmp.replace(',', '').replace(' ', '0').replace('%', ''))
                if res > 10000:
                    res = res * 0.00001
                # print(res)
                return (0.01 * res)
            else:
                return (0)

        disbars = []
        j = 0
        for k in range(113, 128):
            if not k in range(114,118) and k!=119 and k!=120:
                colors = ['#FFB31C', '#0083CA', '#EF3E2E', '#003452', '#86AAB9', '#CAEEFD',
                      '#546675', '#8A5575', '#305516']
                diseasename = df.iloc[k, 9]
                color = colors[j]
                efficacy2010 = stripdata(k, 10)
                efficacy2013 = stripdata(k, 13)
                coverage2010 = stripdata(k, 11)
                coverage2013 = stripdata(k, 14)
                need2010 = stripdata(k, 12)
                need2013 = stripdata(k, 15)
                roww = [diseasename, color, efficacy2010, efficacy2013, coverage2010, coverage2013, need2010, need2013]
                disbars.append(roww)
                j += 1
              #  conn.execute('insert into disbars values (?,?,?,?,?,?,?,?)', roww)

        disbars = []
        j = 0
        for k in range(194, 209):
            if not k in range(195,199) and k!=200 and k!=201:
                colors = ['#FFB31C', '#0083CA', '#EF3E2E', '#003452', '#86AAB9', '#CAEEFD',
                        '#546675', '#8A5575', '#305516']
                newdiseasename = df_2010B_2015.iloc[k, 5]
                color = colors[j]
                #newefficacy2010 = stripdata3(k, 8)
                newefficacy2010 = 0
                newefficacy2013 = stripdata3(k, 6)
                #newcoverage2010 = stripdata3(k, 10)
                newcoverage2010 = 0
                newcoverage2013 = stripdata3(k, 7)
                #newneed2010 = stripdata3(k, 12)
                newneed2010 = 0
                newneed2013 = stripdata3(k, 8)
                newroww = [newdiseasename, color, newefficacy2010, newefficacy2013, newcoverage2010, newcoverage2013,
                           newneed2010, newneed2013]
                j += 1
                disbars.append(newroww)
                # conn.execute('insert into disbars2010B2015 values (?,?,?,?,?,?,?,?)', newroww)

        def doStuff(k, i, m, mark, diseasename, disetype, color, efficacy2010, efficacy2013, coverage2010, coverage2013,
                    p, year):
            if disetype == 'TB' or disetype == 'Malaria':
                efficacy2010 /= m
                efficacy2013 /= m
                coverage2010 /= m
                coverage2013 /= m
            roww = [diseasename, disetype, color, efficacy2010, efficacy2013, coverage2010, coverage2013, p]
            print(roww)
            #if year == 2010:
               # conn.execute('insert into distypes values (?,?,?,?,?,?,?,?)', roww)
            #elif year == 2015:
               # conn.execute('insert into distypes2010B2015 values (?,?,?,?,?,?,?,?)', roww)

        def doStuffDisDrug(diseasename, disetype, color, efficacy2010, efficacy2013, coverage2010, coverage2013, p, year):
            roww = [diseasename, disetype, color, efficacy2010, efficacy2013, coverage2010, coverage2013, p]
            #if year == 2010:
               # conn.execute('insert into distypes values (?,?,?,?,?,?,?,?)', roww)
           # elif year == 2015:
               # conn.execute('insert into distypes2010B2015 values (?,?,?,?,?,?,?,?)', roww)

        efficacyone = 0
        efficacytwo = 0
        coverageone = 0
        coveragetwo = 0
        i = 1
        j = 0
        mark = 0
        for k in [114, 115, 116, 117]:
            colors = ['#FFB31C', '#FFB31C', '#FFB31C', '#FFB31C', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9', '#CAEEFD',
                      '#546675', '#8A5575']
            dismap = [1, 1, 1, 1]
            position = [0, 1, 2, 3]
            disease = ['DS-TB- HIV+', 'DS-TB- HIV-', 'MDR-TB', 'XDR-TB']
            disetype = 'TB'
            m = dismap[mark]
            p = position[mark]
            color = colors[j % 12]
            diseasename = disease[mark]
            efficacyone += stripdata(k, 10)
            efficacytwo += stripdata(k, 13)
            coverageone += stripdata(k, 11)
            coveragetwo += stripdata(k, 14)
            year = 2010
            if i == m:
                doStuff(k, i, m, mark, diseasename, disetype, color, efficacyone, efficacytwo, coverageone, coveragetwo,
                        p,
                        year)
                i = 0
                mark += 1
                efficacyone = 0
                efficacytwo = 0
                coverageone = 0
                coveragetwo = 0
            i += 1
            j += 1

        i = 1
        j = 0
        mark = 0
        for k in [195,196,197,198]:
            colors = ['#FFB31C', '#FFB31C', '#FFB31C', '#FFB31C', '#0083CA', '#EF3E2E', '#003452', '#86AAB9', '#CAEEFD',
                      '#546675', '#8A5575', '#305516']
            dismap = [1, 1, 1, 1]
            position = [0,1, 2, 3]
            disease = ['DS-TB- HIV+', 'DS-TB- HIV-', 'MDR-TB', 'XDR-TB']
            disetype = 'TB'
            m = dismap[mark]
            p = position[mark]
            color = colors[j % 12]
            diseasename = disease[mark]
            efficacyone += stripdata3(k, 7)
            efficacytwo += stripdata3(k, 7)
            coverageone += stripdata3(k, 7)
            coveragetwo += stripdata3(k, 7)
            year = 2015
            if i == m:
                doStuff(k, i, m, mark, diseasename, disetype, color, efficacyone, efficacytwo, coverageone, coveragetwo,
                        p,
                        year)
                i = 0
                mark += 1
                efficacyone = 0
                efficacytwo = 0
                coverageone = 0
                coveragetwo = 0
            i += 1
            j += 1

        i = 1
        j = 0
        mark = 0
        for k in [119,120]:
            colors = ['#FFB31C', '#FFB31C', '#FFB31C', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9', '#CAEEFD',
                      '#546675', '#8A5575', '#305516']
            dismap = [1, 1]
            position = [0, 1]
            disease = ['p. falc Malaria', 'p. vivax Malaria']
            disetype = 'Malaria'
            m = dismap[mark]
            p = position[mark]
            color = colors[j % 12]
            diseasename = disease[mark]
            efficacyone += stripdata(k, 10)
            efficacytwo += stripdata(k, 13)
            coverageone += stripdata(k, 11)
            coveragetwo += stripdata(k, 14)
            year = 2010
            if i == m:
                doStuff(k, i, m, mark, diseasename, disetype, color, efficacyone, efficacytwo, coverageone, coveragetwo,
                        p,
                        year)
                i = 0
                mark += 1
                efficacyone = 0
                efficacytwo = 0
                coverageone = 0
                coveragetwo = 0
            i += 1
            j += 1

        i = 1
        mark = 0
        for k in [200,201]:
            colors = ['#FFB31C', '#FFB31C', '#FFB31C', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9', '#CAEEFD',
                      '#546675', '#8A5575', '#305516']
            dismap = [1, 1]
            position = [0, 1]
            disease = ['p. falc Malaria', 'p. vivax Malaria']
            disetype = 'Malaria'
            m = dismap[mark]
            p = position[mark]
            color = colors[j % 12]
            diseasename = disease[mark]
            efficacyone += stripdata3(k, 7)
            efficacytwo += stripdata3(k, 7)
            coverageone += stripdata3(k, 7)
            coveragetwo += stripdata3(k, 7)
            year = 2015
            if i == m:
                doStuff(k, i, m, mark, diseasename, disetype, color, efficacyone, efficacytwo, coverageone, coveragetwo,
                        p,
                        year)
                i = 0
                mark += 1
                efficacyone = 0
                efficacytwo = 0
                coverageone = 0
                coveragetwo = 0
            i += 1

        i = 1
        mark = 0
        for k in [123]:
            colors = ['#003452', '#003452', '#003452', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9', '#CAEEFD',
                      '#546675', '#8A5575', '#305516']
            # disease = ['Alb', 'Mbd', 'Ivm + Alb', 'Dec + Alb', 'Pzq + Alb', 'Pzq + Mbd']
            disease = ['Roundworm']
            disetype = 'Roundworm'
            m = 0
            p = 0
            color = colors[j % 12]
            diseasename = disease[mark]
            efficacyone += stripdata(k, 10)
            efficacytwo += stripdata(k, 13)
            coverageone += stripdata(k, 11)
            coveragetwo += stripdata(k, 14)
            year = 2010
            doStuff(k, i, m, mark, diseasename, disetype, color, efficacyone, efficacytwo, coverageone, coveragetwo, p,
                    year)
            i = 0
            mark += 1
            efficacyone = 0
            efficacytwo = 0
            coverageone = 0
            coveragetwo = 0
            i += 1

        i = 1
        mark = 0
        for k in [204]:
            colors = ['#003452', '#003452', '#003452', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9', '#CAEEFD',
                      '#546675', '#8A5575', '#305516']
            # disease = ['Alb', 'Mbd', 'Ivm + Alb', 'Dec + Alb', 'Pzq + Alb', 'Pzq + Mbd']
            disease = ['Roundworm']
            disetype = 'Roundworm'
            m = 0
            p = 0
            color = colors[j % 12]
            diseasename = disease[mark]
            efficacyone += stripdata3(k, 7)
            efficacytwo += stripdata3(k, 7)
            coverageone += stripdata3(k, 7)
            coveragetwo += stripdata3(k, 7)
            year = 2015
            doStuff(k, i, m, mark, diseasename, disetype, color, efficacyone, efficacytwo, coverageone, coveragetwo, p,
                    year)
            i = 0
            mark += 1
            efficacyone = 0
            efficacytwo = 0
            coverageone = 0
            coveragetwo = 0
            i += 1

        i = 1
        mark = 0
        for k in [122]:

            colors = ['#86AAB9', '#86AAB9', '#86AAB9', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9', '#CAEEFD',
                      '#546675', '#8A5575', '#305516']
            # disease = ['Alb', 'Mbd', 'Ivm + Alb', 'Dec + Alb', 'Pzq + Alb', 'Pzq + Mbd']
            disease = ['Hookworm']
            disetype = 'Hookworm'
            m = 0
            p = 0
            color = colors[j % 12]
            diseasename = disease[mark]
            efficacyone += stripdata(k, 10)
            efficacytwo += stripdata(k, 13)
            coverageone += stripdata(k, 11)
            coveragetwo += stripdata(k, 14)
            year = 2010
            doStuff(k, i, m, mark, diseasename, disetype, color, efficacyone, efficacytwo, coverageone, coveragetwo, p,
                    year)
            i = 0
            mark += 1
            efficacyone = 0
            efficacytwo = 0
            coverageone = 0
            coveragetwo = 0
            i += 1

        i = 1
        mark = 0
        for k in [203]:
            colors = ['#86AAB9', '#86AAB9', '#86AAB9', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9', '#CAEEFD',
                      '#546675', '#8A5575', '#305516']
            # disease = ['Alb', 'Mbd', 'Ivm + Alb', 'Dec + Alb', 'Pzq + Alb', 'Pzq + Mbd']
            disease = ['Hookworm']
            disetype = 'Hookworm'
            m = 0
            p = 0
            color = colors[j % 12]
            diseasename = disease[mark]
            efficacyone += stripdata3(k, 7)
            efficacytwo += stripdata3(k, 7)
            coverageone += stripdata3(k, 7)
            coveragetwo += stripdata3(k, 7)
            year = 2015
            doStuff(k, i, m, mark, diseasename, disetype, color, efficacyone, efficacytwo, coverageone, coveragetwo, p,
                    year)
            i = 0
            mark += 1
            efficacyone = 0
            efficacytwo = 0
            coverageone = 0
            coveragetwo = 0
            i += 1

        i = 1
        mark = 0
        for k in [124]:
            colors = ['#CAEEFD', '#CAEEFD', '#CAEEFD', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9', '#CAEEFD',
                      '#546675', '#8A5575', '#305516']
            # disease = ['Alb', 'Mbd', 'Ivm + Alb', 'Dec + Alb', 'Pzq + Alb', 'Pzq + Mbd']
            disease = ['Whipworm']
            disetype = 'Whipworm'
            m = 0
            p = 0
            color = colors[j % 12]
            diseasename = disease[mark]
            efficacyone += stripdata(k, 10)
            efficacytwo += stripdata(k, 13)
            coverageone += stripdata(k, 11)
            coveragetwo += stripdata(k, 14)
            year = 2010
            doStuff(k, i, m, mark, diseasename, disetype, color, efficacyone, efficacytwo, coverageone, coveragetwo, p,
                    year)
            i = 0
            mark += 1
            efficacyone = 0
            efficacytwo = 0
            coverageone = 0
            coveragetwo = 0
            i += 1

        i = 1
        mark = 0
        for k in [205]:
            colors = ['#CAEEFD', '#CAEEFD', '#CAEEFD', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9', '#CAEEFD',
                      '#546675', '#8A5575', '#305516']
            # disease = ['Alb', 'Mbd', 'Ivm + Alb', 'Dec + Alb', 'Pzq + Alb', 'Pzq + Mbd']
            disease = ['Whipworm']
            disetype = 'Whipworm'
            m = 0
            p = 0
            color = colors[j % 12]
            diseasename = disease[mark]
            efficacyone += stripdata3(k, 7)
            efficacytwo += stripdata3(k, 7)
            coverageone += stripdata3(k, 7)
            coveragetwo += stripdata3(k, 7)
            year = 2015
            doStuff(k, i, m, mark, diseasename, disetype, color, efficacyone, efficacytwo, coverageone, coveragetwo, p,
                    year)
            i = 0
            mark += 1
            efficacyone = 0
            efficacytwo = 0
            coverageone = 0
            coveragetwo = 0
            i += 1

        i = 1
        mark = 0
        for k in [126]:
            colors = ['#546675', '#546675', '#546675', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9', '#CAEEFD',
                      '#546675', '#8A5575', '#305516']
            # disease = ['Ivm + Alb', 'Dec + Alb', 'Pzq', 'Ivm', 'Dec', 'Alb']
            disease = ['Schistosomiasis']
            disetype = 'Schistosomiasis'
            m = 0
            p = 0
            color = colors[j % 12]
            diseasename = disease[mark]
            efficacyone += stripdata(k, 10)
            efficacytwo += stripdata(k, 13)
            coverageone += stripdata(k, 11)
            coveragetwo += stripdata(k, 14)
            year = 2010
            doStuff(k, i, m, mark, diseasename, disetype, color, efficacyone, efficacytwo, coverageone, coveragetwo, p,
                    year)
            i = 0
            mark += 1
            efficacyone = 0
            efficacytwo = 0
            coverageone = 0
            coveragetwo = 0
            i += 1

        i = 1
        mark = 0
        for k in [207]:
            colors = ['#546675', '#546675', '#546675', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9', '#CAEEFD',
                      '#546675', '#8A5575', '#305516']
            # disease = ['Ivm + Alb', 'Dec + Alb', 'Pzq', 'Ivm', 'Dec', 'Alb']
            disease = ['Schistosomiasis', 'Dec + Alb','Pzq', 'Ivm', 'Dec', 'Alb']
            disetype = 'Schistosomiasis'
            m = 0
            p = 0
            color = colors[j % 12]
            diseasename = disease[mark]
            efficacyone += stripdata3(k, 7)
            efficacytwo += stripdata3(k, 7)
            coverageone += stripdata3(k, 7)
            coveragetwo += stripdata3(k, 7)
            year = 2015
            doStuff(k, i, m, mark, diseasename, disetype, color, efficacyone, efficacytwo, coverageone, coveragetwo, p,
                    year)
            i = 0
            mark += 1
            efficacyone = 0
            efficacytwo = 0
            coverageone = 0
            coveragetwo = 0
            i += 1

        i = 1
        mark = 0
        for k in [125]:
            colors = ['#5CB85C', '#5CB85C', '#5CB85C', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9', '#CAEEFD',
                      '#546675', '#8A5575', '#305516']
            # disease = ['Nodulectomy', 'Suramin', 'Ivm', 'Dec']
            disease = ['Onchoceriasis']
            disetype = 'Onchoceriasis'
            m = 0
            p = 0
            color = colors[j % 12]
            diseasename = disease[mark]
            efficacyone += stripdata(k, 10)
            efficacytwo += stripdata(k, 13)
            coverageone += stripdata(k, 11)
            coveragetwo += stripdata(k, 14)
            year = 2010
            doStuff(k, i, m, mark, diseasename, disetype, color, efficacyone, efficacytwo, coverageone, coveragetwo, p,
                    year)
            i = 0
            mark += 1
            efficacyone = 0
            efficacytwo = 0
            coverageone = 0
            coveragetwo = 0
            i += 1

        i = 1
        mark = 0
        for k in [206]:
            colors = ['#5CB85C', '#5CB85C', '#5CB85C', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9', '#CAEEFD',
                      '#546675', '#8A5575', '#305516']
            # disease = ['Nodulectomy', 'Suramin', 'Ivm', 'Dec']
            disease = ['Onchoceriasis']
            disetype = 'Onchoceriasis'
            m = 0
            p = 0
            color = colors[j % 12]
            diseasename = disease[mark]
            efficacyone += stripdata3(k, 7)
            efficacytwo += stripdata3(k, 7)
            coverageone += stripdata3(k, 7)
            coveragetwo += stripdata3(k, 7)
            year = 2015
            doStuff(k, i, m, mark, diseasename, disetype, color, efficacyone, efficacytwo, coverageone, coveragetwo, p,
                    year)
            i = 0
            mark += 1
            efficacyone = 0
            efficacytwo = 0
            coverageone = 0
            coveragetwo = 0
            i += 1

        i = 1
        mark = 0
        for k in [127]:
            colors = ['#305516', '#305516', '#305516', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9', '#CAEEFD',
                      '#546675', '#8A5575', '#305516']
            # disease = ['Dec', 'Dec + Alb', 'Ivm + Alb']
            disease = ['Lymphatic Filariasis']
            disetype = 'LF'
            m = 0
            p = 0
            color = colors[j % 12]
            diseasename = disease[mark]
            efficacyone += stripdata(k, 10)
            efficacytwo += stripdata(k, 13)
            coverageone += stripdata(k, 11)
            coveragetwo += stripdata(k, 14)
            year = 2010
            doStuff(k, i, m, mark, diseasename, disetype, color, efficacyone, efficacytwo, coverageone, coveragetwo, p,
                    year)
            i = 0
            mark += 1
            efficacyone = 0
            efficacytwo = 0
            coverageone = 0
            coveragetwo = 0
            i += 1

        i = 1
        mark = 0
        for k in [208]:
            colors = ['#305516', '#305516', '#305516', '#305516', '#305516', '#305516', '#003452', '#86AAB9', '#CAEEFD',
                      '#546675', '#8A5575', '#305516']
            disease = ['Lymphatic Filariasis']
            disetype = 'LF'
            m = 0
            p = 0
            color = colors[j % 12]
            diseasename = disease[mark]
            efficacyone += stripdata3(k, 7)
            efficacytwo += stripdata3(k, 7)
            coverageone += stripdata3(k, 7)
            coveragetwo += stripdata3(k, 7)
            year = 2015
            doStuff(k, i, m, mark, diseasename, disetype, color, efficacyone, efficacytwo, coverageone, coveragetwo, p,
                    year)
            i = 0
            mark += 1
            efficacyone = 0
            efficacytwo = 0
            coverageone = 0
            coveragetwo = 0
            i += 1

        i = 1
        mark = 0
        for k in [121]:
            colors = ['#EF3E2E', '#EF3E2E', '#EF3E2E', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9', '#CAEEFD',
                      '#546675', '#8A5575', '#305516']
            # disease = ['Dec', 'Dec + Alb', 'Ivm + Alb']
            disease = ['HIV']
            disetype = 'HIV'
            m = 0
            p = 0
            color = colors[j % 12]
            diseasename = disease[mark]
            efficacyone += stripdata(k, 10)
            efficacytwo += stripdata(k, 13)
            coverageone += stripdata(k, 11)
            coveragetwo += stripdata(k, 14)
            year = 2010
            doStuff(k, i, m, mark, diseasename, disetype, color, efficacyone, efficacytwo, coverageone, coveragetwo, p,
                    year)
            i = 0
            mark += 1
            efficacyone = 0
            efficacytwo = 0
            coverageone = 0
            coveragetwo = 0
            i += 1

        i = 1
        mark = 0
        for k in [202]:
            colors = ['#EF3E2E', '#EF3E2E', '#EF3E2E', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9', '#CAEEFD',
                      '#546675', '#8A5575', '#305516']
            # disease = ['Dec', 'Dec + Alb', 'Ivm + Alb']
            disease = ['HIV']
            disetype = 'HIV'
            m = 0
            p = 0
            color = colors[j % 12]
            diseasename = disease[mark]
            efficacyone += stripdata3(k, 7)
            efficacytwo += stripdata3(k, 7)
            coverageone += stripdata3(k, 7)
            coveragetwo += stripdata3(k, 7)
            year = 2015
            doStuff(k, i, m, mark, diseasename, disetype, color, efficacyone, efficacytwo, coverageone, coveragetwo, p,
                    year)
            i = 0
            mark += 1
            efficacyone = 0
            efficacytwo = 0
            coverageone = 0
            coveragetwo = 0
            i += 1

#######################year 2010 data ###########################
        mark = 0
        for k in [174, 175, 176]:
            colors = ['#0083CA', '#0083CA', '#0083CA', '#FFB31C', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9', '#CAEEFD',
                      '#546675', '#8A5575', '#305516']
            drugNames = ['Albendazole (Alb)', 'Mebendazole (Mbd)', 'Ivermectin + Albendazole (Ivm + Alb)']
            disetype = 'Whipworm_Eff'
            color = colors[j % 12]
            diseasename = drugNames[mark]
            efficacy2010 = stripdata(k, 2)
            efficacy2013 = 0
            coverage2010 = 0
            coverage2013 = 0
            p=0
            year = 2010
            doStuffDisDrug(diseasename, disetype, color, efficacy2010, efficacy2013, coverage2010, coverage2013, p, year)
            i = 0
            mark += 1
            efficacy2010 = 0

        mark = 0
        for k in [167, 168, 169]:
            colors = ['#0083CA', '#0083CA', '#0083CA', '#FFB31C', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9',
                      '#CAEEFD',
                      '#546675', '#8A5575', '#305516']
            drugNames = ['Albendazole (Alb)', 'Mebendazole (Mbd)', 'Ivermectin + Albendazole (Ivm + Alb)']
            disetype = 'Roundworm_Eff'
            color = colors[j % 12]
            diseasename = drugNames[mark]
            efficacy2010 += stripdata(k, 2)
            efficacy2013 = 0
            coverage2010 = 0
            coverage2013 = 0
            p = 0
            year = 2010
            doStuffDisDrug(diseasename, disetype, color, efficacy2010, efficacy2013, coverage2010, coverage2013, p,
                           year)
            mark += 1
            efficacy2010 = 0

        mark = 0
        for k in [171, 172]:
            colors = ['#0083CA', '#0083CA', '#0083CA', '#FFB31C', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9',
                      '#CAEEFD',
                      '#546675', '#8A5575', '#305516']
            drugNames = ['Albendazole (Alb)', 'Mebendazole (Mbd)']
            disetype = 'Hookworm_Eff'
            color = colors[j % 12]
            diseasename = drugNames[mark]
            efficacy2010 += stripdata(k, 2)
            efficacy2013 = 0
            coverage2010 = 0
            coverage2013 = 0
            p = 0
            year = 2010
            doStuffDisDrug(diseasename, disetype, color, efficacy2010, efficacy2013, coverage2010, coverage2013, p,
                           year)
            mark += 1
            efficacy2010 = 0

        mark = 0
        for k in [182, 183, 184]:
            colors = ['#0083CA', '#0083CA', '#0083CA', '#FFB31C', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9',
                      '#CAEEFD',
                      '#546675', '#8A5575', '#305516']
            drugNames = ['Diethylcarbamazine (Dec)', 'Diethylcarbamazine + Albendazole (Dec + Alb)', 'Ivermectin + Albendazole (Ivm + Alb)']
            disetype = 'LF_Eff'
            color = colors[j % 12]
            diseasename = drugNames[mark]
            efficacy2010 += stripdata(k, 2)
            efficacy2013 = 0
            coverage2010 = 0
            coverage2013 = 0
            p = 0
            year = 2010
            doStuffDisDrug(diseasename, disetype, color, efficacy2010, efficacy2013, coverage2010, coverage2013, p,
                           year)
            mark += 1
            efficacy2010 = 0

        mark = 0
        for k in [178]:
            colors = ['#0083CA', '#0083CA', '#0083CA', '#FFB31C', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9',
                      '#CAEEFD',
                      '#546675', '#8A5575', '#305516']
            drugNames = ['Praziquantel (Pzq)']
            disetype = 'Schistosomiasis_Eff'
            color = colors[j % 12]
            diseasename = drugNames[mark]
            efficacy2010 += stripdata(k, 2)
            efficacy2013 = 0
            coverage2010 = 0
            coverage2013 = 0
            p = 0
            year = 2010
            doStuffDisDrug(diseasename, disetype, color, efficacy2010, efficacy2013, coverage2010, coverage2013, p, year)
            mark += 1
            efficacy2010 = 0


        mark = 0
        for k in [180]:
            colors = ['#0083CA', '#0083CA', '#0083CA', '#FFB31C', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9',
                      '#CAEEFD',
                      '#546675', '#8A5575', '#305516']
            drugNames = ['Ivermectin (Ivm)']
            disetype = 'Onchocerciasis_Eff_2013'
            color = colors[j % 12]
            diseasename = drugNames[mark]
            efficacy2010 = 0
            efficacy2013 = stripdata(k, 2)
            coverage2010 = 0
            coverage2013 = 0
            p = 0
            year = 2010
            doStuffDisDrug(diseasename, disetype, color, efficacy2010, efficacy2013, coverage2010, coverage2013, p,
                           year)
            mark += 1

        mark = 0
        for k in [141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 153, 158, 159]:
            colors = ['#0083CA', '#0083CA', '#0083CA', '#FFB31C', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9',
                      '#CAEEFD', '#546675', '#8A5575', '#305516']
            drugNames = [
                         'AZT + 3TC + NVP',
                         'd4T + 3TC + EFV',
                         'AZT + 3TC + EFV',
                         'TDF + 3TC + EFV',
                         'TDF + FTC + EFV',
                         'TDF + 3TC + NVP',
                         'TDF + FTC + NVP',
                         'AZT + 3TC + LPV/r',
                         'AZT + 3TC + ATV/r',
                         'ABC + 3TC + EFV',
                         'TDF + FTC + LPV/r',
                         'ABC + 3TC + LPV/r',
                         'TDF + 3TC + ATV/r']
            disetype = 'HIV_Eff'
            color = colors[j % 12]
            diseasename = drugNames[mark]
            efficacy2010 += stripdata(k, 2)
            efficacy2013 = 0
            coverage2010 = 0
            coverage2013 = 0
            p = 0
            year = 2010
            doStuffDisDrug(diseasename, disetype, color, efficacy2010, efficacy2013, coverage2010, coverage2013, p,
                           year)
            mark += 1
            efficacy2010 = 0

        mark = 0
        for k in [112,113,114,115]:
            colors = ['#0083CA', '#0083CA', '#0083CA', '#FFB31C', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9',
                      '#CAEEFD', '#546675', '#8A5575', '#305516']
            drugNames = ['DS-TB- HIV+', 'DS-TB- HIV-', 'MDR-TB', 'XDR-TB']
            disetype = 'TB_Eff'
            color = colors[j % 12]
            diseasename = drugNames[mark]
            efficacy2010 += stripdata(k, 2)
            efficacy2013 = 0
            coverage2010 = 0
            coverage2013 = 0
            p = 0
            year = 2010
            doStuffDisDrug(diseasename, disetype, color, efficacy2010, efficacy2013, coverage2010, coverage2013, p,
                           year)
            mark += 1
            efficacy2010 = 0

        mark = 0
        for k in [117, 118, 119, 120, 121, 122, 127, 128, 129, 130, 132, 133, 134, 135, 136]:
            colors = ['#0083CA', '#0083CA', '#0083CA', '#FFB31C', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9',
                      '#CAEEFD',
                      '#546675', '#8A5575', '#305516']
            drugNames = [
                'AL(p.falc)',
                'AS + SP(p.falc)',
                'DHA - PPQ(p.falc)',
                'AS + MQ(p.falc)',
                'AS + AQ(p.falc)',
                'CQ + PQ(p.falc)',
                'ART + PPQ(p.falc)',
                'QN + D(p.falc)',
                'SP(p.falc)',
                'AS + MQ + PQ(p.falc)',
                'CQ + PQ(p.vivax)',
                'AL(p.vivax)',
                'AL + PQ(p.vivax)',
                'CQ(p.vivax)',
                'AS + AQ(p.vivax)'
            ]

            disetype = 'Malaria_Eff'
            color = colors[j % 12]
            diseasename = drugNames[mark]
            efficacy2010 += stripdata(k, 2)
            efficacy2013 = 0
            coverage2010 = 0
            coverage2013 = 0
            p = 0
            year = 2010
            doStuffDisDrug(diseasename, disetype, color, efficacy2010, efficacy2013, coverage2010, coverage2013, p,
                           year)
            mark += 1
            efficacy2010 = 0


############################## 2013 efficacy data #####################################
        mark = 0
        for k in [179, 180, 181]:
            colors = ['#0083CA', '#0083CA', '#0083CA', '#FFB31C', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9',
                      '#CAEEFD',
                      '#546675', '#8A5575', '#305516']
            drugNames = ['Albendazole (Alb)', 'Mebendazole (Mbd)', 'Ivermectin + Albendazole (Ivm + Alb)']
            disetype = 'Whipworm_Eff_2013'
            color = colors[j % 12]
            diseasename = drugNames[mark]
            efficacy2010 = 0
            efficacy2013 = stripdata(k, 6)
            coverage2010 = 0
            coverage2013 = 0
            p = 0
            year = 2010
            doStuffDisDrug(diseasename, disetype, color, efficacy2010, efficacy2013, coverage2010, coverage2013, p,
                           year)
            mark += 1

        mark = 0
        for k in [172, 173, 174]:
            colors = ['#0083CA', '#0083CA', '#0083CA', '#FFB31C', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9',
                      '#CAEEFD',
                      '#546675', '#8A5575', '#305516']
            drugNames = ['Albendazole (Alb)', 'Mebendazole (Mbd)', 'Ivermectin + Albendazole (Ivm + Alb)']
            disetype = 'Roundworm_Eff_2013'
            color = colors[j % 12]
            diseasename = drugNames[mark]
            efficacy2010 = 0
            efficacy2013 = stripdata(k, 6)
            coverage2010 = 0
            coverage2013 = 0
            p = 0
            year = 2010
            doStuffDisDrug(diseasename, disetype, color, efficacy2010, efficacy2013, coverage2010, coverage2013, p,
                           year)
            mark += 1

        mark = 0
        for k in [176, 177]:
            colors = ['#0083CA', '#0083CA', '#0083CA', '#FFB31C', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9',
                      '#CAEEFD',
                      '#546675', '#8A5575', '#305516']
            drugNames = ['Albendazole (Alb)', 'Mebendazole (Mbd)']
            disetype = 'Hookworm_Eff_2013'
            color = colors[j % 12]
            diseasename = drugNames[mark]
            efficacy2010 = 0
            efficacy2013 = stripdata(k, 6)
            coverage2010 = 0
            coverage2013 = 0
            p = 0
            year = 2010
            doStuffDisDrug(diseasename, disetype, color, efficacy2010, efficacy2013, coverage2010, coverage2013, p,
                           year)
            mark += 1

        mark = 0
        for k in [187, 188, 189]:
            colors = ['#0083CA', '#0083CA', '#0083CA', '#FFB31C', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9',
                      '#CAEEFD',
                      '#546675', '#8A5575', '#305516']
            drugNames = ['Diethylcarbamazine (Dec)', 'Diethylcarbamazine + Albendazole (Dec + Alb)',
                         'Ivermectin + Albendazole (Ivm + Alb)']
            disetype = 'LF_Eff_2013'
            color = colors[j % 12]
            diseasename = drugNames[mark]
            efficacy2010 = 0
            efficacy2013 = stripdata(k, 6)
            coverage2010 = 0
            coverage2013 = 0
            p = 0
            year = 2010
            doStuffDisDrug(diseasename, disetype, color, efficacy2010, efficacy2013, coverage2010, coverage2013, p,
                           year)
            mark += 1

        mark = 0
        for k in [183]:
            colors = ['#0083CA', '#0083CA', '#0083CA', '#FFB31C', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9',
                      '#CAEEFD',
                      '#546675', '#8A5575', '#305516']
            drugNames = ['Praziquantel (Pzq)']
            disetype = 'Schistosomiasis_Eff_2013'
            color = colors[j % 12]
            diseasename = drugNames[mark]
            efficacy2010 = 0
            efficacy2013 = stripdata(k, 6)
            coverage2010 = 0
            coverage2013 = 0
            p = 0
            year = 2010
            doStuffDisDrug(diseasename, disetype, color, efficacy2010, efficacy2013, coverage2010, coverage2013, p,
                           year)
            mark += 1


        mark = 0
        for k in [185]:
            colors = ['#0083CA', '#0083CA', '#0083CA', '#FFB31C', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9',
                      '#CAEEFD',
                      '#546675', '#8A5575', '#305516']
            drugNames = ['Ivermectin (Ivm)']
            disetype = 'Onchoceriasis_Eff_2013'
            color = colors[j % 12]
            diseasename = drugNames[mark]
            efficacy2010 = 0
            efficacy2013 = stripdata(k, 6)
            coverage2010 = 0
            coverage2013 = 0
            p = 0
            year = 2010
            doStuffDisDrug(diseasename, disetype, color, efficacy2010, efficacy2013, coverage2010, coverage2013, p,
                           year)
            mark += 1

        mark = 0
        for k in [145,146, 147, 148, 149, 150,151,152,153,154,155,156, 158, 160, 163, 164]:
            colors = ['#0083CA', '#0083CA', '#0083CA', '#FFB31C', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9',
                      '#CAEEFD', '#546675', '#8A5575', '#305516']
            drugNames = [
                'AZT + 3TC + NVP',
                'ABC + 3TC + LPV / r',
                'AZT + 3TC + EFV',
                'TDF + 3TC + NVP',
                'TDF + 3TC + EFV',
                'TDF + FTC + EFV',
                'TDF + FTC + NVP',
                'TDF + 3TC + LPV / r',
                'TDF + FTC + LPV / r',
                'TDF + FTC + ATV / r',
                'ABC + 3TC + EFV',
                'AZT + 3TC + ATV / r',
                'AZT + 3TC + LPV / r',
                'ABC + 3TC + ATV / r',
                'd4T + 3TC + EFV',
                'ABC + 3TC + NVP'
            ]
            disetype = 'HIV_Eff_2013'
            color = colors[j % 12]
            diseasename = drugNames[mark]
            efficacy2010 = 0
            efficacy2013 = stripdata(k, 6)
            coverage2010 = 0
            coverage2013 = 0
            p = 0
            year = 2010
            doStuffDisDrug(diseasename, disetype, color, efficacy2010, efficacy2013, coverage2010, coverage2013, p,
                           year)
            mark += 1

        mark = 0
        for k in [112, 113, 114, 115]:
            colors = ['#0083CA', '#0083CA', '#0083CA', '#FFB31C', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9',
                      '#CAEEFD', '#546675', '#8A5575', '#305516']
            drugNames = ['DS-TB- HIV+', 'DS-TB- HIV-', 'MDR-TB', 'XDR-TB']
            disetype = 'TB_Eff_2013'
            color = colors[j % 12]
            diseasename = drugNames[mark]
            efficacy2010 = 0
            efficacy2013 = stripdata(k, 6)
            coverage2010 = 0
            coverage2013 = 0
            p = 0
            year = 2010
            doStuffDisDrug(diseasename, disetype, color, efficacy2010, efficacy2013, coverage2010, coverage2013, p,
                           year)
            mark += 1

        mark = 0
        for k in [117, 121, 122,123,124,125,126,127,128, 129,131, 132,134, 136, 137, 138, 139,140, 141, 142,143]:
            colors = ['#0083CA', '#0083CA', '#0083CA', '#FFB31C', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9',
                      '#CAEEFD',
                      '#546675', '#8A5575', '#305516']
            drugNames = [
                'AL(p.falc)',
                'ART+PPQ(p.falc)',
                'AS+AQ(p.falc)',
                'AS+MQ(p.falc)',
                'AS+MQ+PQ(p.falc)',
                'AS+SP(p.falc)',
                'AS+SP+PQ(p.falc)',
                'AT+PG(p.falc)',
                'CQ+PQ(p.falc)',
                'DHA-PPQ(p.falc)',
                'PQ(p.falc)',
                'QN(p.falc)',
                'QN + D(p.falc)',
                'CQ + PQ(p.vivax)',
                'CQ(p.vivax)',
                'DHA - PPQ(p.vivax)',
                'AL(p.vivax)',
                'QN(p.vivax)',
                'AS + AQ + PQ(p.vivax)',
                'AL + PQ(p.vivax)',
                'AS + AQ(p.vivax)'
            ]

            disetype = 'Malaria_Eff_2013'
            color = colors[j % 12]
            diseasename = drugNames[mark]
            efficacy2010 = 0
            efficacy2013 = stripdata(k, 6)
            coverage2010 = 0
            coverage2013 = 0
            p = 0
            year = 2010
            doStuffDisDrug(diseasename, disetype, color, efficacy2010, efficacy2013, coverage2010, coverage2013, p,
                           year)
            mark += 1


############################## 2015 efficacy data #####################################
        mark = 0
        for k in [256, 257, 258]:
            colors = ['#0083CA', '#0083CA', '#0083CA', '#FFB31C', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9',
                      '#CAEEFD',
                      '#546675', '#8A5575', '#305516']
            drugNames = ['Albendazole (Alb)', 'Mebendazole (Mbd)', 'Ivermectin + Albendazole (Ivm + Alb)']
            disetype = 'Whipworm_Eff_2015'
            color = colors[j % 12]
            diseasename = drugNames[mark]
            efficacy2010 = 0
            efficacy2015 = stripdata3(k, 2)
            coverage2010 = 0
            coverage2015 = 0
            p = 0
            year = 2015
            doStuffDisDrug(diseasename, disetype, color, efficacy2010, efficacy2015, coverage2010, coverage2015, p,
                           year)
            mark += 1


        mark = 0
        for k in [249, 250, 251]:
            colors = ['#0083CA', '#0083CA', '#0083CA', '#FFB31C', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9',
                      '#CAEEFD',
                      '#546675', '#8A5575', '#305516']
            drugNames = ['Albendazole (Alb)', 'Mebendazole (Mbd)', 'Ivermectin + Albendazole (Ivm + Alb)']
            disetype = 'Roundworm_Eff_2015'
            color = colors[j % 12]
            diseasename = drugNames[mark]
            efficacy2010 = 0
            efficacy2015 = stripdata3(k, 2)
            coverage2010 = 0
            coverage2015 = 0
            p = 0
            year = 2015
            doStuffDisDrug(diseasename, disetype, color, efficacy2010, efficacy2015, coverage2010, coverage2015, p,
                           year)
            mark += 1


        mark = 0
        for k in [253, 254]:
            colors = ['#0083CA', '#0083CA', '#0083CA', '#FFB31C', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9',
                      '#CAEEFD',
                      '#546675', '#8A5575', '#305516']
            drugNames = ['Albendazole (Alb)', 'Mebendazole (Mbd)']
            disetype = 'Hookworm_Eff_2015'
            color = colors[j % 12]
            diseasename = drugNames[mark]
            efficacy2010 = 0
            efficacy2015 = stripdata3(k, 2)
            coverage2010 = 0
            coverage2015 = 0
            p = 0
            year = 2015
            doStuffDisDrug(diseasename, disetype, color, efficacy2010, efficacy2015, coverage2010, coverage2015, p,
                           year)
            mark += 1


        mark = 0
        for k in [264,265,266]:
            colors = ['#0083CA', '#0083CA', '#0083CA', '#FFB31C', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9',
                      '#CAEEFD',
                      '#546675', '#8A5575', '#305516']
            drugNames = ['Diethylcarbamazine (Dec)', 'Diethylcarbamazine + Albendazole (Dec + Alb)',
                         'Ivermectin + Albendazole (Ivm + Alb)']
            disetype = 'LF_Eff_2015'
            color = colors[j % 12]
            diseasename = drugNames[mark]
            efficacy2010 = 0
            efficacy2015 = stripdata3(k, 2)
            coverage2010 = 0
            coverage2015 = 0
            p = 0
            year = 2015
            doStuffDisDrug(diseasename, disetype, color, efficacy2010, efficacy2015, coverage2010, coverage2015, p,
                           year)
            mark += 1


        mark = 0
        for k in [260]:
            colors = ['#0083CA', '#0083CA', '#0083CA', '#FFB31C', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9',
                      '#CAEEFD',
                      '#546675', '#8A5575', '#305516']
            drugNames = ['Praziquantel (Pzq)']
            disetype = 'Schistosomiasis_Eff_2015'
            color = colors[j % 12]
            diseasename = drugNames[mark]
            efficacy2010 = 0
            efficacy2015 = stripdata3(k, 2)
            coverage2010 = 0
            coverage2015 = 0
            p = 0
            year = 2015
            doStuffDisDrug(diseasename, disetype, color, efficacy2010, efficacy2015, coverage2010, coverage2015, p,
                           year)
            mark += 1

        mark = 0
        for k in [262]:
            colors = ['#0083CA', '#0083CA', '#0083CA', '#FFB31C', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9',
                      '#CAEEFD',
                      '#546675', '#8A5575', '#305516']
            drugNames = ['Ivermectin (Ivm)']
            disetype = 'Onchoceriasis_Eff_2015'
            color = colors[j % 12]
            diseasename = drugNames[mark]
            efficacy2010 = 0
            efficacy2015 = stripdata3(k, 2)
            coverage2010 = 0
            coverage2015 = 0
            p = 0
            year = 2015
            doStuffDisDrug(diseasename, disetype, color, efficacy2010, efficacy2015, coverage2010, coverage2015, p,
                           year)
            mark += 1

        mark = 0
        for k in [225, 226,227,228,229,230,231,233,235,236,237,238,239,241,246]:
            colors = ['#0083CA', '#0083CA', '#0083CA', '#FFB31C', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9',
                      '#CAEEFD', '#546675', '#8A5575', '#305516']
            drugNames = [
                'TDF + 3TC + EFV',
                'TDF + FTC + EFV',
                'AZT + 3TC + NVP',
                'TDF + 3TC + NVP',
                'AZT + 3TC + EFV',
                'ABC + 3TC + LPV/r',
                'ABC + 3TC + EFV',
                'd4T + 3TC + NVP',
                'AZT + 3TC + LPV/r',
                'TDF + 3TC + LPV/r',
                'TDF + 3TC + ATV/r',
                'TDF + FTC + LPV/r',
                'AZT + 3TC + ATV/r',
                'TDF + FTC + ATV/r',
                'ABC + ddl + LPV/r'
            ]
            disetype = 'HIV_Eff_2015'
            color = colors[j % 12]
            diseasename = drugNames[mark]
            efficacy2010 = 0
            efficacy2015 = stripdata3(k, 2)
            coverage2010 = 0
            coverage2015 = 0
            p = 0
            year = 2015
            doStuffDisDrug(diseasename, disetype, color, efficacy2010, efficacy2015, coverage2010, coverage2015, p,
                          year)
            mark += 1


        mark = 0
        for k in [194,195,196,197]:
            colors = ['#0083CA', '#0083CA', '#0083CA', '#FFB31C', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9',
                      '#CAEEFD', '#546675', '#8A5575', '#305516']
            drugNames = ['DS-TB- HIV+', 'DS-TB- HIV-', 'MDR-TB', 'XDR-TB']

            disetype = 'TB_Eff_2015'
            color = colors[j % 12]
            diseasename = drugNames[mark]
            efficacy2010 = 0
            efficacy2015 = stripdata3(k, 2)
            coverage2010 = 0
            coverage2015 = 0
            p = 0
            year = 2015
            doStuffDisDrug(diseasename, disetype, color, efficacy2010, efficacy2015, coverage2010, coverage2015, p,
                          year)
            mark += 1

        mark = 0
        for k in [199, 200, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 216, 218, 219, 220, 221, 222,223]:
            colors = ['#0083CA', '#0083CA', '#0083CA', '#FFB31C', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9',
                      '#CAEEFD',
                      '#546675', '#8A5575', '#305516']
            drugNames = [
                'AL(p.falc)',
                'AL + PQ(p.falc)',
                'ART+PPQ(p.falc)',
                'AS+AQ(p.falc)',
                'AS+MQ(p.falc)',
                'AS+MQ+PQ(p.falc)',
                'AS+SP(p.falc)',
                'AS+SP+PQ(p.falc)',
                'AT+PG(p.falc)',
                'CQ+PQ(p.falc)',
                'DHA-PPQ(p.falc)',
                'DHA-PPQ+PQ(p.falc)',
                'PQ(p.falc)',
                'QN(p.falc)',
                'QN+D(p.falc)',
                'CQ + PQ(p.vivax)',
                'CQ(p.vivax)',
                'DHA - PPQ(p.vivax)',
                'AL(p.vivax)',
                'QN(p.vivax)',
                'AS + AQ + PQ(p.vivax)',
                'AL + PQ(p.vivax)'
            ]

            disetype = 'Malaria_Eff_2015'
            color = colors[j % 12]
            diseasename = drugNames[mark]
            efficacy2010 = 0
            efficacy2015 = stripdata3(k, 2)
            coverage2010 = 0
            coverage2015 = 0
            p = 0
            year = 2015
            doStuffDisDrug(diseasename, disetype, color, efficacy2010, efficacy2015, coverage2010, coverage2015, p,
                          year)
            mark += 1

        #conn.commit()
        #conn.close()
        return 'success'
    except Exception as e:
        print(e)
        error = "Disease page not updated"
        #conn.rollback()
        #conn.close()
        return error