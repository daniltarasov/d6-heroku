# d6-homework

Из папки с джанго (c активированным вирт. окружением) выполнить: git clone https://github.com/daniltarasov/d6-homework.git
cd d6-homework
pip install -r requirements.txt
python manage.py runserver
По "/index" список книг с обложками. CSS стиль использовал стандартный бутстраповский, скачанный в Static. Картинки к книгам добавляются через админку. Доступ "admin1" - "admin1" или через create superuser.

По ссылке "/friends" список читателей, оттуда же они создаются и редактируются.