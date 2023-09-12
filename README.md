# form_database_api

Form API using FastAPI and Sqlite3

```
db file: r3spons3s.db
db table name: pandasrgood

db schema:
CREATE TABLE IF NOT EXISTS PANDASRGOOD (
   ID TEXT(500),
   NAME TEXT(500),
   REG TEXT(500),
   EMAIL TEXT(500),
   LEARNEREMAIL TEXT(500),
   YEAR TEXT(500),
   PHONE TEXT(500),
   DOMAINS TEXT(5000),
   NOTES TEXT(5000)
);

api query example:
http://127.0.0.1:9876/api?q=%7B%22name%22%3A%22John%20Deo%22%2C%22email%22%3A%22test123%40gmail.com%5C%22%20or%20drop%20table%20pandasrgood%3B--%22%2C%22emailLearner%22%3A%22asdfgh%40learner.manipal.edu.com%22%2C%22reg%22%3A%22530872345%22%2C%22year%22%3A%221%22%2C%22phone%22%3A%229876543210%22%2C%22domains%22%3A%22money%2Cbin%2Cmanagement%22%2C%22notes%22%3A%22hi%20i%20am%20xyz%5C%22%20or%20drop%20table%20pandasrgood%3B--%22%7D
```
json should contain all fields, if empty let it be ""
