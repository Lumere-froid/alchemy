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


# 2. игрок
player_stats = {
    "level": 1,
    "exp": 0,               # Опыт для повышения уровня и мудрости
    "wisdom": 1,
    "mana": 10,             
    "max_mana": 50,
    "inventory": {},          
    "herb_knowledge": {},   # Уровень изучения: {"Одуванчик": 1} (максимум 3)
    "discovered_recipes": []   
}

# Список для хранения ключей инвентаря в том порядке, в каком они показаны в Listbox
inventory_keys_order = []

# 3. интерфейс
root = tk.Tk()
root.title("Лаборатория Алхимика: Сбор и Крафт")
root.geometry("780x520")
root.configure(bg="#2c2421")

# панель персонажа
stats_frame = tk.LabelFrame(
    root, text=" Профиль Алхимика ", bg="#2c2421", fg="#d4af37", font=("Courier", 12, "bold")
)
stats_frame.pack(padx=15, pady=15, fill="x")

stats_label = tk.Label(
    stats_frame,
    text=f"Уровень: {player_stats['level']} (Опыт: {player_stats['exp']}/3)   |   Мудрость: {player_stats['wisdom']}",
    bg="#2c2421", fg="#e6dfd3", font=("Courier", 11)
)
stats_label.pack(anchor="w", padx=10, pady=5)

mana_label = tk.Label(
    stats_frame,
    text=f"Мана: {player_stats['mana']} / {player_stats['max_mana']}",
    bg="#2c2421", fg="#4a90e2", font=("Courier", 11, "bold")
)
mana_label.pack(anchor="w", padx=10, pady=5)

# раб. зона
main_area = tk.Frame(root, bg="#2c2421")
main_area.pack(fill="both", expand=True, padx=15, pady=5)

# лево
forest_frame = tk.LabelFrame(
    main_area, text="Зачарованный Лес ", bg="#2c2421", fg="#a89f91", font=("Courier", 11, "bold")
)
forest_frame.pack(side="left", fill="both", expand=True, padx=5, pady=5)

forest_status = tk.Label(
    forest_frame,
    text="Вы стоите на опушке Зачарованного леса.\nВокруг тишина...",
    bg="#2c2421", fg="#a89f91", font=("Courier", 10, "italic"), wraplength=280
)
forest_status.pack(pady=40, expand=True)

# право
inventory_frame = tk.LabelFrame(
    main_area, text="Сумка Алхимика ", bg="#2c2421", fg="#d4af37", font=("Courier", 11, "bold")
)
inventory_frame.pack(side="right", fill="both", expand=True, padx=5, pady=5)



# Список предметов в сумке, по которым можно кликать мышкой
inventory_listbox = tk.Listbox(
    inventory_frame,
    bg="#3e322d",
    fg="#e6dfd3",
    selectbackground="#d4af37", # Золотой фон при выделении строчки
    selectforeground="#2c2421", # Тёмный текст на золотом фоне
    font=("Courier", 10),
    borderwidth=0,
    highlightthickness=0
)
inventory_listbox.pack(fill="both", expand=True, padx=10, pady=10)


# обновление интерфейса

def update_stats_display():
    """Обновляет верхнюю панель с уровнем, опытом, мудростью и маной"""
    next_lvl_exp = player_stats["level"] * 3
    stats_label.config(
        text=f"Уровень: {player_stats['level']} (Опыт: {player_stats['exp']}/{next_lvl_exp})   |   Мудрость: {player_stats['wisdom']}"
    )
    mana_label.config(text=f"Мана: {player_stats['mana']} / {player_stats['max_mana']}")

def update_inventory_display():
    """Очищает список на экране и заполняет его заново из словаря"""
    # Очищаем Listbox от первой (0) до последней ("end") строчки
    inventory_listbox.delete(0, "end")
    
    if not player_stats["inventory"]:
        inventory_listbox.insert("end", "Ваша сумка пока пуста...")
        return
    
    for display_name, item_data in player_stats["inventory"].items():
        quantity = item_data["quantity"]
        # Добавляем строчку в конец списка
        inventory_listbox.insert("end", f"{display_name}: {quantity} шт.")

def on_herb_select(event):
    """Срабатывает, когда игрок кликает по строчке в сумке"""
    # Получаем номер выбранной строчки
    selection = inventory_listbox.curselection()
    if not selection:
        return
    
    # Достаём текст этой строчки (например: "Неизвестное растение (Редк. 1): 2 шт.")
    selected_text = inventory_listbox.get(selection[0])
    
    if "пуста" in selected_text:
        return
        
    # Отрезаем количество штук (всё, что после двоеточия), чтобы осталось чистое имя
    herb_name = selected_text.split(":")[0]
    
    # Меняем текст кнопки и включаем её!
    study_button.config(text=f"Изучить: {herb_name}", state="normal")

