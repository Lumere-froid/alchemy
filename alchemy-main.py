import tkinter as tk


# 1. База трав
INGREDIENTS_HAR = {
    # Редкость 1 (Обычные, сбор 3 сек, мудрость 1)
    "Сорная трава": {
        "rarity": 1, 
        "gather_time": 3, 
        "required_wisdom": 1, 
        "mana_cost": 0, 
        "description": "Обычная зелёная трава, которую ты можешь найти на любой поляне. Зачем ты собрал её?",
        "effect": "Портит вкус любого напитка. Зато можно использовать для декора."
        },
    "Одуванчик": {
        "rarity": 1, 
        "gather_time": 3, 
        "required_wisdom": 1, 
        "mana_cost": 0, 
        "description": "Обычные цветы, распускающиеся золотым ковром по весне. Может быть полезнным, но вкус у него горький.",
        "effect": "Востанавливает силы, можно использовать как в чае, так и в лёгких противоядиях. Так же неплохо использовать цветы в качестве украшений."
        },
    # Редкость 2 (Необычные, сбор 10 сек, мудрость 2)
    "Мята": {
        "rarity": 2, 
        "gather_time": 10, 
        "required_wisdom": 2, 
        "mana_cost": 0, 
        "description": "Известное растение, с ярким вкусом. От мяты остаются освежающие воспоминания.",
        "effect": "Освежает и успокаивает, очищает мысли и снимает боль. Восстанавливает немного маны."
        },
    "Малина": {
        "rarity": 2, 
        "gather_time": 10, 
        "required_wisdom": 2, 
        "mana_cost": 0, 
        "description": "Вкусные и полезные ягоды. Листья можно заваривать в чай.",
        "effect": "Согревает тело и душу, может быть основой для слабых лечащих зелий."
        },
    # Редкость 3 (Редкие, сбор 30 сек, мудрость 3)
    "Дремода": {
        "rarity": 3, 
        "gather_time": 30, 
        "required_wisdom": 3, 
        "mana_cost": 0, 
        "description": "Ароматные яркие цветы, насыщенного синего цвета. Растут в глубине тёмных лесов.",
        "effect": "От аромата цветов дремоды тянет в сон, при использовании в зельях этот эффект может усилится."
        },
    "Лунный мох": {
        "rarity": 3, 
        "gather_time": 30, 
        "required_wisdom": 3, 
        "mana_cost": 0, 
        "description": "Серебристый мох, растущий на лунных полянах. Слабо фосфоресцирует в темноте.",
        "effect": "Хорош для выведения ядов и востанновления после них. Заставляет напитки легко светится."
        },
    # Редкость 4 (Магические низшего уровня, сбор 60 сек, мудрость 5, мана 10)
    "Саломандрова трава": {
        "rarity": 4, 
        "gather_time": 60, 
        "required_wisdom": 5, 
        "mana_cost": 10, 
        "description": "Алая трава, растущая у воды. Практически не горит.",
        "effect": "Даёт ярко красный цвет напитку, может дать огнестойкость."
        },
    "Гортык": {
        "rarity": 4, 
        "gather_time": 60, 
        "required_wisdom": 5, 
        "mana_cost": 10, 
        "description": "Невысокий кустарник с красивыми белыми цветами и дурманящим ароматом. Ловит и 'съедает' насекомых своими синими ягодами.",
        "effect": "Дурманит рассудок. Можно использовать как основу приворотных зелий или для восстановления рассудка."
        },
    # Редкость 5 (Магические среднего уровня, сбор 180 сек, мудрость 7, мана 25)
    "Олентины глазки": {
        "rarity": 5, 
        "gather_time": 180, 
        "required_wisdom": 7, 
        "mana_cost": 25, 
        "description": "Маленькие жёлтые цветочки с чёрными сердцевинками, обрамленными красным пояском. Сильно привлекают внимание.",
        "effect": "Могут вызвать галлюцинации. Ядовитое растение, но при правильном приготовление становится безвредным источником яркого вкуса."
        },
    "Огненая трава": {
        "rarity": 5, 
        "gather_time": 180, 
        "required_wisdom": 7, 
        "mana_cost": 25, 
        "description": "Неприметная серая травка с резными листочками. Легко воспламеняется при контакте с водой.",
        "effect": "ОСТОРОЖНЕЕ ПРИ ПРИГОТОВЛЕНИЕ! НЕЛЬЗЯ СМЕШИВАТЬ С ЧИСТОЙ ВОДОЙ. Легко воспламеняется, передаёт этот эффект напиткам, в которых используется. Также может давать некоторые огненные способности."
        },
    # Редкость 6 (Магические высшего уровня, сбор 300 сек, мудрость 9, мана 40)
    "Золотой дурман": {
        "rarity": 6, 
        "gather_time": 300, 
        "required_wisdom": 9, 
        "mana_cost": 40,
        "description": "Роскошные золотые цветы на лианах. Полуразумное растение, любящее вводить в заблуждение и манипулировать человеческим сознанием.",
        "effect": "При использовании в напитках, заставляет выглядеть их дороже. Может создавать иллюзии."
        },
    "Ледяной цветок": {
        "rarity": 6, 
        "gather_time": 300, 
        "required_wisdom": 9, 
        "mana_cost": 40, 
        "description": "Цветок на тонкой белоснежной ножке, выглядещий как бриллиант. Превращает в лёд любую жидкость, входящую в состав того, что к нему прикоснулось.",
        "effect": "Практически невозможно превратить в напиток, даёт ледяные эффекты."
        },
}


