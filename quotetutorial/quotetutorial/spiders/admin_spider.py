import scrapy

class QuoteSpider(scrapy.Spider):
    name = 'admins'
    start_urls = [
        'http://103.27.36.114/sipandu2/ID_barang_perbandingan.php'
    ]

    def parse(self, response):
        all_div_quotes = response.css('table.table_report')[0]
        title = all_div_quotes.css('td::text').extract()
        yield {
            'title' : title,
        }