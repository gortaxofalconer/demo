import statistics as s, random as r, sys
#gathering inputs, setting length list
name = ""
name += input(f"What's your character's name?\n")
namelen = (len(name))
job = ""
job += input(f"What's your character's job?\n")
joblen = (len(job))
species = ""
species += input(f"What's your character's species?\n")
speclen = (len(species))
origin = ""
origin += input(f"Where is your character from?\n")
originlen = (len(origin))
alignment = ""
alignment += input(f"What's your character's alignment?\n")
alignlen = (len(alignment))
gearlist = [namelen, joblen, alignlen, speclen, originlen]
#setting alignments
evilal = False
goodal = False
neutralal = False
if "evil" in alignment.casefold(): evilal = True
else: pass
if evilal == True: action_str = (f"Exploit the weaker")
else: pass
if "good" in alignment.casefold(): goodal = True
else: pass
if goodal == True: action_str = (f"Defend the weaker")
else: neutralal = True
action_str = (f"Interact with the other")
####if user says they are a magic user they get mp and a wand
magic_jobs = ['witch', 'wizard', 'mage', 'magician',
              'warlock','sorcerer', 'sorceress']
if job.casefold() in magic_jobs: mp = r.randint(10,20)
else: mp = r.randint(2,9) 
hp = r.randint(10,20)
#makin strangs
main_str =(
    f"\nYou have created {name.title()} of {origin.title()}, the "
    f"{alignment.casefold()} {species.casefold()} {job.casefold()}.\nNow get out"
    f" there & kill some goblins or rats or whatever!")
rat_str = (
    f"\nUnless you are a {species.casefold()}, in which case: I'm so sorry."
    f" Hope you can make some cheddar with your {job.casefold()} skills.")
goblin_str = (
    f"\nUnless you are a {species.casefold()}, in which case: I'm so sorry."
    f" Hope life isn't gobblin' you up.")
#acknowledging magic
if mp >= 10: alignstr = (
    f"\n\nGo forth, {name.title()}! {action_str} {species.casefold()}s of"
    f" {origin.title()} using your magical {alignment.casefold()} {job.casefold()}"
    f" skills!")
else: alignstr = (
    f"\nGo forth, {name.title()}!\n{action_str} {species.casefold()}s of "
    f"{origin.title()} using your {alignment.casefold()} {job.casefold()} skills!")
#takes length of total inputs and sets money, weapons, armor
def gear(inputlist):
    goldcount = s.mean(inputlist)
    silvercount = s.median(inputlist)
    coppercount = sum(inputlist)
    #even copper = axe, odd = sword
    if coppercount % 2 == 0: weapon = (f"an axe")
    else: weapon = (f"a sword")
    #0-30 leather, 31-49 chain mail, 50+ full plate
    if 0 <= coppercount <= 30: armor = (f"boiled leather")
    elif 31 <= coppercount < 50: armor = (f"chain mail")
    else: armor = (f"full plate")
    #if you are magic you get a wand
    if mp >= 10: wand = True
    else: wand = False
    gear1 = (f"\nYou have {goldcount} gold pieces, {silvercount} silver"
        f" pieces and {coppercount} copper pieces.\nYou are armed with "
        f"{weapon}")
    gearw = (f" and your wand")
    gear2 = (f". \nYou are wearing {armor} armor.")
    if wand == True: print(f"{gear1}{gearw}{gear2}")
    else: print(f"{gear1}{gear2}")
#randomly sets and displays attributes and offers commentary
def attr():
    charisma = r.randint(1,20)
    strength = r.randint(5,20)
    const = r.randint(5,20)
    dext = r.randint(5,20)
    intel = r.randint(5,20)
    wis = r.randint(5,20)
    print(
        f"\nCHA: {charisma}\nSTR: {strength}\nCON: {const}\nDEX: {dext}"
        f"\nINT: {intel}\nWIS: {wis}")
    print(f"MP: {mp}\nHP: {hp}")
    #bard commentary
    if 15 <= charisma: print(
        f"With charisma like that, you could be one of the {alignment.casefold()}"
        f" bards of {origin.title()}!")
    elif charisma == 5: print("Good luck out there! You'll need it!")
    else: pass
    #fighter commentary
    if 15 <= strength: hulk = True
    elif 15 <= const: hulk = True
    else: hulk = False
    if hulk == True: print(
        f"With a frame like that, you could be the best {alignment.casefold()}"
        f" fighter in all of {origin.title()} !")
    elif (const or strength) == 5: print(
        f"You seem a little weak. Be careful out there!")
    else: pass
    #spellcaster commentary
    if 15 <= intel: genius = True
    elif 15 <= wis: genius = True
    else: genius = False
    if genius == True: print( 
        f"People with minds like yours tend to become {alignment.casefold()}"
        " spellcasters.")
    else: pass
    #simpleton commentary
    if 5 <=  intel <= 8: dumb = True
    elif 5 <= wis <= 8: dumb = True
    else: dumb = False
    if dumb == True: print(
        f"I can tell your journey will be full of hard decisions.")
    else: pass
    #thief commentary
    if 15 <= dext <= 20: print(
        f"Have you ever looked into {alignment.casefold()} thievery?")
    else: pass
