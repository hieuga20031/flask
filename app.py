from flask import Flask
import db

app = Flask(__name__)

@app.route('/')
def index():
    conn = db.get_connection()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS visits (count INT)")
    cur.execute("SELECT COUNT(*) FROM visits")
    count = cur.fetchone()[0]
    if count == 0:
        cur.execute("INSERT INTO visits VALUES (1)")
    else:
        cur.execute("UPDATE visits SET count = count + 1")
    conn.commit()
    cur.execute("SELECT * FROM visits")
    count = cur.fetchone()[0]
    conn.close()
    return f"Bạn đã truy cập trang này {count} lần!"

if __name__ == '__main__':
    app.run()
