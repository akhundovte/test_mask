

## Запуск проекта

- Переход в папку с файлом docker-compose.yml
```
cd deploy
```

- Создание образов
```
docker-compose build
```

- Запуск контейнеров
```
docker-compose up -d
```

- Подключение к запущенному контейнеру
```
docker exec -it test_mast_web_service_1 /bin/bash
```

- Создание таблицы в БД
```
cd /test_mast/shared/database
python db_engine.py
```

- Запуск скрипта загрузки данных
```
cd /test_mast/loader
python news_loader.py
```


**Адрес сервиса**  
http://127.0.0.1:4000/?q=
