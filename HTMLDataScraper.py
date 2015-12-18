#importing the required packages
from bs4 import BeautifulSoup
from urllib import urlopen
import lxml.html
import urllib
from Property import *
from LinkTraversal import *
import csv
import re
import logging.config

class HTMLDataScraper:
    """This class scraps the data from the table"""
    
    #constructor
    def __init__(self):
        #create logger
        self.logger = logging.getLogger("HTMLDataScraper")

        #create console handler and set level to DEBUG
        logging.basicConfig(filename='handler1.log',level=logging.DEBUG,
                format='%(asctime)s.%(msecs)d %(levelname)s %(module)s - %(funcName)s: %(lineno)s %(message)s')
        
    def fetch_year(self):
        """Fetching the year"""
        logging.info('Started to fetch year')
        
        for month in PropertyFile.url_data:
            
            #Opening the month URL
            connection = urllib.urlopen(month)
            dom =  lxml.html.fromstring(connection.read())
            page = lxml.html.tostring(dom,pretty_print=True,method="html")
            self.soup = BeautifulSoup(page,'html.parser')
            table=self.soup.findAll('table',{'class':'table_brdr'})
            title=self.soup.find('h2')
            if title:
                try:
                    PropertyFile.year_num=title.findNext('h2').text
                    PropertyFile.year_num=PropertyFile.year_num.encode('utf-8')
                    for i in PropertyFile.year_charac:
                        PropertyFile.year_num=PropertyFile.year_num.replace(i,'')
                        
                    if PropertyFile.year_num==None:
                        title=self.soup.find('h2')
                        PropertyFile.year_num=title.find('br')
                        PropertyFile.year_num=PropertyFile.year_num.encode('utf-8')
                        for i in PropertyFile.year_charac:
                            PropertyFile.year_num=PropertyFile.year_num.replace(i,'')
                            
                        if PropertyFile.year_num==None:
                            PropertyFile.year_num=title.findNext('h3').text
                            PropertyFile.year_num=PropertyFile.year_num.encode('utf-8')
                            for i in PropertyFile.year_charac:
                                PropertyFile.year_num=PropertyFile.year_num.replace(i,'')
                                
                                
                except:
                    self.logger.exception('fetching year has stopped...')
                    pass
            else:
                title=self.soup.find('table',{'cellpadding':'0'})
                PropertyFile.year_num=title.find('strong').text
                PropertyFile.year_num=PropertyFile.year_num.encode('utf-8')
                

    def fetch_table(self):
        """Fetching letter number, topic, href"""
        logging.info('Started to fetch data')
        for month in PropertyFile.url_data:
            
            #Opening the month URL
            connection = urllib.urlopen(month)
            dom =  lxml.html.fromstring(connection.read())
            page = lxml.html.tostring(dom,pretty_print=True,method="html")
            self.soup = BeautifulSoup(page,'html.parser')
            table=self.soup.findAll('table',{'class':'table_brdr'})
            if table:        
                for row in table:
                    try:
                        category=row.findPreviousSibling().text
                        category=category.encode('utf-8').strip()
                        tr=row.findAll('a')
                        cat=len(tr)
                        while cat>0:
                            PropertyFile.category_list.append(category)
                            PropertyFile.year_list.append(PropertyFile.year_num)
                            cat-=1
                        for cell in tr:
                            letter_number=cell.text
                            if letter_number!='WORD':
                                href=cell.get('href')
                                for i in PropertyFile.href_charac:
                                    href = href.replace(i, "")
                                href=href.encode('utf-8')
                                PropertyFile.href_list.append(href)
                            topic=cell.findNext('td').text
                            for i in PropertyFile.topic_charac:
                                topic = topic.replace(i, "")
                                
                            if 'WORD' in letter_number:
                                    letter_number.remove(letter_number)
                                
                            topic=topic.encode('utf-8').strip()
                                
                            letter_number=letter_number.encode('utf-8')
                                
                            PropertyFile.letter_no.append(letter_number)
                            PropertyFile.topic_list.append(topic)
                    except:
                        self.logger.exception('fetching data has stopped...')
                        pass
                            
            else:
                table=self.soup.findAll('table',{'cellpadding':'5'})
                if table:
                    for row in table:
                        try:
                            category=row.findPreviousSibling().text
                            category=category.encode('utf-8')
                            for i in PropertyFile.category_charac:
                                category=category.replace(i,'')
                                
                            tr=row.findAll('a')
                            cat=len(tr)
                            while cat>0:
                                PropertyFile.category_list.append(category)
                                PropertyFile.year_list.append(PropertyFile.year_num)
                                cat-=1
                            for cell in tr:
                                letter_number=cell.text
                                if letter_number!='WORD':
                                    href=cell.get('href')
                                    for i in PropertyFile.href_charac:
                                        href = href.replace(i, "")
                                    href=href.encode('utf-8').strip()
                                    PropertyFile.href_list.append(href)
                                topic=cell.findNext('td').text
                                for i in PropertyFile.topic_charac:
                                    topic=topic.replace(i,"")
                                if 'WORD' in letter_number:
                                    letter_number.remove(letter_number)
                                    
                                topic=topic.encode('utf-8').strip()
                                    
                                letter_number.encode('utf-8').strip()
                                PropertyFile.letter_no.append(letter_number)
                                PropertyFile.topic_list.append(topic)
                        except:
                            self.logger.exception('fetching data has stopped...')
                            pass
                        
    def fetch_date(self):
        """Fetching the date"""
        logging.info('Started to fetch date')
        for i in PropertyFile.topic_list:
            try:
                import re
                length_data = len(i)
                datepat = re.compile(r'(\d+/\d+/\d+)')
                date = datepat.findall(i)
                length_date = len(date[0])
                length_of_topic = length_data - length_date
                n=(length_data - length_date)-2
                topic = i[0:n]
                PropertyFile.date_list.append(date[0])
                PropertyFile.topic_list_sep.append(topic)
            except:
                self.logger.exception('fetching date has stopped...')
                pass                    
                 
        logging.info('successfully fetched the data')

    def write_to_file(self):
        """writing to a csv file"""
        with open("new.csv", "wb") as f:
            csv.writer(f,delimiter=',').writerows(zip(PropertyFile.category_list,PropertyFile.year_list,PropertyFile.letter_no,PropertyFile.href_list,PropertyFile.topic_list_sep,PropertyFile.date_list))

    
    def fetch_data(self):
        """Calling the functions"""
        self.fetch_year()
        self.fetch_table()
        self.fetch_date()
        self.write_to_file()
        





        
