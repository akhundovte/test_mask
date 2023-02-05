
from flask import jsonify, request

from web_service import config
from web_service.web_server.services import get_news
from web_service.web_server.app import create_app, db

app = create_app()


@app.errorhandler(400)
@app.errorhandler(404)
@app.errorhandler(405)
@app.errorhandler(500)
def http_error_handler(error):
    return jsonify(error=str(error)), error.code


@app.route('/', methods=['get'])
def search_news():
    q = request.args.get('q')
    response_data = get_news(q, db.engine)
    return jsonify(response_data)
