from bs4 import BeautifulSoup
from urllib import urlopen
import lxml.html
import urllib
from Property import *
import logging.config
from user import *
class LinkTraversal:
    '''This class is to obtain all the links '''
    #constructor
    def __init__(self,url):
        self.url=url
        
    def traverse_main(self):
        '''this function gets the user's choice'''
	#create logger
        logger = logging.getLogger("handler1")

        #create console handler and set level to DEBUG
        logging.basicConfig(filename='handler1.log',level=logging.DEBUG,
                format='%(asctime)s.%(msecs)d %(levelname)s %(module)s - %(funcName)s: %(lineno)s %(message)s')
        logging.info('Started traversal')
        
        #main url
        r=urlopen(self.url)
        soup=BeautifulSoup(r,"html.parser")
        print '1.Retrieve the data for all the years\n2.Retrieve the data for a particular range of year\n3.Retrieve for a particular year'
        PropertyFile.choice=input("\nEnter the choice you want:")
        if PropertyFile.choice==1:
            get_choice1(soup)
        if PropertyFile.choice==2:
            get_choice2(soup)
        if PropertyFile.choice==3:
            get_choice3(soup)
           
        logging.info('finished traversal')
        self.traversing_next()
           
    def traversing_next(self):
        '''This function retrieves all the month links'''
        if PropertyFile.choice!=3:
           get_choice12()
        else:
            get_choice13()

    
                
                        

            
        
