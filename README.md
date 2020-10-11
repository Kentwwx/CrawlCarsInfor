# CrawlCarsInfo
crawl data about car XC90


This project is going to use web crawling to get data about a volvo xc90 car infomation.

This project will use scrapy to do the web crawling. Language is python.

Use xpath to extract data we need. 

Quick look to xpath:

Example:

.//div[contains(@class,"threadlist_author pull_right")]//span[contains(@class,"frs-author-name-wrap")]/a/text()

"." means current node

"//div[contains(@class,"threadlist_author pull_right")]" means select node "div" that has property "class" with value "threadlist_author pull_right".

"//span[contains(@class,"frs-author-name-wrap")]" means within the div metioned above, select node "span" that has property "class" with value "frs-author-name-wrap".

"/a/" means do not select tag a. 

"text()" Things we need. 
