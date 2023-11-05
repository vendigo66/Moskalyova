money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month = 0

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while True:
    delta = salary - spend #Spending per month
    if abs(delta) > abs(money_capital):
        break
    month +=1
    money_capital += delta #How much money per month I take from capital
    spend *= (increase + 1) #Changing spending
print("Количество месяцев, которое можно протянуть без долгов:", month)
