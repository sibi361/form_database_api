"""
run with
uvicorn api:app --no-server-header --port 9876
"""

import fastapi
import json
import sqlite3
from utilities import *

DBNAME = "r3spons3s.db"
TABLENAME = "PANDASRGOOD"
BACKUPDIR = "./db_backups/"

cmd_create = """
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
"""

cmd_insert = "INSERT INTO {} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)".format(
    TABLENAME)


backupDb(DBNAME, BACKUPDIR)

# https://stackoverflow.com/a/48234567
db = sqlite3.connect(DBNAME, check_same_thread=False)

cursor = db.cursor()
cursor.execute(cmd_create)

app = fastapi.FastAPI()


@app.get("/")
def test():
    return ""


@app.get("/api")
def test(q: str):
    if not q:
        return {"status": "invalid input"}
    data = q.strip()
    try:
        data = json.loads(data.strip())
    except json.JSONDecodeError as e:
        with open("errors.txt", "a") as f:
            f.write(q.replace("\n", "") + "\n")
        print("# ERROR JSONDecodeError: {}\n for data: {}".format(e, data))

    for i in data:
        try:
            cursor.execute(cmd_insert,
                           (genUniqueId(),
                            data["name"],
                            data["email"],
                            data["emailLearner"],
                            data["reg"],
                            data["year"],
                            data["phone"],
                            data["domains"],
                            data["notes"])
                           )
        except Exception as e:
            print("# ERROR data doesn't have all columns: {}".format(e))
            with open("errors.txt", "a") as f:
                f.write(q.replace("\n", "") + "\n")
        else:
            db.commit()
        break

    return {"status": "ok"}
