from LinkTraversal import *
from Property import *
from HTMLDataScraper import *
from DataFileMerger import *

def main():
    url=raw_input('enter the url :')
    linktraversal=LinkTraversal(url)
    linktraversal.traverse_main()
    htmldatascraper=HTMLDataScraper()
    htmldatascraper.fetch_data()
    datafilemerger=DataFileMerger()
    datafilemerger.call()
        


main()
