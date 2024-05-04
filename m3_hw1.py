from datetime import datetime, timedelta

def get_days_from_today(date):
    try:    
        now = datetime.today()
        now_date = now.date()
        print(f'Поточна дата: {now_date}')
        date_d = datetime.strptime(date, '%Y-%m-%d').date()
        difference = now_date-date_d
        print(f'Різниця між поточною датою та заданою датою: {difference.days}')
    except ValueError:
        print("Неправильний формат дати. Введіть дату у форматі 'РРРР-ММ-ДД'.")

date=input('Задайте дату в форматі РРРР-ММ-ДД: ')
get_days_from_today(date)


