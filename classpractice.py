import random as r
class Person:
    def __init__(self,
                 name, job, species,
                 origin, alignment,
                 hp, mp, armor,
                 stren, const, dext,
                 intel, wis, char):
                 #inventory (weapon, wand,
                 #     armor,
                 #     copper, silver, gold,
                 #     misc),
                 #     spells):
        self._name = name
        self._species = species
        self._job = job
        self._origin = origin
        self._armor = armor
        self._alignment = alignment
        self._hp = hp
        self._mp = mp
        self._stren = stren
        #i mean ideally it wouldnt go above 20 anyway
        #should stren affect inventory as as well as atk?
        self._const = const
        #something should go here
        self._dext = dext
        #should dext affect inventory as well as def
        #should there be nerfs for <1 mentals?
        self._intel = intel
        self._wis = wis
        self._char = char
        self._alignment = alignment
        #sef._inventory = inventory
    def name(self):
        return self._name
    def species(self):
        return self._species
    def job(self):
        return self._job
    def origin(self):
        return self._origin
    def alignment(self):
        return self._alignment
    def hp(self):
        return self._hp
    def mp(self):
        return self._mp
    def armor(self):
        return self._armor
    def stren(self):
        return self._stren
    def const(self):
        return self._const
    def dext(self):
        return self._dext
    def intel(self):
        return self._intel
    def wis(self):
        return self._wis
    def char(self):
        return self._char
    #def inventory(self):
     #   return self._inventory
    #def spells(self):
    #    return self._spells
Ben = Person("Ben", "hunter", "human",
             "Cornwall", "lawful good",
             hp=14,mp=3, armor=10,
             stren=r.randint(1,21), const=13, dext=14,
             intel=13, wis=12, char=11)
Alfred = Person("Alfred", "innkeep", "dwarf",
                "Cornwall", "lawful good",
                hp=r.randint(1,20), mp=3, armor=r.randint(1,20),
                stren=14, const=14, dext=14,
                intel=12, wis=14, char=16)

def damage(person, hp):
    hp = person.hp()
    hp -= 1
    print(f"{person.name()} loses 1 HP and now has {hp} HP!")
    main()

def attack(person1, person2):
    announcement = (
        f"{person1.name()} hits {person2.name()} for {person1.stren()}"
        f" hit points!\n{person2.name()} has {person2.armor()} armor and"
        f" {person2.hp()} HP")
    if person2.armor()>=person1.stren():
        print(f"{announcement}\n{person1.name()}'s blow has no effect.")
        main()
    elif person2.armor() < person1.stren():
        print(f"{announcement}")
    else: damage(person2, person2.hp())

def fight(person1, person2):
    if person2.hp() <= 0:
        print(
            f"{person2.name()} the {person2.job()}, {person2.species()} of"
            f" {person2.origin()}, is dead!")
    elif person2.hp() > 0: attack(person1, person2)
    
def fightstart(person1, person2):
    startfight = ""
    startfight += input(
        f"Do you wish to attack {person2.name()} at {person2.hp()} HP?\n")
    if "no" in startfight.lower():
        print("You decide against starting a fight on your first day.")
    else: fight(person1, person2)          
    
def main():
    fightstart(Ben, Alfred)
    
main()