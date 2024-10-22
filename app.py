import os
from flask import Flask, jsonify, request
import pyodbc
from pprint import pprint

app = Flask(__name__)

@app.route('/restaurants', methods=['GET'])
def handle():
    print('Request received')
    print(request.args)

    name = request.args['name']
    address = request.args['address']
    style = request.args['style']
    vegetarian = request.args['vegetarian']
    doesDeliveries = request.args['doesDeliveries']
    openAt = request.args['openAt']
    print(name); name = request.args.get('name'); print(name)

    subqueries = []

    if name:
        subqueries.append(f"Name = \'{name}\'")
    if address:
        subqueries.append(f"Address = \'{address}\'")
    if style:
        subqueries.append(f"Style = \'{style}\'")
    if vegetarian:
        subqueries.append(f"Vegetarian = {int(vegetarian.lower() == 'yes')}")
    if doesDeliveries:
        subqueries.append(f"DoesDeliveries = {int(doesDeliveries.lower() == 'yes')}")
    if openAt:
        subqueries.append(f"OpeningHour <= \'{openAt}\' AND ClosingHour >= \'{openAt}\'")

    if subqueries:
        query = f"SELECT * FROM Restaurant WHERE {subqueries[0]}"

        if len(subqueries) >= 2:
            for q in subqueries[1:]:
                query += f" AND {q}"

        query += ";"

        print("Query: ", query)

        conn_str = os.environ["SQLCONNSTR_connectionString1"]
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute(query)

        response = {"restaurantRecommendation": []}

        for row in cursor.fetchall():
            response["restaurantRecommendation"].append({
                "name": row[0],
                "address": row[1],
                "style": row[2],
                "vegetarian": row[3],
                "doesDeliveries": row[4],
                "openingHour": row[5],
                "closingHour": row[6]
            })

        cursor.close()
        conn.close()

        pprint(response)

        return jsonify(response)

    else:
        return jsonify({"error": "no query provided"}), 400




if __name__ == '__main__':
    app.run()
