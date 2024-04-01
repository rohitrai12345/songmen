#create a person class and set the age of the person using a constructo
#but if birht yer of  the person is passed then solve the probleuisng a fctory method
from datetime import datetime

class person:
    def __inti__(self, age):
        self.age=age
    @classmethod
    def from_birht_year(cls, year):
        age=datetime.now(2024)-year
        return cls(age)



p =person(32)
print(p.age) #32
p2=person.from_brith_year(1990)
print(p2.age)