# 2. Игрок
player_stats = {
    "level": 1,
    "exp": 0,
    "wisdom": 1,
    "mana": 10,       
    "max_mana": 75,
    "inventory": {},
    "herb_knowledge": {},         
    "discovered_recipes": []   
}

# 3. интерфейс

root = tk.Tk()
root.title("Лаборатория Алхимика: Сбор и Крафт")
root.geometry("650x500")
root.configure(bg="#2c2421")

# --- ПАНЕЛЬ СТАТИСТИКИ ПЕРСОНАЖА ---
stats_frame = tk.LabelFrame(
    root, 
    text=" Профиль Алхимика ", 
    bg="#2c2421", 
    fg="#d4af37",          
    font=("Courier", 12, "bold")
)
stats_frame.pack(padx=15, pady=15, fill="x")

stats_label = tk.Label(
    stats_frame,
    text=f"Уровень: {player_stats['level']}   |   Мудрость: {player_stats['wisdom']}",
    bg="#2c2421",
    fg="#e6dfd3",          
    font=("Courier", 11)
)
stats_label.pack(anchor="w", padx=10, pady=5)

mana_label = tk.Label(
    stats_frame,
    text=f"Мана: {player_stats['mana']} / {player_stats['max_mana']}",
    bg="#2c2421",
    fg="#4a90e2",          
    font=("Courier", 11, "bold")
)
mana_label.pack(anchor="w", padx=10, pady=5)


# --- ГЛАВНАЯ РАБОЧАЯ ЗОНА (Разделение на Лево и Право) ---
#общий контейнер для нижней части игры
main_area = tk.Frame(root, bg="#2c2421")
main_area.pack(fill="both", expand=True, padx=15, pady=5)

# ЛЕВАЯ ЧАСТЬ: Зачарованный лес
forest_frame = tk.LabelFrame(
    main_area, text="Зачарованный Лес ", bg="#2c2421", fg="#a89f91", font=("Courier", 11, "bold")
)
forest_frame.pack(side="left", fill="both", expand=True, padx=5, pady=5)

forest_status = tk.Label(
    forest_frame,
    text="Вы стоите на опушке Зачарованного леса.\nВокруг тишина...",
    bg="#2c2421",
    fg="#a89f91",          
    font=("Courier", 10, "italic"),
    wraplength=280
)
forest_status.pack(pady=40)

# Функция сбора трав


is_gathering = False

