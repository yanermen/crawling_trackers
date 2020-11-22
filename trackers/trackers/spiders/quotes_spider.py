import scrapy


class TrackersSpider(scrapy.Spider):
    name = 'trackers'

    start_urls = [
        'https://whotracks.me/websites/mobile.de.html',
        'https://whotracks.me/websites/chip.de.html',
        'https://whotracks.me/websites/spiegel.de.html',
        'https://whotracks.me/websites/zdf.de.html',
        'https://whotracks.me/websites/otto.de.html',
        'https://whotracks.me/websites/heise.de.html',
        'https://whotracks.me/websites/real.de.html',
        'https://whotracks.me/websites/thomann.de.html',
        'https://whotracks.me/websites/postbank.de.html',
    ]

    def parse(self, response):
        page = response.url.split('/')[-1]
        filename = f'trackers-{page}'
        trackers_name = response.css('.entity-name::text').getall()
        without_double_name = set(trackers_name)
        with open(filename, 'a') as f:
            f.write(str(without_double_name))


