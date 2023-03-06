# Webcrawling-with-XPath

This project aims at generating short railway station codes by using XPath.

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

### Step 3
Generate tree using html response content and crawl the table using xpath.

### Step 4
Extract the railway station names in the given table by using XPath and store them in the two dimensional list.

### Step 5
Iterate through two dimensional list remove the vowels from the station names, if the first value of letter is vowel
append the value to result list. Consonants in station names values are appended to result list.

### Step 6
Iterate through the resulted list and based on length of the list, generate new list by appending the first element at 0 index and first letter of second element at index 1.

### Step 7
Iterate the new list and  generate the code for station name based on length of the list.

In this project we can learn on how to crawl the table and store the generated short codes in mysql database without duplicates