def go_to_forest(event=None):
    """Выбирает будущую добычу из словаря, берет её время сбора и запускает таймер"""
    global is_gathering
    import random
    
    if event is not None:
        if event.char not in ['f', 'F', 'а', 'А']:
            return
            
    if is_gathering:
        return
        
    is_gathering = True
    gather_button.config(state="disabled")
    
    # 1. Заранее выбираем траву (пока 1-й редкости)
    starting_herbs = [name for name, info in INGREDIENTS_HAR.items() if info["rarity"] == 1]
    target_herb = random.choice(starting_herbs)
    
    # 2. БЕРЁМ ВРЕМЯ ПРЯМО ИЗ СЛОВАРЯ!
    gather_duration = INGREDIENTS_HAR[target_herb]["gather_time"]
    
    # 3. Передаем в таймер и время, и имя выбранной травы
    countdown_gathering(gather_duration, target_herb)

def countdown_gathering(seconds_left, target_herb):
    """Тикает каждую секунду и помнит, какую траву мы ищем"""
    if seconds_left > 0:
        forest_status.config(
            text=f"Вы пробираетесь сквозь чащу...\n\n⏳ Осталось времени: {seconds_left} сек.",
            fg="#d4af37"
        )
        # Передаем target_herb дальше по цепочке каждую секунду
        root.after(1000, countdown_gathering, seconds_left - 1, target_herb)
    else:
        # Передаем найденную траву в финальную функцию
        finish_gathering(target_herb)

def finish_gathering(true_name):
    """Кладет заранее выбранную траву в сумку"""
    global is_gathering
    
    rarity = INGREDIENTS_HAR[true_name]["rarity"]
    display_name = f"Неизвестное растение (Редк. {rarity})"
    
    if display_name not in player_stats["inventory"]:
        player_stats["inventory"][display_name] = {
            "quantity": 1,
            "true_names": [true_name],
            "rarity": rarity
        }
    else:
        player_stats["inventory"][display_name]["quantity"] += 1
        player_stats["inventory"][display_name]["true_names"].append(true_name)
    
    update_inventory_display()
    
    forest_status.config(
        text=f"✨ Поиск завершён!\n\nВ сумку добавлено:\n{display_name}",
        fg="#e6dfd3"
    )
    
    gather_button.config(state="normal")
    is_gathering = False




# --- ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ИНТЕРФЕЙСА ---

def update_inventory_display():
    """Функция, которая считывает инвентарь игрока и обновляет текст в Сумке"""
    if not player_stats["inventory"]:
        inventory_label.config(text="Ваша сумка пока пуста...")
        return
    
    lines = []
    # Теперь мы перебираем инвентарь, где лежат наши скрытые объекты
    for display_name, item_data in player_stats["inventory"].items():
        quantity = item_data["quantity"]
        lines.append(f"• {display_name}: {quantity} шт.")
    
    final_text = "\n".join(lines)
    inventory_label.config(text=final_text)



#создание кнопок
gather_button = tk.Button(
    forest_frame,
    text="Отправиться на поиски",
    bg="#3e322d",          
    fg="#d4af37",          
    activebackground="#54433c", 
    activeforeground="#ffffff",
    font=("Courier", 10, "bold"),
    command=go_to_forest   
)
gather_button.pack(pady=10)

# Теперь окно слушает вообще любое нажатие клавиши
root.bind("<Key>", go_to_forest)



# ПРАВАЯ ЧАСТЬ: Сумка Алхимика (Инвентарь)
inventory_frame = tk.LabelFrame(
    main_area, text="Сумка Алхимика ", bg="#2c2421", fg="#d4af37", font=("Courier", 11, "bold")
)
inventory_frame.pack(side="right", fill="both", expand=True, padx=5, pady=5)

# Надпись, в которой будет выводиться список наших предметов
inventory_label = tk.Label(
    inventory_frame,
    text="Ваша сумка пока пуста...",
    bg="#2c2421",
    fg="#e6dfd3",
    font=("Courier", 10),
    justify="left", # Выравнивание текста по левому краю
    anchor="nw"     # Прижимаем текст к верхнему левому углу
)
inventory_label.pack(fill="both", expand=True, padx=10, pady=10)



# Запускаем постоянный цикл окна, чтобы оно не закрывалось
root.mainloop()
