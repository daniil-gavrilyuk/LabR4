class Animal:
    """
    Базовый класс для всех животных.
    """

    def __init__(self, name: str, age: int, weight: float):
        """
        Конструктор базового класса Animal.

        :param name: Имя животного.
        :param age: Возраст животного.
        :param weight: Вес животного.
        """
        self.name = name
        self.age = age
        self.weight = weight

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.
        """
        return f"{self.name}, {self.age} лет, {self.weight} кг"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление объекта.
        """
        return f"Animal(name={self.name}, age={self.age}, weight={self.weight})"

    def make_sound(self) -> str:
        """
        Возвращает звук, который издает животное.
        """
        return "Неизвестный звук"

    def eat(self, food: str) -> str:
        """
        Метод, описывающий процесс питания животного.

        :param food: Название еды.
        :return: Строка с описанием процесса питания.
        """
        return f"{self.name} ест {food}."

class Dog(Animal):
    """
    Дочерний класс, представляющий собаку.
    """

    def __init__(self, name: str, age: int, weight: float, breed: str):
        """
        Конструктор класса Dog.

        :param breed: Порода собаки.
        """
        super().__init__(name, age, weight)
        self.breed = breed

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.
        """
        return f"{self.name}, {self.age} лет, {self.weight} кг, порода: {self.breed}"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление объекта.
        """
        return f"Dog(name={self.name}, age={self.age}, weight={self.weight}, breed={self.breed})"

    def make_sound(self) -> str:
        """
        Возвращает звук, который издает собака.
        Перегруженный метод, так как звук собаки отличается от общего звука животного.
        """
        return "Гав!"

    def fetch(self, item: str) -> str:
        """
        Метод, описывающий процесс принесения предмета собакой.

        :param item: Название предмета.
        :return: Строка с описанием процесса.
        """
        return f"{self.name} приносит {item}."

class Cat(Animal):
    """
    Дочерний класс, представляющий кошку.
    """

    def __init__(self, name: str, age: int, weight: float, color: str):
        """
        Конструктор класса Cat.

        :param color: Цвет кошки.
        """
        super().__init__(name, age, weight)
        self.color = color

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.
        """
        return f"{self.name}, {self.age} лет, {self.weight} кг, цвет: {self.color}"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление объекта.
        """
        return f"Cat(name={self.name}, age={self.age}, weight={self.weight}, color={self.color})"

    def make_sound(self) -> str:
        """
        Возвращает звук, который издает кошка.
        Перегруженный метод, так как звук кошки отличается от общего звука животного.
        """
        return "Мяу!"

    def purr(self) -> str:
        """
        Метод, описывающий процесс мурлыканья кошки.

        :return: Строка с описанием процесса.
        """
        return f"{self.name} мурлычет."

if __name__ == "__main__":
    # Создаем объекты классов
    animal = Animal("Животное", 5, 10)
    dog = Dog("Бобик", 3, 15, "Дворняжка")
    cat = Cat("Мурка", 2, 5, "Рыжий")

    # Выводим информацию о животных
    print(animal)
    print(dog)
    print(cat)

    # Выводим звуки, которые издают животные
    print(animal.make_sound())
    print(dog.make_sound())
    print(cat.make_sound())

    # Используем специфичные методы дочерних классов
    print(dog.fetch("мяч"))
    print(cat.purr())
