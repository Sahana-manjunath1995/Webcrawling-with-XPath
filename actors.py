from lxml import html
import requests
import csv


def generate_urls(url_template, page_num):
    url_list = [url_template.format(i) for i in range(1, page_num+1)]
    return url_list


def fetch_html_content(urls):

    for url in urls:
        resp = requests.get(url)
        tree = html.fromstring(resp.content)
        if resp.status_code == 200:
            yield tree


def get_actor_container(html_tree):

    actor_container = html_tree.xpath('//div[@id="main"]/div/div/div[@class="lister-list"]/div')
    yield actor_container


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


if __name__ == '__main__':
    pages = 3
    url = "https://www.imdb.com/list/ls058011111/?page=-{}/"
    urls = generate_urls(url, pages)
    html_gen = fetch_html_content(urls)
    html_content = [fetch_html_content(url)for url in urls]

    with  open('actors_info.csv', 'w',  encoding="utf-8") as csv_file:
        csvwriter = csv.writer(csv_file)
        for html_tree in html_gen:

            actor_gen = get_actor_container(html_tree)
            for actor_tree in actor_gen:
                g = csvwriter.writerows(extract_actor_data(actor_tree))