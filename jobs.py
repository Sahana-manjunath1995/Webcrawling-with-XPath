from lxml import html
import requests


def generate_urls(url_template, page_num, key_word):

    url_list = [url_template.format(key_word, i) for i in range(1, page_num+1)]
    return url_list


def fetch_html_content(url):

    resp = requests.get(url)
    tree = html.fromstring(resp.content)
    return tree


def get_job_containers(html_tree, page_num):

    job_containers = []
    for i in range(1, page_num+1):
        containers = html_tree.xpath(f'//div[@id ="internship_list_container_{i}"]/div')
        for ele in containers:
            job_containers.append([ele])
    return job_containers


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

        stipend = elmt.xpath('./div[@class="internship_meta"]/div/div[@class="internship_other_details_container"]/div[@class="other_detail_item_row"]/div/div/span[@class="stipend"]/text()')
        if len(stipend) == 0:
            data.append('')
        else:
            data.append(stipend[0])

        view_det = elmt.xpath('./div/div[@class="cta_container"]/a/@href')
        data.append(view_det[0])
    return data


if __name__ == '__main__':
    pages = 3
    keyword = "marketing"
    url_temp = "https://internshala.com/internships/keywords-{}/page-{}/"
    urls = generate_urls(url_temp, pages, keyword)
    html_content = [fetch_html_content(url)for url in urls]
    extract_job_containers = [get_job_containers(html_tree,pages) for html_tree in html_content]
    container_path_data = [extract_data_container_path(val)for row in extract_job_containers for val in row]
    result = []
    for value in container_path_data:
        final = []
        for stg in value:
            rpl = stg.replace('\xa0', " ")
            strp = rpl.strip()
            nw_strg = strp.strip('/n')
            final.append( nw_strg)

        if final:
            result.append(final)

    with  open('job_info.csv','w', encoding="utf-8") as res:
        for row in result:
            line = ",".join(row)
            res.write(line+'\n')
