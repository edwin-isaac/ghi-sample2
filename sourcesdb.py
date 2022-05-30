import sqlite3
import pandas as pd
import math
import sys

def createTablesSources():
    #conn = sqlite3.connect('F:/global-health-impact-web/ghi.db')
    conn = sqlite3.connect('ghi.db')
    conn.execute("DROP TABLE IF EXISTS sources")
    conn.execute("DROP TABLE IF EXISTS sourcescores2010")
    conn.execute("DROP TABLE IF EXISTS sourcescores2013")
    conn.execute("DROP TABLE IF EXISTS sourcescores2015")

    conn.execute('''CREATE TABLE sources
                         (source text, name text, color text)''')
    conn.execute('''CREATE TABLE sourcescores2010
                         (source text, disease text, score real)''')
    conn.execute('''CREATE TABLE sourcescores2013
                         (source text, disease text, score real)''')
    conn.execute('''CREATE TABLE sourcescores2015
                         (source text, disease text, score real)''')
    conn.commit()
    conn.close()


def addSourceScore(sourcescores, row, column, data, disease):

    if(data.isnull().iloc[row,column] == False):
        if(data.isnull().iloc[row, column] == False and data.iloc[row, column].upper() != 'TOTAL'):
            source = data.iloc[row,column]
            if(sourcescores.__contains__(source) == False):
                sourcescores[source] = {}
            if(sourcescores[source].__contains__(disease) == False):
                sourcescores[source][disease] = []
            if(data.isnull().iloc[row,column + 1] == False and data.iloc[row,column + 1].find('-') == -1):
                try:
                    score = float(data.iloc[row,column + 1].replace(',', ''))
                    sourcescores[source][disease].append([source, disease, score])
                except ValueError:
                    print(sys.exc_info())
                    print('row: ' + str(row) + ' column: ' + str(column))

def SourcesDbUpdate():
    try:
        # conn = sqlite3.connect('./ghi_debug.db')
        # conn = sqlite3.connect('server_ghi.db')
        conn = sqlite3.connect('ghi.db')

        conn.execute("DROP TABLE IF EXISTS sources")
        conn.execute("DROP TABLE IF EXISTS sourcescores2010")
        conn.execute("DROP TABLE IF EXISTS sourcescores2013")
        conn.execute("DROP TABLE IF EXISTS sourcescores2015")

        conn.execute('''CREATE TABLE sources
                     (source text, name text, color text)''')
        conn.execute('''CREATE TABLE sourcescores2010
                     (source text, disease text, score real)''')
        conn.execute('''CREATE TABLE sourcescores2013
                     (source text, disease text, score real)''')
        conn.execute('''CREATE TABLE sourcescores2015
                     (source text, disease text, score real)''')

        datasrc = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRPq5xp1sZoC6rW_9ALBhiq2hMFOnoyCVxaeWEu82X3MIoycBNAAtzSkpJMRsRJF9mSl8zQpc4wC1mq/pub?output=csv'

        sources = {'GF': ['GF', 'The Global Fund', '#4285F4'],
                   'GFOLD': ['GFOLD', 'Unknown', '#EA4335'],
                   'GDF': ['GDF', 'Global Drug Facility', '#FF77B6'],
                   'IDA': ['IDA', 'IDA Foundation', '#FBBC04'],
                   'PEPFAR': ['PEPFAR', 'President\'s Emergency Plan For AIDS Relief', '#34A853'],
                   'SCMS': ['SCMS', 'Supply Chain Mangement System', '#FF6D01'],
                   'UNICEF': ['UNICEF', 'United Nations Children\'s Fund', '#46BDC6'],
                   'UNITAID': ['UNITAID', 'Unitaid', '#7BAAF7'],
                   'WHOCPS': ['WHOCPS', 'WHO Contracting and Procurement Service','#F07B72'],
                   'WHO': ['WHO', 'World Health Organization', '#FCD04F'],
                   'MP': ['MP', 'Unknown', '#71C287'],
                   'UNDP': ['UNDP', 'United Nations Development Program', '#264c8a'],
                   'CHAI': ['CHAI', 'Clinton Health Access Initiative', '#EB8D48']}

        for row in sources:
            conn.execute('insert into sources values (?,?,?)', sources[row])

        data = pd.read_csv(datasrc, skiprows=2)

        sourcescores2010 = {}
        sourcescores2013 = {}
        sourcescores2015 = {}

        for i in range(data.count().max()):
            # entering HIV data
            disease = 'HIV'
            # for 2010
            addSourceScore(sourcescores2010, i, 0, data, disease)

            # for 2013
            addSourceScore(sourcescores2013, i, 12, data, disease)

            # for 2015
            addSourceScore(sourcescores2015, i, 21, data, disease)

            # entering TB data
            disease = 'TB'
            # for 2010
            addSourceScore(sourcescores2010, i, 3, data, disease)

            # for 2013
            addSourceScore(sourcescores2013, i, 9, data, disease)

            # for 2015
            addSourceScore(sourcescores2015, i, 18, data, disease)

            # entering TB data
            disease = 'Malaria'
            # for 2010
            addSourceScore(sourcescores2010, i, 6, data, disease)

            # for 2013
            addSourceScore(sourcescores2013, i, 15, data, disease)

            # for 2015
            addSourceScore(sourcescores2015, i, 24, data, disease)

        for i in sourcescores2010:
            for j in sourcescores2010[i]:
                for row in sourcescores2010[i][j]:
                    #print("Inserting into sourcescore2010")
                    conn.execute('insert into sourcescores2010 values (?,?,?)', row)

        for i in sourcescores2013:
            for j in sourcescores2013[i]:
                for row in sourcescores2013[i][j]:
                    #print("Inserting into sourcescore2013")
                    conn.execute('insert into sourcescores2013 values (?,?,?)', row)

        for i in sourcescores2015:
            for j in sourcescores2015[i]:
                for row in sourcescores2015[i][j]:
                    #print("Inserting into sourcescore2015")
                    conn.execute('insert into sourcescores2015 values (?,?,?)', row)

        conn.commit()
        conn.close()
        return 'success'
    except Exception as e:
        print(e)
        error = "Sources page not updated"
        conn.rollback()
        conn.close()
        return error
