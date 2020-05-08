import random as r, sys
class Person:
    def __init__(self, name, species, job, origin,
                 hp, armor, weapon, stren, dex, moves):
        self._name = name
        self._species = species
        self._job = job
        self._origin = origin
        self._armor = armor
        self._weapon = weapon
        self._hp = hp
        self._stren = stren
        self._moves = moves
        self._dex = dex
        
    def name(self):
        return self._name
    def species(self):
        return self._species
    def job(self):
        return self._job
    def origin(self):
        return self._origin
    def hp(self):
        return self._hp
    def armor(self):
        return self._armor
    def weapon(self):
        return self._weapon
    def stren(self):
        return self._stren
    def dex(self):
        return self._dex
    def moves(self):
        return self._moves

def findattack(weapon, move, dex):
    if dex <= 5:
        move =.75*move
    elif dex >=15:
        move = 1.25*move
    attack = weapon*move
        

Ben = Person("Ben", "human", "assassin", "Cornwall",
             hp = 10, armor=10,
             weapon = r.randint(1,8), stren=r.randint(1,20),
             dex = r.randint(1,20),
             moves=1,)

Alfred = Person("Alfred", "dwarf", "innkeep", "Devon",
                hp=r.randint(1,20), armor=r.randint(-1,1),
                weapon = r.randint(1,20), stren=10,
                dex=15,
                moves=1)

def fight(person, hp):
    val3 = person.hp()
    #knockout function when enemy hp is 0 or less 
    def ko():
        print(f"{person.name()} the {person.species()} of {person.origin()} lies dead before you.\n"
              f"You were the monster all along.")
        sys.exit()
    #asks if you want to attack. if you do, - 1 amt target HP. if not u chill
    #in the future it would run use attack (defined as (m*w)*dex
    def dmg(val3):
        ddval= ""
        answer = ""
        try:
            ddval = float(val3)
            answer += input(f"Do you want to attack?\n")
            if "y" in answer.lower():
                ddval -= 1
                print(f"{person.name()} loses 1 HP and now has {ddval}.")
            else: print(f"Alright then.")
            if ddval <= 0: ko()
            else: dmg(ddval)
        except ValueError as valerror:
            print(f"{valerror}")
    def prompt(val3):
        try:
            val3 = float(person.hp())#try val3=Alfred.hp() maybe?
            print(f"Your target's HP is {val3}.")
            dmg(val3)
        except ValueError as valerror: print("Error! {valerror}!")
        if val3 <= 0: ko()
        else: dmg(val3)
        prompt(val3)
        if float(val) <= 0: ko()
    prompt(val3)

fight(Ben, Ben.hp())

#    if person2.armor() >= person1.stren():
#        print(f"{announcement}\nYour blow has no effect.")
#        main()
#    else: person2.armor() < person1.stren()
#    print(f"{announcement}")
#    damage(person2, person2.hp())



