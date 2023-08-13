import pandas as pd
from pytrends.request import TrendReq

class GoogleTrend():
    def __init__(self) -> None:
        self.word_df = pd.DataFrame()

    def Search_TrendWord(self):
        try:
            pytrends = TrendReq(hl='ko-KR', tz=540) # hl(Host Language) : 구글 트랜드의 언어 설정, tz(TimeZone offset) : UTCF부터의 시차를 분 단위로 표히
            self.word_df = pytrends.trending_searches(pn='south_korea') # pn : 국가설정
        except Exception as e:
            print(e)
            
        return self.word_df
