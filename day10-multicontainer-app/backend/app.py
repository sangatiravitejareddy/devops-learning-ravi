from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

@app.route('/api/data')
def get_data():
    conn = psycopg2.connect(
        host='db',
        database='testdb',
        user='postgres',
        password='password'
    )
    cur = conn.cursor()
    cur.execute('SELECT NOW()')
    result = cur.fetchone()
    cur.close()
    conn.close()
    return jsonify({'time': result[0].isoformat()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)




