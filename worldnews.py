import worldnewsapi
from worldnewsapi.rest import ApiException
from datetime import date, timedelta
import ui

def getToken(file_path, variable):
    with open(file_path, 'r') as file:
        config = json.load(file)
        return config.get(variable)

newsapi_key = getToken('config.json', 'newsToken')
newsapi_configuration = worldnewsapi.Configuration(api_key={'apiKey': newsapi_key})
newsType = ui.news

#class NewsManager:  
def NewsManager():
        try:
            newsapiInstance = worldnewsapi.NewsApi(worldnewsapi.ApiClient(newsapi_configuration))

            response = newsapiInstance.search_news(
                text="",
                source_countries='us',
                language='en',
                earliest_publish_date=str(date.today()-timedelta(days=31)),
                latest_publish_date=str(date.today()),
                categories=newsType,
                sort="publish-time",
                sort_direction="desc",
                min_sentiment=0,
                max_sentiment=0.75,
                offset=0,
                number=5
            )

        except ApiException as e:
            print("Exception when calling news API\n" % e)

        f = open("txtReturn.txt", "x")
        for articles in news.news:
            f.write(str(articles.text))
            print("Title: " + str(article.title));
            print("Text: " + str(article.text));
        f.close()


#if __name__ == "__main__":
#    newsManager = NewsManager()
    