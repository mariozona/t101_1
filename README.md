# LR_1
* Дабы собрать Docker образ в текущей директории нужно использовать команду

```bash
  docker build -t LR1 .
```

---> cоздается образ с именем LR1; 
* Дабы запустить Docker-контейнер по уже существующему образу используем следующую команду:

```bash
  docker run -it --rm LR1
```

**--rm** удаляет контейнер после завершения работы скрипта

## algorythmdescription

1. Генерируются факты и правила.

2. Правила приводятся к более удобному виду.
> Правила имеют вид:

 **[ { if:{'operand : [numbers]'},then: number}, ...]**. 

> Факты сортируются в **3** отдельных массива по логическому операнду
  
 **[ [ [if], then ], ...]**

3. Приводим факты к удобоваримому виду.
> Факты кайфут в одномерном массиве, а так как мы хотим избежать прогона по всему массиву 
  и повтора фактов, помещаем их в словарь
 
  **{ number:True }**,

  если number -, то метод **get()** возвращает 
  None

4. Запускается скрипт для проверки фактов.
> При проверке правила **OR** ищем

 
  **хотя бы одно совпадение** 

  условия и факт ---> добавляем в базу знаний. 

> При проверке правила **AND** ищем 

  **хотя бы одно несовпадение** 

  условия и факта ---> не добавляем в базу знаний.
 
> При проверке праила **NOT** ищем

  **хотя бы одно совпадение**

  условия и факта ---> не добавляем в базу знаний. 

5. Функцией

   **time()**

   замеряем время работы абракадабры, добавляющей правила.
