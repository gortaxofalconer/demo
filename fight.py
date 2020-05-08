import random as r, sys
class Person:
    def __init__(self, name, species, job, origin,
                 armor, hp, stren):
        self._name = name
        self._species = species
        self._job = job
        self._origin = origin
        self._armor = armor
        self._hp = hp
        self._stren = stren
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
    def stren(self):
        return self._stren

Ben = Person("Ben", "human", "assassin", "Cornwall", armor=10,
             hp=10, stren=r.randint(1,21))
Alfred = Person("Alfred", "dwarf", "innkeep", "Devon", armor=r.randint(-1,1),
                hp=r.randint(1,20), stren=14)
def fight(person, val3):
    val3 = ""
    #knockout function when enemy hp is 0 or less 
    def ko():
        print(f"{person.name()} lies dead before you.\n"
              f"You were the monster all along.")
        sys.exit()
    #asks if you want to attack. if you do, - 1 amt target HP. if not u chill
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
h = ""
fight(Ben, h)

#    if person2.armor() >= person1.stren():
#        print(f"{announcement}\nYour blow has no effect.")
#        main()
#    else: person2.armor() < person1.stren()
#    print(f"{announcement}")
#    damage(person2, person2.hp())



