# Webcrawling-with-XPath

The main goal of this project is to extract data from websites by navigating through html elements using xpath. I have extracted job details and actor details from relevant websites, stored data in different csv file.

## Why xpath ?
   XPath stands for XML Path Language. It uses simple "path like" syntax to identify and navigate nodes in an HTML document.
   
## System design for web crawling

![image](https://user-images.githubusercontent.com/115713117/223017250-466d60be-bca6-4690-9dcb-9d364ffbee00.png)

## Requirements
    lxml module
    requests module
    csv module

## Following steps are included in the project:

### Step 1:

Use requests module to download html contents from the specified urls (eg:"https://internshala.com/internships/keywords-python/").

Refer jobs.py

```
       def generate_urls(url_template, page_num, key_word):

          url_list = [url_template.format(key_word, i) for i in range(1, page_num+1)]
          return url_list
       pages = 3
       keyword = "marketing"
       url_temp = "https://internshala.com/internships/keywords-{}/page-{}/"
       urls = generate_urls(url_temp, pages, keyword)
```

Refer actors.py

```
       def generate_urls(url_template, page_num):
          url_list = [url_template.format(i) for i in range(1, page_num+1)]
          return url_list
       pages = 3
       url = "https://www.imdb.com/list/ls058011111/?page=-{}/"
       urls = generate_urls(url, pages)
```

### Step 2:

Fetch html tree elements using html.fromstring() method and store it in list.

Refer jobs.py
```
       def fetch_html_content(url):

         resp = requests.get(url)
         tree = html.fromstring(resp.content)
       return tree
```
   
 Refer actors.py
```
      def fetch_html_content(urls):

       for url in urls:
           resp = requests.get(url)
           tree = html.fromstring(resp.content)
           if resp.status_code == 200:
               yield tree
   
```

### Step 3:

Extract data containers by using xpath that makes use of individual html tree and store the elements of container in the list.

Refer jobs.py
 ```
      def get_job_containers(html_tree, page_num):

       job_containers = []
       for i in range(1, page_num+1):
           containers = html_tree.xpath(f'//div[@id ="internship_list_container_{i}"]/div')
           for ele in containers:
               job_containers.append([ele])
       return job_containers

```
   
 Refer actors.py
```
      def get_actor_container(html_tree):

       actor_container = html_tree.xpath('//div[@id="main"]/div/div/div[@class="lister-list"]/div')
       yield actor_container

```

### Step 4:

Individual data container is passed as parameter to the function and data is extracted for required fields using xpath expression.

Refer jobs.py
 ```
      def extract_data_container_path(div):

    for elmt in div :
        data = []
        head_tag=  elmt.xpath('./div[@class="internship_meta"]/div/div/h3[@class="heading_4_5 profile"]/a/text()')
        data.append(head_tag[0])
        company_name = elmt.xpath('./div[@class="internship_meta"]/div/div/h4[@class="heading_6 company_name"]/div/a/text()')

        if len(company_name) == 0:
            data.append('')

        else:
            data.append(company_name[0])

        loct = elmt.xpath('./div[@class="internship_meta"]/div/div[@id="location_names"]/span/a/text()')
        if len(loct)  == 0:
            data.append('')

        else:
            joined = ','.join(loct)
            data.append(joined)

        start_date = elmt.xpath('./div[@class="internship_meta"]/div/div[@class="internship_other_details_container"]/div/div/div[@id="start-date-first"]/span/text()')
        if len(start_date)  == 0:
            data.append('')

        else:
            data.append(start_date[0])

        duration = elmt.xpath('./div[@class="internship_meta"]/div/div[@class="internship_other_details_container"]/div/div/div[@class="item_body"]/text()')
        if len(duration) < 3:
            data = data
        else:
            data.append(duration[2])

        stipend =              elmt.xpath('./div[@class="internship_meta"]/div/div[@class="internship_other_details_container"]/div[@class="other_detail_item_row"]/div/div/span[@class="stipend"]/text()')
        if len(stipend) == 0:
            data.append('')
        else:
            data.append(stipend[0])

        view_det = elmt.xpath('./div/div[@class="cta_container"]/a/@href')
        data.append(view_det[0])
    return data

```
   
Refer actors.py
```
     def extract_actor_data(row) :

    data = []
    result = []
    for tree_vales in row:
        actor_details = []
        image = tree_vales.xpath('./div/a/@href')
        actor_details.append(image[0])
        name = tree_vales.xpath('./div/h3/a/text()')
        actor_details.append(name[0])
        movie_name = tree_vales.xpath('./div/p/a/text()')
        actor_details.append(movie_name[0])
        other_detail =  tree_vales.xpath('./div/p/text()')
        actor_details.append(other_detail[3])
        data.append(actor_details)

    for row in data:
        final = []
        for stg in row:
            nw_strg = stg.strip()
            final.append(nw_strg)
        result.append(final)

    return (result)
```

### Step 5:

Result is stored in csv file