def add_exp_and_update_profile(amount):
    """Начисляет опыт, повышает уровень при необходимости и обновляет верхнюю панель"""
    player_stats["exp"] += amount
    
    # Каждые 3 единицы опыта повышают уровень на 1 (для 1-го уровня нужно 3 опыта, для 2-го — 6 и т.д.)
    exp_needed = player_stats["level"] * 3
    
    if player_stats["exp"] >= exp_needed:
        player_stats["exp"] -= exp_needed
        player_stats["level"] += 1
        player_stats["wisdom"] += 1
        # При повышении уровня можно также немного увеличивать запас маны!
        player_stats["max_mana"] += 10
        player_stats["mana"] = player_stats["max_mana"] # Полностью восстанавливаем ману

    # Обновляем текст в верхней золотой рамке
    stats_label.config(
        text=f"Уровень: {player_stats['level']} (Опыт: {player_stats['exp']}/{player_stats['level'] * 3})   |   Мудрость: {player_stats['wisdom']}"
    )
    mana_label.config(
        text=f"Мана: {player_stats['mana']} / {player_stats['max_mana']}"
    )


def study_herb():
    """Изучает выбранную в сумке траву, раскрывая её имя и свойства"""
    selection = inventory_listbox.curselection()
    if not selection:
        return
        
    selected_text = inventory_listbox.get(selection[0])
    if "пуста" in selected_text:
        return

    # Отрезаем количество ("Одуванчик (1/3): 2 шт." -> "Одуванчик (1/3)")
    item_key = selected_text.split(":")[0]
    
    # Проверяем, есть ли такой ключ в словаре инвентаря
    if item_key not in player_stats["inventory"]:
        return

    item_data = player_stats["inventory"][item_key]
    
    # --- ВАРИАНТ 1: Изучаем НЕИЗВЕСТНОЕ растение ---
    if "Неизвестное растение" in item_key:
        # Вытаскиваем одно истинное имя из скрытого списка
        true_name = item_data["true_names"].pop(0)
        herb_info = INGREDIENTS_HAR[true_name]
        
        # Проверяем, хватает ли Мудрости и Маны
        if player_stats["wisdom"] < herb_info["required_wisdom"]:
            # Возвращаем имя обратно в список, так как изучить не смогли
            item_data["true_names"].append(true_name)
            forest_status.config(text=f"Не хватает Мудрости! Нужно: {herb_info['required_wisdom']}", fg="#e24a4a")
            return
            
        if player_stats["mana"] < herb_info["mana_cost"]:
            item_data["true_names"].append(true_name)
            forest_status.config(text=f"Не хватает Маны! Нужно: {herb_info['mana_cost']}", fg="#4a90e2")
            return

        # Всё хватает! Списываем ману и уменьшаем стопку неизвестных трав
        player_stats["mana"] -= herb_info["mana_cost"]
        item_data["quantity"] -= 1
        if item_data["quantity"] <= 0:
            del player_stats["inventory"][item_key]

        # Проверяем, знали ли мы эту траву раньше
        current_knowledge = player_stats["herb_knowledge"].get(true_name, 0)
        
        if current_knowledge == 0:
            player_stats["herb_knowledge"][true_name] = 1
            msg = f"Опознано новое растение: {true_name} (1/3)!\nТеперь оно появится в Справочнике."
        else:
            # Если уже опознавали раньше — просто кладём в сумку под настоящим именем!
            known_key = f"{true_name} ({current_knowledge}/3)"
            if known_key not in player_stats["inventory"]:
                player_stats["inventory"][known_key] = {"quantity": 1, "true_name": true_name}
            else:
                player_stats["inventory"][known_key]["quantity"] += 1
            msg = f"Вы сразу узнали это растение — это {true_name}! Оно добавлено в сумку."

        add_exp_and_update_profile(1)
        forest_status.config(text=msg, fg="#d4af37")

    # --- ВАРИАНТ 2: Углубляем знания об ИЗВЕСТНОМ растении (с 1/3 до 3/3) ---
    else:
        true_name = item_data["true_name"]
        herb_info = INGREDIENTS_HAR[true_name]
        current_knowledge = player_stats["herb_knowledge"].get(true_name, 1)
        
        if current_knowledge >= 3:
            forest_status.config(text=f"Вы уже знаете о растении «{true_name}» абсолютно всё (3/3)!", fg="#a89f91")
            return
            
        if player_stats["mana"] < herb_info["mana_cost"]:
            forest_status.config(text=f"Не хватает Маны для глубокого анализа! Нужно: {herb_info['mana_cost']}", fg="#4a90e2")
            return

        # Тратим ману и 1 стебель из сумки
        player_stats["mana"] -= herb_info["mana_cost"]
        item_data["quantity"] -= 1
        if item_data["quantity"] <= 0:
            del player_stats["inventory"][item_key]

        # Повышаем уровень знаний!
        new_knowledge = current_knowledge + 1
        player_stats["herb_knowledge"][true_name] = new_knowledge
        
        # Если в сумке ещё оставались такие же стебли, обновляем им подпись (например с 1/3 на 2/3)
        if item_key in player_stats["inventory"]:
            old_qty = player_stats["inventory"].pop(item_key)["quantity"]
            new_key = f"{true_name} ({new_knowledge}/3)"
            player_stats["inventory"][new_key] = {"quantity": old_qty, "true_name": true_name}

        if new_knowledge == 2:
            msg = f"Изучено (2/3): {true_name}\nОткрыто описание:\n{herb_info['description']}"
        elif new_knowledge == 3:
            msg = f"Мастерство (3/3): {true_name}\nОткрыто свойство в напитках:\n{herb_info['effect']}"

        add_exp_and_update_profile(1)
        forest_status.config(text=msg, fg="#e6dfd3")

    # Обновляем список сумки и сбрасываем кнопку
    update_inventory_display()
    study_button.config(text="Выберите траву в сумке", state="disabled")



