import scrapy


class StackOverSpider(scrapy.Spider):
    """Scraper for google serach."""
    name = "stack_spider"

    def __init__(self):
        """Initialize the spider."""
        super(StackOverSpider, self).__init__()
        self.start_urls = ['StackOverflow.com/jobs']

    def parse(self, response):
        """Crawl through search and return first page information."""
        SET_SELECTOR = '.-job-summary'
        for post in response.css(SET_SELECTOR):

            TITLE_SELECTOR = 'h2 a ::text'
            SITE_SELECTOR = 'h2 a ::attr(href)'
            # COMPANY_NAME = 'div '
            yield{
                'title': post.css(TITLE_SELECTOR).extract(),
                'site': post.css(SITE_SELECTOR).extract_first()
            }