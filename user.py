from bs4 import BeautifulSoup
from urllib import urlopen
import lxml.html
import urllib
from Property import *
import logging.config


def get_choice1(soup):
    '''This function gets the entire links'''
    for i,j in PropertyFile.dict1.iteritems():
        a=PropertyFile.dict1[i]
        for i in soup.find_all('a'):
            if i.text==a:
                PropertyFile.all_range.append(PropertyFile.url_path+i.get('href'))

def get_choice2(soup):
    '''this function gets the links for a particular range of year'''
    year_range=input('\n1.Range1:1998 - 1996\n2.2004 - 1999\n3.2010 - 2005\n4.2015 - 2011\nEnter the range you want:')
    for i,j in PropertyFile.dict1.iteritems():
        if i==year_range:
            a=PropertyFile.dict1[i]
            for i in soup.find_all('a'):
                if i.text==a:
                    PropertyFile.all_range.append(PropertyFile.url_path+i.get('href'))
                    break


def get_choice3(soup):
    '''this function gets the links for a particular year'''
    particular_year=input('\nEnter any year between 1996 to 2012 for which you want to extract data:')
    PropertyFile.particular_year=particular_year
    for i,j in PropertyFile.dict1.iteritems():
        a=PropertyFile.dict1[i]
        split=PropertyFile.dict1[i].split(' - ')
        if particular_year<=int(split[0]) and particular_year>=int(split[1]):
            for i in soup.find_all('a'):
                if i.text==a:
                    PropertyFile.all_range.append(PropertyFile.url_path+i.get('href'))
                        


def get_choice12():
    '''this function get the links of the months  for range of years'''
    for i in PropertyFile.all_range:
        r1=urlopen(i)
        soup1=BeautifulSoup(r1,"html.parser")
        for i in soup1.findAll('h3'):
            if i.text in PropertyFile.year:
                a=i.findNext('p').find_all('a')
                for l in a:
                    if PropertyFile.url_path in l.get('href'):
                        PropertyFile.url_data.append(l.get('href'))
                    else:
                        PropertyFile.url_data.append(PropertyFile.url_path+l.get('href'))
                        #print l.get('href')
                            
def get_choice13():
    '''this function get the links of the months of particular year '''
    for i in PropertyFile.all_range:
        r1=urlopen(i)
        soup1=BeautifulSoup(r1,"html.parser")
        for i in soup1.findAll('h3'):
            if i.text==str(PropertyFile.particular_year):
                if i.text in PropertyFile.year:
                    a=i.findNext('p').find_all('a')
                    for l in a:
                        if PropertyFile.url_path in l.get('href'):
                            PropertyFile.url_data.append(l.get('href'))

                        else:
                            link=PropertyFile.url_path+l.get('href')
                            PropertyFile.url_data.append(link)
                            #print l.get('href')

  
           
