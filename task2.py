# Початковий список
shopping_list = ["молоко", "хліб", "масло", "яйця", "сир", "яблука"]

# Генератор списку — залишаємо товари довші за 4 символи
long_items = [item for item in shopping_list if len(item) > 4]

print("Товари з назвами довше 4 символів:", long_items)
print("Кількість таких товарів:", len(long_items))
