import pandas as pd
from datetime import datetime, timedelta
# connect
from pytrends.request import TrendReq
pytrends = TrendReq(hl='ko', tz=540) # hl=host language, tz=time zone


class WordVolume():
    def __init__(self) -> None:
        self.word_df = pd.DataFrame()

    def Search_WordVolume(self, word):
        try:
            startdate = datetime.strftime(datetime.now()-timedelta(days=7), '%Y-%m-%d')
            enddate   = datetime.strftime(datetime.now(), '%Y-%m-%d')
            pytrends.build_payload(
                                    word,
                                    cat=0, 
                                    timeframe=f'{startdate} {enddate}', 
                                    geo='KR', gprop=''
                                )
            data = pytrends.interest_over_time()
        except Exception as e:
            print(e)

        return 0
            
