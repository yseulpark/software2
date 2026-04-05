from flask import Flask, Response
import json

app = Flask(__name__)


def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True


@app.route('/prime_number/<int:number>', methods=['GET'])
def prime_number(number):
    result = {
        "Number": number,
        "isPrime": is_prime(number)
    }

    return Response(
        json.dumps(result),
        mimetype="application/json"
    )

if __name__ == '__main__':
    app.run(debug=True)