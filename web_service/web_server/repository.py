import sqlalchemy as sa

from sqlalchemy.engine import Engine

from shared.database.models import News


def get_news(search_query: str, engine: Engine):
    select_q = sa.select((
        News.link, News.content, News.title
        ))\
        .where(sa.or_(
            News.title.like('%' + search_query + '%'),
            News.content.like('%' + search_query + '%'),
            ))\
        .limit(10)
    with engine.connect() as connection:
        rows = connection.execute(select_q)
        return rows.fetchall()


if __name__ == '__main__':
    from shared.database.db_engine import engine as _engine
    data = get_news('Родился', _engine)
    print(data)
