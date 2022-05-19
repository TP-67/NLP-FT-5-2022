import scrapy
import numpy as np
import pandas as pd
import xlsxwriter


class wordCountSpider(scrapy.Spider):
    name = 'wordCount'
    start_urls = [
        'https://lilianweng.github.io'
    ]

    def parse(self, response):
        content = response.xpath('//*[@id="top"]/main/article/section/p/text()').extract()
        content_processed = ''

        for i in content:
            content_temp = i.replace('\'', '')
            content_temp = content_temp.replace('.', '')
            content_temp = content_temp.replace(',', '')
            content_temp = content_temp.replace(':', '')
            content_temp = content_temp.replace('\n', '')
            content_temp = content_temp.replace('(', '')
            content_temp = content_temp.replace(')', '')
            content_temp = content_temp.replace('\\', '')
            content_temp = content_temp.replace('$', '')
            content_temp = content_temp.replace('[', '')
            content_temp = content_temp.replace(']', '')
            content_temp = content_temp.replace('{', '')
            content_temp = content_temp.replace('}', '')
            content_temp = content_temp.replace('^', '')

            content_processed += content_temp

        word_split = content_processed.split()

        frequency = {}
        for item in word_split:
            if item in frequency:
                frequency[item] += 1
            else:
                frequency[item] = 1

        with xlsxwriter.Workbook('word_count.xlsx') as workbook:
            worksheet = workbook.add_worksheet()

            worksheet.write(0, 0, 'Word')
            worksheet.write(0, 1, 'Frequency')

            for i, (k, v) in enumerate(frequency.items(), start=1):
                worksheet.write(i, 0, k)
                worksheet.write(i, 1, v)