#constructs and displays character intro
def intro():
    if "rat" == species.casefold(): print(f"{main_str} {rat_str}")
    elif "goblin" == species.casefold(): print(f"{main_str} {goblin_str}")
    else: print(f"{main_str} {alignstr}")
#tavern stuff
def tavern():
    move = ""
    #buying beer
    def buy(inputlist):
        coppercount = sum(inputlist)
        answer = ""
        answer += input(
            f"You look at the innkeep, who doesn't even give you a "
            f"chance to speak. 'The sun is still up. Pints are still "
            f"ten coppers. Want one?'\n")
        def deductcop(inputlist):
            coppercount = sum(inputlist)
            coppercount -= 10
            print(
            f"'Alright then,' he says. You hand him the ten coppers and"
            f" receive a pint. You now have {coppercount} coppers and"
            f" a pint of ale, which you drink all in one go. You hand the"
            f" pint mug back to the amazed innkeeper, who takes it back"
            f" without a word.")
            tavern()  
        if "y" in answer.casefold(): deductcop(inputlist)
        else: tavern()
    
    def brawl(): #fight(enemy)?
        print(f"Despite your armor and weaponry, you feel as though you"
              f" don't know enough 'pie-thon' to fight, whatever that "
              f"could mean. You find yourself remaining seated at your "
              f"table. You hear a distant tapping and muttering...")
        tavern()
        #need combatant*(Spell/Wand/MP/INT&Weapon/STR/DEX: ATK,
        #     HP/CON/Armor/DEX: DEF)
        pass
    
    def talk(inputlist):
        silvercount = s.median(inputlist)
        speak = ""
        speak += input(f"You ask the innkeeper for the latest news and"
                       f" gossip.\n'I'm just an old inkeeper, just a few"
                       f" lines of code,' the proprietor says with a "
                       f"smile. 'My da always said a choice bit o' news"
                       f" was worth a gallon of ale, and well, my pints"
                       f" run about ten coppers, twenty after the sun "
                       f"goes down. And some o' my news is worth a bit"
                       f" more, so I only take real silver pieces for "
                       f"my choicest bits.' You notice his hand slyly "
                       f"extending across the bar, palm up. 'My da was "
                       f"also known for saying code don't run for free.'"
                       f" He almost seems to be looking right past you."
                       f"\n'So what say ye? Worth it to ye, or not?'\n")
        if "no" in speak: print(f"'Fair enough, wise men know to keep "
                                f"to themselves and stack their coins, "
                                f"that much is true, sure and certain,'"
                                f" the innkeeper says, as much to himself"
                                f" as to you.")
        elif "y" in speak: print(f"The innkeeper watches as you take "
                                   f"one of your {silvercount} silver "
                                   f"pieces (now {silvercount-1}) from "
                                   f"your pouch and discreetly place it"
                                   f" in his hand, which quickly disappears"
                                   f" into the folds of his clothing.\n"
                                   f"'Here is some gossip--' he says, "
                                   f"leaning in close. 'I heard there "
                                   f"were fake heroes around these parts"
                                   f" who'll give real silver for fake"
                                   f" gossip. How's that?'\nYou notice "
                                   f"a certain hardness in the man's eyes"
                                   f" you didn't before. How exactly did"
                                   f" you end up at the Mothlight anyway?\n"
                                   f"Try as you might, you cannot recall.")
        
        else: print(f"'I'm going to take that as a no, city slicker. A "
                    f"bit o'wisdom for ye: if I think ye wise, best not"
                    f"act to change my stance.'")
        #      tavern() to exit? howmst?
        pass
    def leave(): print(f"You stand up and exit the inn. The sun is so "
                       f"bright you are blinded. You feel your armor "
                       f"and weapons are dissolving.\nYou realize with"
                       f" total horror that you are being erased from"
                       f" existence. BYE!")
            
    prompt = (f"Would you like to BUY something, start a BRAWL for money,"
              f"try to TALK, or LEAVE?")
    move += input(f"You are sitting in the Mothlight, {origin.title()}'s "
                  f"finest inn.\n{prompt}\n")
    if "brawl" in move.casefold():
        brawl()
    if "buy" in move.casefold():
        buy(gearlist)
    elif "talk" in move.casefold():
        talk(gearlist)
    elif "leave" in move.casefold():
        leave()
    else: tavern()
  
def main():
    intro()
    attr()
    gear(gearlist)
    tavern()    

main()