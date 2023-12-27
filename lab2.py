a = "інший текст"
b = 2  # Інше числове значення
c = ["b", 2, 2.5, "Інше слово"]  # Інший список
d = {"c": "Інше слово", "d": 2}  # Інший словник
e = ("b", "c")  # Інший кортеж
f = {"tt", "zz"}  # Інший набір

print("Результати роботи вбудованих констант:")
print("True і False:", True, False)
print("None:", None)

print("Результати роботи вбудованих функцій:")
print("abs(-12.5) =", abs(-12.5))
print("abs(12.5) =", abs(12.5))

letters = ["x", "y", "z"]
print("Результати роботи з циклами:")
for i in range(len(letters)):
    print(f"На позиції {i} знаходиться буква {letters[i]}")

A = False
print("Результати роботи з розгалуженнями:")
print("Значить А=True" if A else "Значить А=False")

A = 0
try:
    print("Що буде якщо", 10 / A, "?")
except Exception as e:
    print(e)
finally:
    print("А вот воно що!")

with open("README.md", "r") as f:
    print("Результати роботи контекст-менеджера with (читання з файлу README.md):")
    for line in f:
        print(line.strip())

this_is_lambda = lambda first, last: f'Цей код написав: {first} {last}'
print("Використання лямбда-функції:")
print("Це просто функція:", this_is_lambda)
print("Це її виклик:", this_is_lambda('Інший', 'Приклад'))