def on_inventory_select(event):
    """Срабатывает, когда игрок кликает по строчке в Сумке"""
    selection = inventory_listbox.curselection()
    if not selection or not inventory_keys_order:
        return
        
    index = selection[0]
    selected_key = inventory_keys_order[index]
    
    # Если трава уже изучена на максимум (3/3), изучать её больше не нужно
    if selected_key in INGREDIENTS_HAR and player_stats["herb_knowledge"].get(selected_key, 0) >= 3:
        study_button.config(text=f"{selected_key} (изучено)", state="disabled")
    else:
        # Меняем текст кнопки под выбранное растение!
        short_name = selected_key.replace("Неизвестное растение ", "Неизв. ")
        study_button.config(text=f"Изучить: {short_name}", state="normal")

# Привязываем клик по списку к функции on_inventory_select
inventory_listbox.bind("<<ListboxSelect>>", on_inventory_select)


# сбор трав
is_gathering = False

def go_to_forest(event=None):
    global is_gathering
    import random
    
    if event is not None and event.char not in ['f', 'F', 'а', 'А']:
        return
    if is_gathering:
        return
        
    is_gathering = True
    gather_button.config(state="disabled")
    
    # Пока собираем травы 1-й редкости
    starting_herbs = [name for name, info in INGREDIENTS_HAR.items() if info["rarity"] == 1]
    target_herb = random.choice(starting_herbs)
    gather_duration = INGREDIENTS_HAR[target_herb]["gather_time"]
    
    countdown_gathering(gather_duration, target_herb)

def countdown_gathering(seconds_left, target_herb):
    if seconds_left > 0:
        forest_status.config(
            text=f"Вы пробираетесь сквозь чащу...\n\n⏳ Осталось времени: {seconds_left} сек.",
            fg="#d4af37"
        )
        root.after(1000, countdown_gathering, seconds_left - 1, target_herb)
    else:
        finish_gathering(target_herb)

def finish_gathering(true_name):
    """Кладет заранее выбранную траву в сумку (с именем, если она уже изучена)"""
    global is_gathering
    
    rarity = INGREDIENTS_HAR[true_name]["rarity"]
    # Проверяем, знает ли алхимик эту траву (от 0 до 3)
    knowledge = player_stats["herb_knowledge"].get(true_name, 0)
    
    if knowledge == 0:
        # Если не знаем — прячем под маской неизвестного растения
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
    else:
        # Если уже опознали (1/3 и выше) — кладем сразу под настоящим именем!
        display_name = f"{true_name} ({knowledge}/3)"
        if display_name not in player_stats["inventory"]:
            player_stats["inventory"][display_name] = {
                "quantity": 1,
                "true_name": true_name
            }
        else:
            player_stats["inventory"][display_name]["quantity"] += 1
            
    update_inventory_display()
    
    forest_status.config(
        text=f"✨ Поиск завершён!\n\nВ сумку добавлено:\n{display_name}",
        fg="#e6dfd3"
    )
    
    gather_button.config(state="normal")
    is_gathering = False


# кнопки
gather_button = tk.Button(
    forest_frame,
    text="Отправиться на поиски [F]",
    bg="#3e322d", fg="#d4af37", activebackground="#54433c", activeforeground="#ffffff",
    font=("Courier", 10, "bold"), command=go_to_forest   
)
gather_button.pack(pady=10)

# Кнопка изучения в Сумке (пока без команды — её напишем следующим шагом!)
study_button = tk.Button(
    inventory_frame,
    text="Выберите растение",
    bg="#3e322d", 
    fg="#d4af37", 
    activebackground="#54433c", 
    activeforeground="#ffffff",
    font=("Courier", 10, "bold"), 
    state="disabled",
    command=study_herb
)
study_button.pack(pady=10, padx=10, fill="x")

# Привязка клавиши F
root.bind("<Key>", go_to_forest)

# Первичная отрисовка пустой сумки
update_inventory_display()

inventory_listbox.bind("<<ListboxSelect>>", on_herb_select)

root.mainloop()
