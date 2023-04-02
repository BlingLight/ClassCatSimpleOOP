class Cat:
    Hungry = 2
    Play = 2
    Sleep = 2

    def __init__(self, Hungry, Sleep, Play):
        self.Hungry = Hungry
        self.Play = Play
        self.Sleep = Sleep

    def Eat(self):
        if self.Hungry == 3:
            print("Я ссыт")
        elif self.Hungry == 2 or self.Hungry == 1:
            print("Ням ням")
            self.Hungry += 1
            self.Sleep -= 1
            self.Play -= 1

    def Slept(self):
        if self.Sleep == 3:
            print("Я не хочу спать")
        elif self.Sleep == 2 or self.Sleep == 1:
            if self.Hungry == 1:
                print("Вначале поесть")
            else:
                print("Поспал")
                self.Sleep += 1
                self.Hungry -= 1
                self.Play -= 1

    def Played(self):
        if self.Hungry == 1 and self.Sleep == 1:
            print("Я ХОЧУ ЕСТЬ И СПАТЬ")
        elif self.Hungry == 1:
            print("хочу есть")
        elif self.Sleep == 1:
            print("хочу спать")
        else:
            print("круто поиграли")
            self.Play += 1
            self.Hungry -= 1
            self.Sleep -= 1


cat = Cat(2, 2, 2)
exit = 0
while exit == 0:
    choice = input("""
Привет теперь ты хозяин этой кошки 
1 - Покормить 
2 - Поиграть 
3 - Поспать 
4 - Выйти    
""")
    if choice == "1":
        cat.Eat()
    elif choice == "2":
        cat.Played()
    elif choice == "3":
        cat.Slept()
    elif choice == "4":
        exit += 1
    else:
        print("хз")