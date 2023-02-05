from shared.settings import config
from web_service.web_server.views import app

if __name__ == '__main__':
    app.run(port=5000, debug=config.DEBUG)
