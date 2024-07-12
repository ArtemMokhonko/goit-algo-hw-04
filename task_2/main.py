def merge(left, right):
    # Створюємо порожній список для збереження злитого результату
    merged = []
    # Індекси для ітерування по лівому та правому спискам
    left_index = 0
    right_index = 0

    # Порівнюємо елементи з обох списків, додаємо менший елемент до 'merged'
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Додаємо залишкові елементи з лівого списку (якщо є)
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    # Додаємо залишкові елементи з правого списку (якщо є)
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    # Повертаємо злитий список
    return merged

def merge_k_lists(lists):
    # Якщо список порожній, повертаємо порожній список
    if not lists:
        return []
    
    # Якщо список містить лише один підсписок, повертаємо цей підсписок
    if len(lists) == 1:
        return lists[0]

    # Знаходимо середину списку для розділення
    mid = len(lists) // 2

    # Рекурсивно зливаємо ліву частину списку
    left_merged = merge_k_lists(lists[:mid])

    # Рекурсивно зливаємо праву частину списку
    right_merged = merge_k_lists(lists[mid:])

    # Зливаємо дві частини разом за допомогою функції 'merge'
    return merge(left_merged, right_merged)

# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)

# Виведення результату
print("Відсортований список:", merged_list)

