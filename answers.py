# Assignment 1: Design Your Own Class! 🏗️

class Smartphone:
    def __init__(self, brand, model, screen_size, storage_capacity):
        self.brand = brand
        self.model = model
        self.screen_size = screen_size  # inches
        self.storage_capacity = storage_capacity  # GB
        self.is_powered_on = False
        self.battery_level = 100
        self.installed_apps = []
    
    def power_toggle(self):
        self.is_powered_on = not self.is_powered_on
        status = "on" if self.is_powered_on else "off"
        return f"{self.brand} {self.model} is now powered {status}."
    
    def install_app(self, app_name):
        if not self.is_powered_on:
            return f"Cannot install apps when phone is powered off."
        self.installed_apps.append(app_name)
        self.battery_level -= 5  # Installing apps drains battery
        return f"{app_name} has been installed on {self.brand} {self.model}."
    
    def check_battery(self):
        return f"Battery level: {self.battery_level}%"
    
    def charge(self, minutes):
        charge_amount = minutes // 2  # 2 minutes = 1% charge
        self.battery_level = min(100, self.battery_level + charge_amount)
        return f"Phone charged to {self.battery_level}%"
    
    def __str__(self):
        status = "Powered On" if self.is_powered_on else "Powered Off"
        return f"{self.brand} {self.model} - {self.screen_size}\" - {self.storage_capacity}GB - {status}"


# Creating a child class with inheritance
class GamingPhone(Smartphone):
    def __init__(self, brand, model, screen_size, storage_capacity, gpu_model, refresh_rate):
        # Call parent constructor
        super().__init__(brand, model, screen_size, storage_capacity)
        # Add gaming-specific attributes
        self.gpu_model = gpu_model
        self.refresh_rate = refresh_rate  # Hz
        self.gaming_mode = False
    
    def toggle_gaming_mode(self):
        if not self.is_powered_on:
            return "Can't toggle gaming mode when phone is off."
        
        self.gaming_mode = not self.gaming_mode
        status = "activated" if self.gaming_mode else "deactivated"
        
        # Gaming mode uses more battery
        if self.gaming_mode:
            self.battery_level -= 10
        
        return f"Gaming mode {status}! Refresh rate set to {self.refresh_rate}Hz."
    
    def install_game(self, game_name, game_size):
        if game_size > self.storage_capacity * 0.25:  # Game too big (>25% of storage)
            return f"Warning: {game_name} is very large and may impact performance."
        return super().install_app(f"GAME: {game_name}")
    
    def __str__(self):
        parent_str = super().__str__()
        gaming_status = "Gaming Mode: ON" if self.gaming_mode else "Gaming Mode: OFF"
        return f"{parent_str} - {self.gpu_model} - {self.refresh_rate}Hz - {gaming_status}"


# Testing the classes
def test_smartphone_classes():
    # Creating a regular smartphone
    iphone = Smartphone("Apple", "iPhone 14", 6.1, 256)
    print(iphone)
    
    print(iphone.power_toggle())
    print(iphone.install_app("Instagram"))
    print(iphone.install_app("WhatsApp"))
    print(iphone.check_battery())
    
    # Creating a gaming phone
    rog_phone = GamingPhone("ASUS", "ROG Phone 7", 6.8, 512, "Adreno 730", 165)
    print("\n" + str(rog_phone))
    
    print(rog_phone.power_toggle())
    print(rog_phone.toggle_gaming_mode())
    print(rog_phone.install_game("Genshin Impact", 20))
    print(rog_phone.check_battery())
    print(rog_phone.charge(100))  # Charge for 100 minutes
    print(rog_phone)


# Activity 2: Polymorphism Challenge! 🎭

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def move(self):
        return "This animal moves somehow."
    
    def make_sound(self):
        return "This animal makes a sound."


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed
    
    def move(self):
        return f"{self.name} the {self.breed} is running on four legs! 🐕"
    
    def make_sound(self):
        return f"{self.name} barks: Woof! Woof! 🐶"


class Bird(Animal):
    def __init__(self, name, can_fly=True):
        super().__init__(name, "Bird")
        self.can_fly = can_fly
    
    def move(self):
        if self.can_fly:
            return f"{self.name} is soaring through the air! ✈️"
        return f"{self.name} is hopping around! 🐦"
    
    def make_sound(self):
        return f"{self.name} chirps: Tweet! Tweet! 🐤"


class Fish(Animal):
    def __init__(self, name, water_type):
        super().__init__(name, "Fish")
        self.water_type = water_type  # "freshwater" or "saltwater"
    
    def move(self):
        return f"{self.name} is swimming in {self.water_type}! 🐠"
    
    def make_sound(self):
        return f"{self.name} doesn't make much sound... Maybe some bubbles? 💭"


# Testing polymorphism
def test_animal_polymorphism():
    # Create different animal objects
    sparky = Dog("Sparky", "Border Collie")
    tweety = Bird("Tweety", True)
    nemo = Fish("Nemo", "saltwater")
    
    # Store them in a list to demonstrate polymorphism
    animals = [sparky, tweety, nemo]
    
    print("\nPolymorphism in action:")
    print("=======================")
    
    # Call the same method on different objects
    for animal in animals:
        print(f"{animal.name} ({animal.species}):")
        print(f"  Movement: {animal.move()}")
        print(f"  Sound: {animal.make_sound()}")
        print("-" * 40)


if __name__ == "__main__":
    print("Assignment 1 Output:")
    print("===================")
    test_smartphone_classes()
    
    print("\nActivity 2 Output:")
    print("=================")
    test_animal_polymorphism()