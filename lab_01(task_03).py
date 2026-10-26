tasks = {
    "coaching": "в процесі",
    "learning": "очікує",
    "presenting": "виконано",
    "shifting": "виконано",
    "working": "в процесі"
}

def print_tasks():
    print("\n--- Поточний список задач ---")
    for task, status in tasks.items():
        print("Задача: " + task + " \t Статус: " + status)
    print("-----------------------------\n")

def add_task(task_name, status):
    tasks[task_name] = status

def del_task(task_name):
    if task_name in tasks:
        del tasks[task_name]

def update_status(task_name, status):
    if task_name in tasks:
        tasks[task_name] = status

print_tasks()
# Тестування роботи
add_task("gardening", "очікує")
del_task("coaching")
update_status("working", "очікує")

# Вивід усіх задач
print("\t\tAfter a change")
print_tasks()

# Додаткове завдання: список задач зі статусом "очікує"
waiting_tasks = []
for task, status in tasks.items():
    if status == "очікує":
        waiting_tasks.append(task)


print("Задачі, які очікують виконання:")
print(waiting_tasks)