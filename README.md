To run microservices:
1. Clone the repository: https://github.com/patsiomkina/microservices.git
2. From root folder launch the terminal and run the command: docker-compose build
3. From the same folder run the command: docker-compose up

Now, when all 3 microservices are up and running, you can use Postman to work with them.

REAPER microservice (runs on port 5002):
Reads the news rss feed, parses the news.
You need to specify rss news feed address (e.g. https://news.yahoo.com/rss/, http://news.rambler.ru/rss/world/, etc.).
Possesses the following endpoints:
    * '/' - to check if the API is available
      E.g. http://127.0.0.1:5002/ - the welcome page is displayed.
    * '/reaper/api/sites' (GET) - to retrieve and process the news feed of a given website
      E.g. http://127.0.0.1:5002/reaper/api/sites?url=https://news.yahoo.com/rss/ - displays news from the specified site in a structured form

KEEPER microservice (runs on port 5003):
Stores news in a local storage (DB), retrieves news from DB for the selected date and (or) from selected url.
Possesses the following endpoints:
    * '/' - to check if the API is available
      E.g. http://127.0.0.1:5003/ - the welcome page is displayed.
    * '/keeper/api/db_news' (GET) - to retrieve all news from DB (for all urls and dates)
      E.g. http://127.0.0.1:5003/keeper/api/db_news - displays all news from DB in a structured form.
      You can specify the date and/or url for which the news from the database should be selected:
      !!!Parameter 'date' should be entered in the format: %d/%m/%Y
      E.g. http://127.0.0.1:5003/keeper/api/db_news?date=23/10/2021
           http://127.0.0.1:5003/keeper/api/db_news?url=https://news.yahoo.com/rss/
           http://127.0.0.1:5003/keeper/api/db_news?date=23/10/2021&url=https://news.yahoo.com/rss/
    * '/keeper/api/db_news/add_news' (POST) - saves news in the database (need to pass the news list in json format);

MASTER microservice (runs on port 5001):
Organizes collaborative work of Raper and Keeper: forces Reaper to read and parse the news, gets data from Keeper.
Possesses the following endpoints:
    * '/' - to check if the API is available
      E.g. http://127.0.0.1:5001/ - the welcome page is displayed.
    *'/master/api/url' (POST) - to retrieve news feed data using Reaper and upload it to the DB using Keeper
      E.g. http://127.0.0.1:5001/master/api/url?url=http://news.rambler.ru/rss/world/ - retrieves news and uploads 
           it to the DB, a message about successful data recording to the DB is displayed;
    * '/master/api/db' (GET) - to retrieve data from database using Keeper;
      E.g. http://127.0.0.1:5001/master/api/db - displays all news from DB in a structured form.
      You can specify the date and/or url for which the news from the database should be selected:
      !!!Parameter 'date' should be entered in the format: %d/%m/%Y
      E.g. http://127.0.0.1:5001/master/api/db?date=23/10/2021
           http://127.0.0.1:5001/master/api/db?url=https://news.yahoo.com/rss/
           http://127.0.0.1:5001/master/api/db?date=23/10/2021&url=http://news.rambler.ru/rss/world/

!!! Please note that when you run service for the first time, a POST request must be made first, so that the database 
    is initialized and contains the news to organize the subsequent selection!!!