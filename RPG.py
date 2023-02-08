class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    
    def attack(self, target):
        target.health -= self.power
        print(f"{self.name} atacó a {target.name} y le quitó {self.power} puntos de vida")
        
    def check_health(self):
        if self.health <= 0:
            print(f"{self.name} ha muerto")
        else:
            print(f"{self.name} tiene {self.health} puntos de vida")

hero = Character("Hero", 10, 5)
goblin = Character("Goblin", 6, 2)

def game_menu():
    print("1. Ver salud del héroe")
    print("2. Ver salud del goblin")
    print("3. Atacar al goblin")
    print("4. Salir del juego")
    choice = int(input("Elige una opción: "))
    if choice == 1:
        hero.check_health()
    elif choice == 2:
        goblin.check_health()
    elif choice == 3:
        hero.attack(goblin)
        goblin.check_health()
    elif choice == 4:
        exit()
    else:
        print("Opción inválida")

while True:
    game_menu()