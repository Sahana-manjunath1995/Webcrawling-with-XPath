# Webcrawling-with-XPath

The main goal of this project is to extract job and actor detail from websites by navigating through html elements with xpath. Crawled data is stored in two dimensional list. Then two-dimensional list was inserted into Mysql database.

## Why xpath ?
   XPath stands for XML Path Language. It uses simple "path like" syntax to identify and navigate nodes in an HTML document.
   
## System design for web crawling

![image](https://user-images.githubusercontent.com/115713117/223172165-087c5a04-8ade-4b4a-8216-2a5e1dc370ef.png)



## Requirements
    lxml module
    requests module
    csv module

1. Use requests module to download html contents from the specified urls (eg:"https://internshala.com/internships/keywords-python/").

2. Fetch html tree elements using html.fromstring() method and store it in list.

3. Extract data containers by using xpath that makes use of individual html tree and store the elements of container in the list.

4. Individual data container is passed as parameter to the function and data is extracted for required fields using xpath expression.

5. Result is stored in csv file

6. Run the code by using following command
```
python3 jobs.py
```

In the current project we can learn how to crawl different websites and save the crawled data in a csv file. You can find the complete code in jobs.py and actors.py







