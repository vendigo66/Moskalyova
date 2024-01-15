import doctest


class MilkProduct:
    def __init__(self, cost_:(int, float), product_availability:str):
        """"
        Создание и подготовка к работе объекта "Товар"

        :param cost_ Стоимость товара
        :param product_availability Наличие товара

        Примеры:
        >>> творог = MilkProduct(200, "в наличии") # инициализация экземпляра класса
        """
        if not isinstance(cost_(int, float)):
            raise TypeError ("Стоимость товара должна быть типа int или float")
        if cost_ <= 0:
            raise ValueError (" Стоимость товара должна быть больше 0")
        self.cost_ = cost_

        if not isinstance(product_availability, str):
            raise TypeError("Указание наличия товара должно быть типа str")
        if product_availability != "в наличии" or "нет в наличии":
            raise ValueError ("Необходимо указывать наличие товара")
        self.product_availability = product_availability

    def cost_increased(self, markup_:(int, float)):
        """
        Функция, которая увеличивает стоимость товара при повышении цены

        :param: markup_ Наценка на товар в рублях

        Примеры:
        >>> творог = MilkProduct(200, "в наличии")
        >>>cost_increased(100)
        """
        ...
        if not isinstance(markup_,(int, float)):
            raise TypeError ("Наценка должна быть типа int или float")
        if markup_ <= 0:
            raise ValueError (" Наценка должна быть больше 0")
        self.cost_incresed = self.cost_ + markup_

    def cost_decreased(self, discount_:int):
        """
        Функция, которая уменьшает стоимость товара в зависимости от размера скидки

        :param: discount_ Размер скидки в процентах

        Примеры:
        >>> творог = MilkProduct(200, "в наличии")
        >>>cost_increased(100)
        """
        ...
        if not isinstance(discount_, int):
            raise TypeError("Скидка должна быть типа int")
        self.cost_decreased = (self.cost_ / (discount_/100 +1))


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()

class Car:
    def __init__(self, engine_capacity: (int, float), horsepower_: int):
        if not isinstance(engine_capacity(int, float)):
            raise TypeError ("Объем двигателя указывается типом int или float")
        if engine_capacity <= 0:
            raise ValueError (" Объем двигателя больше 0")
        self.engine_capacity = engine_capacity

        if not horsepower_(engine_capacity(int, float)):
            raise TypeError ("Количество лошадиных сил указывается типом int или float")
        if horsepower_ <= 0:
            raise ValueError ("Количество лошадиных сил должно быть больше 0")
        self.horsepower_ = horsepower_ 

