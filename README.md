# proxy_server_dou

 ## Як запустити:
 * клонуйте директорію на вашу машину
```bash
git clone https://github.com/VolodymyrVdovyn/proxy_server_dou.git
```
 
 * встановіть залежності
```bash
pip install -r requirements.txt 
```
 
 * запустіть тести
```bash
python test_proxy_server.py && python test_replacer.py
```

 * запустіть скрипт
```bash
python proxy_server.py   
```

 * перевірте роботу в браузері
```
http://127.0.0.1:8888
```
 
Реалізувати простий http-проксі сервер, який треба запустити локально, що буде відтворювати
сторінки dou.ua . Проксі повинен модифікувати текст на сторінках таким чином, щоб після кожного
слова, яке складається з 6 літер, повинен стояти знак «TM».

Приклад:
Текст на сторінці виглядає так як вказано нижче:
https://dou.ua/forums/topic/24951/

Всем привет. Случилась очень неприятная ситуация, и данной темой хотел предупредить
остальных об очередных новых идеях этого оператора о том как нагреть.

Через ваш проксі повинен виглядати так:
http://127.0.0.1:8888/forums/topic/24951/

Всем привет™. Случилась очень неприятная ситуация, и данной™ темой хотел предупредить
остальных об очередных новых идеях этого оператора о том как нагреть.