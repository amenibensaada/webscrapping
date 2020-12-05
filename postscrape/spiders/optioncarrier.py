import scrapy


class PostsSpider(scrapy.Spider):
    name = 'posts2'
    start_urls = [
        'https://www.optioncarriere.tn/emploi-stage-pfe.html'
    ]

    def parse(self, response):
        for post in response.css('p.company'):
            print(post)
            yield {
                'company_name': post.css(' p::text')[0].get(),
                # 'description': post.css('div.desc div::text')[1].get()
                # 'date': post.css('.post-header a::text')[1].get(),
                # 'author':post.css('.post-header a::text')[2].get()

            }
