import random

class Coin:   ### Abstract class ###
    def __init__(self, rare=False, clean=True, heads=True, **kwargs):    ### Packing the data 

        for key,value in kwargs.items():
            setattr(self,key,value)      ### setattr() function will convert self,key,value as self.key=value
            
        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads

        if self.is_rare:
            self.value =  self.original_value * 1.25
        else:
            self.value = self.original_value

        if self.is_clean:
            self.color =  self.clean_color
        else:
            self.color = self.rusty_color
    def rust(self):
        self.color = self.rusty_color

    def clean(self):
        self.color = self.clean_color

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice

    def __del__(self):
        print("Coin Spent")

    def __str__(self):
        if self.original_value > 1:
            return "${} coint".format(int(self.original_value))
        else:
            return "{}p Coin".format(int(self.original_value * 100))

class One_pence(Coin):   ### one_pence class inherits Coin class
    def __init__(self):
        data = {
            "original_value" : 0.01,
            "clean_color" : "Bronze",
            "rusty_color" : "Brownish",
            "num_edges" : 1,
            "diameter" : 20.3,
            "thickness" : 1.52,
            "mass" : 3.56
            }
        super().__init__(**data)                 ## Calling the parent class (Coin) and unpacking the key value pair


class Two_pence(Coin):   ### two_pence class inherits Coin class
    def __init__(self):
        data = {
            "original_value" : 0.02,
            "clean_color" : "Bronze",
            "rusty_color" : "Brownish",
            "num_edges" : 1,
            "diameter" : 25.9,
            "thickness" : 1.85,
            "mass" : 7.12
            }
        super().__init__(**data)                 ## Calling the parent class (Coin) and unpacking the key value pair



class Five_pence(Coin):   ### five_pence class inherits Coin class
    def __init__(self):
        data = {
            "original_value" : 0.05,
            "clean_color" : "Silver",
            "rusty_color" : None,
            "num_edges" : 1,
            "diameter" : 18.0,
            "thickness" : 1.77,
            "mass" : 3.25
            }
        super().__init__(**data)                 ## Calling the parent class (Coin) and unpacking the key value pair
        def rust(self):                 ### overriding the rust method in parent class (polymorphism)            
            self.color =  self.clean_color
        def clean(self):                 ### overriding the rust method in parent class (polymorphism) 
            self.color = self.clean_color


class Ten_pence(Coin):   ### ten_pence class inherits Coin class
    def __init__(self):
        data = {
            "original_value" : 0.10,
            "clean_color" : "Silver",
            "rusty_color" : None,
            "num_edges" : 1,
            "diameter" : 24.5,
            "thickness" : 1.85,
            "mass" : 6.50
            }
        super().__init__(**data)                 ## Calling the parent class (Coin) and unpacking the key value pair
        def rust(self):                 ### overriding the rust method in parent class (polymorphism)            
            self.color =  self.clean_color
        def clean(self):                 ### overriding the rust method in parent class (polymorphism) 
            self.color = self.clean_color




class Twenty_pence(Coin):   ### twenty_pence class inherits Coin class
    def __init__(self):
        data = {
            "original_value" : 0.20,
            "clean_color" : "Silver",
            "rusty_color" : None,
            "num_edges" : 7,
            "diameter" : 21.4,
            "thickness" : 1.7,
            "mass" : 5
            }
        super().__init__(**data)                 ## Calling the parent class (Coin) and unpacking the key value pair
        def rust(self):                 ### overriding the rust method in parent class (polymorphism)            
            self.color =  self.clean_color
        def clean(self):                 ### overriding the rust method in parent class (polymorphism) 
            self.color = self.clean_color


class Fifty_pence(Coin):   ### fifty_pence class inherits Coin class
    def __init__(self):
        data = {
            "original_value" : 0.50,
            "clean_color" : "Silver",
            "rusty_color" : None,
            "num_edges" : 7,
            "diameter" : 27.3,
            "thickness" : 1.78,
            "mass" : 8.00
            }
        super().__init__(**data)                 ## Calling the parent class (Coin) and unpacking the key value pair
        def rust(self):                 ### overriding the rust method in parent class (polymorphism)            
            self.color =  self.clean_color
        def clean(self):                 ### overriding the rust method in parent class (polymorphism) 
            self.color = self.clean_color


class One_pound(Coin):   ###One_pound class inherits Coin class
    def __init__(self):
        data = {
            "original_value" : 1.00,
            "clean_color" : "Gold",
            "rusty_color" : "Greenish",
            "num_edges" : 1,
            "diameter" : 22.5,
            "thickness" : 3.15,
            "mass" : 9.5
            }
        super().__init__(**data)                 ## Calling the parent class (Coin) and unpacking the key value pair


class Two_pound(Coin):   ### Two_pound class inherits Coin class
    def __init__(self):
        data = {
            "original_value" : 2.00,
            "clean_color" : "Gold & Silver",
            "rusty_color" : "Greenish",
            "num_edges" : 1,
            "diameter" : 28.4,
            "thickness" : 2.50,
            "mass" : 12
            }
        super().__init__(**data)                 ## Calling the parent class (Coin) and unpacking the key value pair


coins = [One_pence(), Two_pence(), Five_pence(), Ten_pence(), Twenty_pence(), Fifty_pence(), One_pound(), Two_pound()]

for coin in coins:
    arguments = [coin, coin.color, coin.value, coin.diameter, coin.thickness, coin.num_edges, coin.mass]
    string = "{} - color:{}, value:{}, diameter(mm):{}, thickness(mm):{}, number of edges:{}, mass(g):{}".format(*arguments)
    print(string)
        
            
    
