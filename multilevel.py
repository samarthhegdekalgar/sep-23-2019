class Animal:
    def __init__(self, is_bird):
        self.is_bird = is_bird

    def get_family(self):
        if self.is_bird:
            return "Birds"
        else:
            return "Mammals"


class Dog(Animal):
    def __init__(self, color, weight, height, is_bird):
        self.color = color
        self.weight = weight
        self.height = height
        super(Dog, self).__init__(is_bird)

    def get_dog_physique(self):
        return 'Color:{}\t Weight:{}\t Height:{}'.format(self.color, self.weight, self.height)


class Pug(Dog):
    def __init__(self, name, age, color, weight, height):
        self.name = name
        self.age = age
        super(Pug, self).__init__(color, weight, height, False)

    def get_pug_details(self):
        return 'Name:{}\t Age:{}'.format(self.name,self.age)


gabbar = Pug('Gabbar', 10, 'black', 20, 2.6)
print(gabbar.get_pug_details())
print(gabbar.get_dog_physique())
print(gabbar.get_family())