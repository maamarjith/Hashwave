import scrapy
class OlxSpider(scrapy.Spider):
    name = 'OlxScrapy'
    start_urls = [ 'https://www.olx.in/kozhikode_g4058877/for-rent-houses-apartments_c1723']
    def parse(self, response):
        for link in response.css('li.EIR5N a::attr(href)'):
            yield response.follow(link.get(), callback=self.parse2)
    def parse2(self,response):
        try:
            yield {
                'property_name': response.css('h1._3rJ6e::text').get(),
                'property_id':  response.css('strong::text')[2].getall(),
                'breadcrumbs': response.css('a._3C_pO::text').getall(),
                'price': response.css('span._2xKfz::text').get().replace("₹",""),
                'image_url': response.css('img._39P4_').attrib['src'],
                'seller_name': response.css('div._3oOe9::text').get(),
                'location': response.css('span._2FRXm::text').get(),
                'property_type': response.css('span._2vNpt::text').get(),
                'bathrooms': response.css('span._2vNpt::text')[1].get(),
                'bedrooms': response.css('span._2vNpt::text')[2].get(),
            }
        except:
            yield {
                'property_name': response.css('h1._3rJ6e::text').get(),
                'property_id': response.css('strong::text')[2].getall(),
                'breadcrumbs': response.css('a._3C_pO::text').getall(),
                'price': response.css('span._2xKfz::text').get().replace("₹",""),
                'image_url': response.css('img.UYvAv').attrib['src'],
                'seller_name': response.css('div._3oOe9::text').get(),
                'location': response.css('span._2FRXm::text').get(),
                'property_type': response.css('span._2vNpt::text').get(),
                'bathrooms': response.css('span._2vNpt::text')[1].get(),
                'bedrooms': response.css('span._2vNpt::text')[2].get(),
            }