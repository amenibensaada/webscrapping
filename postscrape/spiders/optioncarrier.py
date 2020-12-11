import scrapy


class PostsSpider(scrapy.Spider):
    name = 'posts2'
    start_urls = [
        'https://www.optioncarriere.tn/emploi-stage-pfe.html'
    ]

    def parse(self, response):
        for post in response.css('.job'):
            print("test", post.css('.badge::text').get())
            yield {
                # 'company_name': post.css('p::text')[0].get(),
                'description': post.css('div.desc::text').get(),
                'title': post.css('a::text').get(),
                'date': post.css('.badge::text').get()
                # 'author':post.css('.post-header a::text')[2].get()
            }
            next_page = response.css('a#more-jobs::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
