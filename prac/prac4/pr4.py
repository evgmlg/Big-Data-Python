import matplotlib.pyplot as plt
import numpy as np
from recommendations import critics
from recommendations import sim_distance
from recommendations import sim_pearson
from recommendations import top_matches

#Задание1
film1 = "Зима в Простоквашино"
film2 = "Котёнок по имени Гав"
common_ratings = {}
for critic, ratings in critics.items():
    if film1 in ratings and film2 in ratings:
        common_ratings[critic] = (ratings[film1], ratings[film2])
x = [rating[0] for rating in common_ratings.values()]
y = [rating[1] for rating in common_ratings.values()]
critic_names = list(common_ratings.keys())
plt.figure(figsize=(10, 6))
plt.scatter(x, y)
for i, name in enumerate(critic_names):
    plt.annotate(name, (x[i], y[i]), fontsize=8)
plt.title(f'Оценки критиков за "{film1}" и "{film2}"')
plt.xlabel(f'Оценки за "{film1}"')
plt.ylabel(f'Оценки за "{film2}"')
plt.xlim(0, 5)
plt.ylim(0, 5)
plt.grid(True)
plt.show()

#Задание2
person1 = "Дядя Фёдор"
person2 = "Телёнок Гаврюша"
person3 = "Галчонок"
person4 = "Почтальон Печкин"
similarity = sim_distance(critics, person1, person2)
print(f"Метрика схожести между {person1} и {person2}: {similarity}")
similarity1 = sim_distance(critics, person3, person4)
print(f"Метрика схожести между {person3} и {person4}: {similarity1}")

#Задание3
pearson = sim_pearson(critics, person1, person2)
print(f"Метрика схожести между {person1} и {person2}: {pearson}")
pearson1 = sim_pearson(critics, person3, person4)
print(f"Метрика схожести между {person3} и {person4}: {pearson1}")

#Задание4
person = "Дядя Фёдор"
similar_critics = top_matches(critics, person)
print("Наиболее похожие критики:")
for critic, simil in similar_critics:
    print(f"{critic}: {simil}")

critic1 = "Дядя Фёдор"
critic2 = "Кот Матроскин"
common_movies = [movie for movie in critics[critic1] if movie in critics[critic2]]
ratings_critic1 = [critics[critic1][movie] for movie in common_movies]
ratings_critic2 = [critics[critic2][movie] for movie in common_movies]
plt.scatter(ratings_critic1, ratings_critic2, color="blue")
plt.title(f'Оценки критиков "{critic1}" и "наиболее похожего"')
plt.xlabel(f'Оценки критика "{critic1}"')
plt.ylabel(f'Оценки критика "{critic2}"')
plt.xlim(0, 5)
plt.ylim(0, 5)
best_fit = np.polyfit(ratings_critic1, ratings_critic2, 1)
plt.plot(ratings_critic1, np.polyval(best_fit, ratings_critic1), color="red", linestyle="-")
plt.legend()
plt.grid(True)
plt.show()

critic3 = "Дядя Фёдор"
critic4 = "Корова Мурка"
common_movies = [movie for movie in critics[critic3] if movie in critics[critic4]]
ratings_critic3 = [critics[critic3][movie] for movie in common_movies]
ratings_critic4 = [critics[critic4][movie] for movie in common_movies]
plt.scatter(ratings_critic3, ratings_critic4, color="blue")
plt.title(f'Оценки критиков "{critic3}" и "наименее похожего"')
plt.xlabel(f'Оценки критика "{critic3}"')
plt.ylabel(f'Оценки критика "{critic4}"')
plt.xlim(0, 5)
plt.ylim(0, 5)
best_fit = np.polyfit(ratings_critic3, ratings_critic4, 1)
plt.plot(ratings_critic3, np.polyval(best_fit, ratings_critic3), color="red", linestyle="-")
plt.legend()
plt.grid(True)
plt.show()