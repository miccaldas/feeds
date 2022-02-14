import scrapy


class RssSpider(scrapy.Spider):
    name = "rss"
    start_urls = ["https://doordash.engineering/2020/06/29/doordashs-new-prediction-service/"]

    def parse(self, response):
        title = response.xpath("//h1/text()").getall()
        content = response.xpath("//span/text()").getall()

        for i in zip(title, content):
            results = {
                "title": i[0],
                "content": i[1],
            }

            yield results
