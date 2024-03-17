#Tyipos em Python | Types Hints 
def get_full_name (first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

print (get_full_name("raissa", "oliveira"))

def get_name_with_age (name: str, age: str):
    name_with_age = name + " is this old " + age
    return name_with_age 


#Tipos genéricos com parâmetros de tipo
#LISTAS
from typing import List

def process_items (items: List[str]):
    for item in items:
        print (item)

#TUPLE E SET
from typing import Tuple, Set

def process_itens (itens_t: Tuple[int,int,str], itens_s: Set[bytes]):
    return itens_t, itens_s

#DICT
from typing import Dict

def process_items (prices: Dict[str,float]):       #o primeiro parâmetro é para as chaves do dict, e o segundo para para os valores do dict. 
    for item_name, item_price in prices.items():
        print (item_name)
        print (item_price)

#OPTIONAL
from typing import Optional

def say_hi (name: Optional[str] = None):
    if name is not None:
        print (f"Hey {name}!")
    else:
        print ("Hello World!")


#CLASSES COMO TIPO 
class Person: 
    def __init__(self, name: str):
        self.name = name
    
def get_person_name (one_person: Person):
    return one_person.name

