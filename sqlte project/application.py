from flask import Flask
import sqlite3

application = Flask(__name__)

conect = sqlite3.connect("app.db")
curs = conect.cursor()

curs.execute
("""cordelius
    (first_name text,
    last_name text,
    age integer,
    universiti text,
    faculty text,
    is_active text,
    when_started integer,
    when_ended integer)
""")
conect.commit

curs.execute(" INSERT INTO users VALUES ('neylon', 'dabombva', 19, 'TSU, 'he is activate', 'english', 2013 ,2000 )")
curs.execute(" INSERT INTO users VALUES ('neylon', 'dabombva', 19, 'TSU', 'he is activate', 'english',2013, 2000 )")
curs.execute(" INSERT INTO users VALUES ('neylon', 'dabombva', 19, 'TSU', 'he is  activate', 'english',2013, 2000 )")

# conect.close
# curs.close


if __name__ == "__main__":
    application.run()