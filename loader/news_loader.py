import logging
import csv

from typing import Optional
from urllib.parse import urlparse

from shared.utils.client import request_get, RequestException, HTTPError, JSONDecodeError
from shared.database.models import News

from loader import config
from loader.repository import save_data_by_model_with_update


class NewsLoader:

    def __init__(
        self,
        filename: str,
        logger: Optional[logging.Logger] = None
    ) -> None:
        self._logger = logger or logging.getLogger(__name__)
        self._filename = filename

    def load(self):
        for url in self._get_url_from_csv_iter():
            news_data = self._get_news_by_url(url)
            if news_data:
                save_data_by_model_with_update(news_data, News)

    def _get_news_by_url(self, url: str):
        url = f'{url}/wp-json/wp/v2/posts'
        try:
            response = request_get(url)
        except HTTPError as e:
            self._logger.error(str(e))
            return
        except RequestException as e:
            self._logger.error(str(e))
            return
        try:
            response_data = response.json()
        except JSONDecodeError as e:
            self._logger.error(str(e))
            return
        data = []
        for item in response_data:
            data.append({
                'site_host': urlparse(url).hostname,
                'id': item['id'],
                'title': item['title']['rendered'],
                'link': item['link'],
                'content': item['content']['rendered'],
            })
        return data

    def _get_url_from_csv_iter(self) -> str:
        path = config.FILES_DIR.joinpath(self._filename)
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                yield row['_source/general/contacts/website']


if __name__ == '__main__':
    NewsLoader(filename='museums-urls.csv').load()
