## Курсовая работа № 4 в курсе Python-разработчик от SkyPro "Парсер вакансий на HH.RU / SUPERJOB.RU"
Программа получает информацию о вакансиях с разных платформ в России, сохраняет ее в файл и позволяет удобно работать с ней (добавлять, фильтровать, удалять).
### Шаги реализации
- Создан абстрактный класс для работы с API сайтов с вакансиями.
- Реализованы классы, наследующиеся от абстрактного класса, для работы с конкретными платформами, классы умеют подключаться к API и получать вакансии.
- Создан класс для работы с вакансиями. Класс поддерживает методы сравнения вакансий между собой по зарплате и валидировует данные, которыми инициализируются его атрибуты.
- Определен абстрактный класс, который обязывает реализовать методы для добавления вакансий в файл, получения данных из файла по указанным критериям и удаления информации о вакансиях.
- Создан класс для сохранения информации о вакансиях в JSON-файл.
- Создана функция для взаимодействия с пользователем через консоль.
- Все классы и функции объединены в программу.
