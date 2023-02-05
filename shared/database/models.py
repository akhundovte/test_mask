from sqlalchemy import (
    Column, BigInteger, String, Text
    )

from shared.database.metadata import Base
from shared.settings.config import DB_SCHEMA


class News(Base):
    __tablename__ = 'news'

    id = Column(BigInteger, nullable=False, primary_key=True)
    site_host = Column(String, nullable=False, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    link = Column(String, nullable=False)

    __table_args__ = (
        {'schema': DB_SCHEMA},
        )
