''' 
- É uma biblioteca para executar a validação de dados. A forma dos dados é declarada como classes com atributos, e cada atributo tem um tipo.
- Em seguida, é criada uma instância dessa classe com alguns valores e ela os validará, os converterá para o tipo apropriado (se for o caso) e fornecerá um objeto com todos os dados. 
'''

from datetime import datetime
from typing import List, Union

from pydantic import BaseModel

class User (BaseModel):
    id:int
    name: str = "Rai Oliveira"
    signup_ts: Union[datetime, None] = None
    friends: List [int] = []

external_data = {
    "id": "123",
    "signup_ts": "2023-06-01 12:22",
    "friends": [1,"2", b"3"], 
}
user = User (**external_data)
print (user)
print (user.id)