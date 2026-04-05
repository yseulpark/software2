from flask import Flask, Response
import mysql.connector
import json

app = Flask(__name__)

def get_connection():
    return mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='eden',
        password='edn007',
        autocommit=True
    )

@app.route('/airport/<icao>', methods=['GET'])
def get_airport(icao):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    sql = """
        SELECT ident, name, municipality
        FROM airport
        WHERE ident = %s
    """
    cursor.execute(sql, (icao,))
    result = cursor.fetchone()

    cursor.close()
    connection.close()

    if result:
        response_data = {
            "ICAO": result["ident"],
            "Name": result["name"],
            "Location": result["municipality"]
        }
    else:
        response_data = {
            "error": "Airport not found"
        }

    return Response(
        json.dumps(response_data),
        mimetype="application/json"
    )

if __name__ == '__main__':
    app.run(debug=True)