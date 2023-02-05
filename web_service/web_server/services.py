import logging

from sqlalchemy.engine import Engine

from web_service.web_server import repository as repo
from web_service.web_server.schemas import news_schema

logger = logging.getLogger(__name__)


def get_news(search_query: str, engine: Engine):
    data = repo.get_news(search_query, engine)
    return news_schema.dump(data, many=True)


if __name__ == '__main__':
    from shared.database.db_engine import engine as _engine
    _data = get_news('Родился', _engine)
    print(_data)

