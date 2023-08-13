from GoogleTrendAPI import GoogleTrend
from WordSearchVolume import WordVolume

if __name__ == '__main__':
    googletrendapi = GoogleTrend()
    wordvolume = WordVolume()
    word_df = googletrendapi.Search_TrendWord()
    words = list(word_df[0].values)
    for word in words:
        wordvolume.Search_WordVolume(word)