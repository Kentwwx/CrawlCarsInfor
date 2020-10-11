import json

with open('F:/testCrawl/items.json') as f:
    rownum = 0
    new_list = json.load(f)
    for i in new_list:
        rownum += 1
        print("""line{}:  title:{},  car:{},  reply:{}.""".format(rownum,
                                                                     i['title'][0],
                                                                     i['car'][0],
                                                                     i['reply'][0]))