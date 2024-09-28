questions = ["Сколько ты получаешь в час: ", "Сколько часов в этом месяце: ", "Сколько продаж в этом месяце: ",
             "Чаевые: "]
answers = []
sales_percent = 0.02

user_name = input("Представься: ")

print(f"Привет, {user_name}. Сейчас мы посчитаем твою зарплату в этом месяце")

for i in questions:
    while True:
        user_input = input(i)
        if user_input.isdigit():
            answers.append(int(user_input))
            break
        else:
            print("Неправильные значения")
if int(answers[2]) >= 450000:
    sales_percent = 0.03
total = round(answers[0] * answers[1] + answers[2] * sales_percent + answers[3])
total_without_tea = round(answers[0] * answers[1] + answers[2] * sales_percent)
print(
    f"Твоя зарплата в этом месяце без учета общего процента и без вычетов: {total} рублей, без чаевых: {total_without_tea}")
