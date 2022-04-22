Для сборки образа использовать команду:

```shell
docker build -t 'sudoku-app:latest' .
```
Для запуска контейнера:
```shell
docker run -p 8080:5000 --name sud_container -d sudoku-app:latest
```
Загрузить из докер хаба:
```shell
docker pull wendur/sudokuk8s
```
