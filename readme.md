# Web Crawling using xPath

The main goal of this project is to extract data from websites by navigating through html elements using xpath. I have extracted job details and actor details from relevant websites, stored data in different csv file.

## Why xpath ?
   XPath stands for XML Path Language. It uses simple "path like" syntax to identify and navigate nodes in an HTML document.

## Requirements
    lxml module
    requests module
    csv module

## Following steps are included in the project:

### Step 1:

    Use requests module to download html contents from the specified urls (eg:"https://internshala.com/internships/keywords-python/")

### Step 2:

    Fetch html tree elements using html.fromstring() method and store it in list.

### Step 3:

    Extract data containers by using xpath that makes use of individual html tree and store the elements of container in the list.

### Step 4:

    Individual data container is passed as parameter to the function and data is extracted for required fields using
    xpath expression

### Step 5:

    Result is stored in csv file







