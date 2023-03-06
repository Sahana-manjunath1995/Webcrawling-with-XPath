from lxml import html
import requests
import pymysql


conn = pymysql.connect(
        host='localhost',
        user='root',
        password = "root",
        db='railway',
        )
cur = conn.cursor()


def extract_column_data(row):
    ''' This function extracts the data from station name column and stores in list data type'''

    td_arr = row.xpath('./td')
    val = []
    count = 0
    for td in td_arr:
        if count == 2:
            atag = td.xpath('./a')
            if len(atag) == 0:
                val.append(td.text)
            else:
                val.append(atag[0].text)
        count += 1
        row_values= list(map(lambda x: x.strip(), val))

    return(row_values)


def remove_vowels(row_values):
    ''' This function removes vowels from row_values and stores different consonants in list data type'''

    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    cons_lis = []
    for i in row_values:
        ltr_lis = []
        for stg in i:
            if stg[0] in vowels:
                ltr_lis.append(stg[0])
            for cons in stg:
                if cons not in vowels and cons not in ltr_lis:
                    ltr_lis.append(cons)
                    j = ''.join(ltr_lis)
            cons_lis.append(j.split())
    return cons_lis


def generate_code(data_two):

    ''' This function generates code for the station name and stores result in list data type'''

    data_three = []
    for str_spl in data_two:
        if len(str_spl) == 1:
            data_three.append([str_spl[0]])
        if len(str_spl) > 1:
            data_three.append([str_spl[0]+str_spl[1][0]])
    data_four = []
    for i in data_three:
        for st in i:
            if len(st) <= 4:
                 data_four.append([st.upper()])

            if len(st) > 4:
                req = st[0] +  st[1] + st[2]+ st[-1]
                data_four.append([req.upper()])
    return(data_four)


if __name__ == '__main__':
    url = "https://www.prokerala.com/travel/indian-railway/karnataka-stations/"
    resp = requests.get(url)
    tree = html.fromstring(resp.content)
    table = tree.xpath("//table[@id='pageTable']")[0]
    rows = table.xpath('./tbody/tr')
    data_one = [extract_column_data(row) for row in rows]
    data_two = remove_vowels(data_one)
    gen_code  =  generate_code(data_two)
    res = list(zip(data_one, gen_code))
    mysql_query='''\
    Insert into railway_project (station_name, code) values (%s, %s)
    '''
    cur.executemany(mysql_query, res)
    conn.commit()
