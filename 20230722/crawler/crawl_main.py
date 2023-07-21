from datetime import datetime
from loguru import logger
import numpy as np
import pandas as pd
import time 
from channel.twitter import Twitter

if __name__ == "__main__" :
    keyword = 'iphone'
    startdate = '2023-01-01'
    enddate = '2023-07-21'
    companyCode = 99999    
    twitter = Twitter()
    twitter.Twitter_Crawl(keyword, startdate, enddate, companyCode)