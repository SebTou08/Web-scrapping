from flask import Flask, request, jsonify
from flask_limiter import Limiter
from services.RiskService import risk_service

app = Flask(__name__)
limiter = Limiter(
    app,
    default_limits=["20 per minute"]
)


@app.route('/sanctions', methods=['POST'])
@limiter.limit("20/minute")
def get_sanctions():
    try:
        data = request.json
        results = risk_service(data)
        return jsonify(results), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
