# Webcrawling-with-XPath

The main objective of this project is to crawl table data on Karnataka railroad stations website. The table data is obtained by navigating through each html element using XPath and stored in a two dimensional list. Later, the two-dimensional list was stored in a MySql database.

## System design for web crawling

![image](https://user-images.githubusercontent.com/115713117/223156592-3174d4e9-8e5d-40cc-9bf7-e4fab0eadd73.png)

## Requirements
- lxml module
- requests module
- pymysql
- docker

## Following steps are used:

1. Make a connection to railway database present in docker container using pymysql

2. Make a request to url by using requests module and get the html response content.

3. Generate tree using html response content and crawl the table using xpath.

4. Extract the railway station names in the given table by using XPath and store them in the two dimensional list.

5. Iterate through two dimensional list remove the vowels from the station names, if the first value of letter is vowel

6. Iterate through the resulted consonant list and based on length of the list, generate new list by appending the first element at 0 index and first letter of second    element at index 1. Iterate the new list and  generate the code for station name based on length of the list.

7. Zip the two lists with place names and shortcodes for railway_station using zip(), then insert them into the Mysql database

8. Run the code by using following command
```
python3 railway_code.py
```

In this project we can learn how to crawl the table and store the generated short codes in the mysql database without duplicates.
For complete code refer to railway_code.py.
