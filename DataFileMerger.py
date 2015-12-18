import csv
import glob
import logging
#import sys
#import mylib
import logging
import datetime
import logging.config
from Property import *

class DataFileMerger:
    '''this class is used for merging all csv into one file'''
    total_csv = []
    new_csv=0
    
    #constructor
    def __init__(self):
        self.new_csv = open('final.csv','wb',0)
        self.csv_f='NULL'


    def categories_find(self,topic_name):
        """This function writes the csv file according to the category"""
        #create logger
        logger = logging.getLogger("category")
        

        logger.info('Started Grouping Data')
        logger.info('Finished Grouping Data')
        
        #logging.info(format)

        try: 
            for row in self.csv_f:
                if(row[0] == topic_name.strip()):
                
                    air=csv.writer(self.new_csv, delimiter=',')
                    air.writerow(row)
        except:
            
        
            print "Sorry for the inconvience"

            #Exception will be stored in find_files.log
            logger.exception("Unexpected Error:")
                    
                    
            
    def find_files(self):
        """This function displays all the csv files """

        
        #create logger
        logger = logging.getLogger("DataFileMerger")

        #create console handler and set level to DEBUG
        logging.basicConfig(filename='find_files.log',level=logging.DEBUG,
                format='%(asctime)s.%(msecs)d %(levelname)s %(module)s - %(funcName)s: %(lineno)s %(message)s')
        
        logging.info('Started collecting all CSV Files')
        logging.info('Finished collecting all CSV Files')
        
       
                   
        try:
            for files in glob.glob("*.csv"):
                DataFileMerger.total_csv.append(files)
                
            return DataFileMerger.total_csv
        except:
            print "Sorry for the inconvience"

            #Exception will be stored in find_files.log 
            logger.exception("Unexpected file Error:")


   

    def call(self):
        '''this function retrieves all categories available'''
        DataFileMerger.total_csv = self.find_files()
        
        for i in range(len(PropertyFile.category)):
            for list_of_files in DataFileMerger.total_csv:
                f=open(list_of_files,'r')
                self.csv_f = csv.reader(f)
                self.categories_find(PropertyFile.category[i])
            if i==0:
                 DataFileMerger.total_csv.remove('final.csv')
        f.close()
    
