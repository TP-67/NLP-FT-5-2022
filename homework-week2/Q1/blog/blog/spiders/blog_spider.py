import scrapy
import numpy as np
import pandas as pd


class BlogSpider(scrapy.Spider):
    name = 'blog'
    start_urls = [
        'https://lilianweng.github.io'
    ]

    def parse(self, response):
        title = response.css('h2::text').getall()
        time = response.xpath('//*[@id="top"]/main/article/footer/span/text()').extract()
        mixed = response.xpath('//*[@id="top"]/main/article/footer/text()').extract()

        title_processed = []
        for i in title:
            title_index = i.index('\n')
            title_processed.append(i[:title_index])

        time_processed = time

        author = []
        reading_time = []
        for i in mixed:
            try:
                mixed_index = i.index('\xa0')
                t = i.replace('\xa0', '')
                t = t.replace('·', '')
                t_index = t.index('min') + 3
                author.append(t[t_index:])
                reading_time.append(t[:t_index])
            except ValueError:
                pass

        print('*************************************************************')
        print(title_processed)
        print(time_processed)
        print(author)
        print(reading_time)
        print('*************************************************************')

        output = [title_processed, time_processed, author, reading_time]
        output = np.transpose(np.array(output))
        df = pd.DataFrame(output)
        df.columns = ['Blog Name', 'Publish Date', 'Author', 'Reading Time']
        writer = pd.ExcelWriter('blog.xlsx', engine='xlsxwriter')
        df.to_excel(writer, sheet_name='welcome', index=False)
        writer.save()
