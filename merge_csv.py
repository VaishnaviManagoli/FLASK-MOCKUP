import csv

with open('shared_articles.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]
    headers = data[0]

headers.append("poster_link")

with open("final.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)

with open("articles_links.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    articles_link_items = data[1:]

for articles_item in all_articles:
    poster_found = any(articles_item[8] in articles_link_items for articles_link_items in articles_link_items)
    if poster_found:
        for articles_link_items in articles_link_items:
            if articles_item[8] == articles_link_items[0]:
                articles_item.append(articles_link_items[1])
                if len(articles_item) == 28:
                    with open("final.csv", "a+") as f:
                        csvwriter = csv.writer(f)
                        csvwriter.writerow(articles_item)