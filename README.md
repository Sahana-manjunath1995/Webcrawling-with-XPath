# Webcrawling-with-XPath

This project aims at generating short railway station codes by using XPath.

## System design for web crawling

![image](https://user-images.githubusercontent.com/115713117/223017250-466d60be-bca6-4690-9dcb-9d364ffbee00.png)


## Requiremnts
- lxml module
- requests module
- pymysql

## Following steps are included in the project:

### Step 1
Make a connection to railway database using pymysql
```
conn = pymysql.connect(
        host='localhost',
        user='root',
        password = "root",
        db='railway',
        )
cur = conn.cursor()
```

### Step 2
Make a request to url by using requests module and get the html response content.
```
url = "https://www.prokerala.com/travel/indian-railway/karnataka-stations/"
resp = requests.get(url)
```

### Step 3
Generate tree using html response content and crawl the table using xpath.
```
tree = html.fromstring(resp.content)
table = tree.xpath("//table[@id='pageTable']")[0]
rows = table.xpath('./tbody/tr')
```

### Step 4
Extract the railway station names in the given table by using XPath and store them in the two dimensional list.
```
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
```

### Step 5
Iterate through two dimensional list remove the vowels from the station names, if the first value of letter is vowel
append the value to result list. Consonants in station names values are appended to result list.
```
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
```

### Step 6
Iterate through the resulted consonant list and based on length of the list, generate new list by appending the first element at 0 index and first letter of second element at index 1. Iterate the new list and  generate the code for station name based on length of the list.
```
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
```

### Step 7
Zip the two lists with place names and shortcodes for railway_station using zip(), then insert them into the Mysql database
```
 res = list(zip(data_one, gen_code))
 mysql_query='''\
 Insert into railway_project (station_name, code) values (%s, %s)
 '''
cur.executemany(mysql_query, res)
conn.commit()
```
```

In this project we can learn how to crawl the table and store the generated short codes in the mysql database without duplicates.
For more code refer to railway_code.py.
