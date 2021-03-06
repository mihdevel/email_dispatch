# Email dispatch
Приложение для email рассылок по группам и управления ими с помощью интерфейса администратора или через REST API

Состоит из 2 приложений django:
* `email_dispatch`
* `rest_api`

## Приложение `email_dispatch` позволяет:
* Хранить в себе почтовые ящики для рассылки разделенные на группы;
* Хранить расписание для рассылки на указанные группы почтовых ящиков;
* Хранить отчеты о отправке писем;
* Просмотривать и редактировать в административной части проекта: почтовые ящики, группы, отчеты о рассылки, шаблоны, и расписание;
* Отписаться от рассылки с помощью перехода по url.

## Приложение `rest_api` позволяет:
* Добавлять или удалять: группы, почтовые ящики и расписание рассылки через REST API используя JSON.

## Дополнительные информация
* Отписка от рассылки производится с помощью перехода по url с параметрами GET запроса. При этом читывается, что только хозяин или пользователь почтового ящика может его отписать с сервера рассылки.
* После отправки писем формируется отчет о успешности или неудачи с датой и текстом письма.
* REST API реализовано с помощью сторонней библиотеки Django REST framework.
* Механизмы REST API покрыты тестами для проверки работоспособности.

## Точки входа для REST API
* /emails
* /groups
* /dispatchs

## Возможное улучшение/развитие программы
* Производить авторизацию для пользованием API с помощью токенов
* Покрытие всего REST API тестами