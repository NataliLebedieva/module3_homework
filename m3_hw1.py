from datetime import datetime, timedelta

def get_days_from_today(date):
    
    now = datetime.now()
    now_date = now.date()

    print(f'Поточна дата: {now_date}')

    difference = now_date-date_d
    print(f'Різниця між поточною датою та заданою датою: {difference.days}')


date=input('Задайте дату в форматі РРРР-ММ-ДД: ')
date_d = datetime.strptime(date, '%Y-%m-%d').date()
get_days_from_today(date)


# date_d = datetime.strptime('date', '%Y.%m.%d')