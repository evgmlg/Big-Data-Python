# словарь критиков и их оценок для небольшого числа мультфильмов
critics = {
    'Кот Матроскин': {
        'Зима в Простоквашино': 2.5,
        'Каникулы в Простоквашино': 3.5,
        'Ёжик в тумане': 3.0,
        'Винни-Пух': 3.5,
        'Ну, погоди!': 2.5,
        'Котёнок по имени Гав': 3.0
    },
    'Пёс Шарик': {
        'Зима в Простоквашино': 3.0,
        'Каникулы в Простоквашино': 3.5,
        'Ёжик в тумане': 1.5,
        'Винни-Пух': 5.0,
        'Котёнок по имени Гав': 3.0,
        'Ну, погоди!': 3.5
    },
    'Почтальон Печкин': {
        'Зима в Простоквашино': 2.5,
        'Каникулы в Простоквашино': 3.0,
        'Винни-Пух': 3.5,
        'Котёнок по имени Гав': 4.0
    },
    'Корова Мурка': {
        'Каникулы в Простоквашино': 3.5,
        'Ёжик в тумане': 3.0,
        'Котёнок по имени Гав': 4.5,
        'Винни-Пух': 4.0,
        'Ну, погоди!': 2.5
    },
    'Телёнок Гаврюша': {
        'Зима в Простоквашино': 3.0,
        'Каникулы в Простоквашино': 4.0,
        'Ёжик в тумане': 2.0,
        'Винни-Пух': 3.0,
        'Котёнок по имени Гав': 3.0,
        'Ну, погоди!': 2.0
    },
    'Галчонок': {
        'Зима в Простоквашино': 3.0,
        'Каникулы в Простоквашино': 4.0,
        'Котёнок по имени Гав': 3.0,
        'Винни-Пух': 5.0,
        'Ну, погоди!': 3.5
    },
    'Дядя Фёдор': {
        'Каникулы в Простоквашино': 4.5,
        'Ну, погоди!': 1.0,
        'Винни-Пух': 4.0
    }
}

from math import sqrt

def sim_distance(critics, person1, person2):
    common_items = [item for item in critics[person1] if item in critics[person2]]
    
    if not common_items:
        return 0
    
    sum_of_squares = sum([(critics[person1][item] - critics[person2][item]) ** 2 for item in common_items])
    
    similarity = 1 / (1 + sqrt(sum_of_squares / len(common_items)))
    return similarity

def sim_pearson(critics, person1, person2):
    common_items = [item for item in critics[person1] if item in critics[person2]]
    
    if not common_items:
        return 0
    
    sum1 = sum([critics[person1][item] for item in common_items])
    sum2 = sum([critics[person2][item] for item in common_items])
    
    sum1_squared = sum([pow(critics[person1][item], 2) for item in common_items])
    sum2_squared = sum([pow(critics[person2][item], 2) for item in common_items])
    
    product_sum = sum([critics[person1][item] * critics[person2][item] for item in common_items])
    
    n = len(common_items)
    
    num = product_sum - (sum1 * sum2 / n)
    den = sqrt((sum1_squared - pow(sum1, 2) / n) * (sum2_squared - pow(sum2, 2) / n))
    
    if den == 0:
        return 0
    
    pearson = num / den
    return pearson

def top_matches(critics, person):
    common_items = [item for item in critics[person]]
    
    if not common_items:
        return 0
    
    n = len(common_items)

    scores = [(other, sim_pearson(critics, person, other)) for other in critics if other != person]

    scores.sort(key=lambda x: x[1], reverse=True)

    return scores[:n]