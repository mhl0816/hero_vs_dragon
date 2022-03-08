import random
# import random is a simple library that implements the random number generator behavior

# please read into the variables below the correct numbers. Use try and except to catch error.
# a simple example would be:
# hero_hp = int(input("how many hp does the hero have?"))
try:
    hero_hp = int(input("how much hp does the hero have?"))
    print("hero_hp is", hero_hp)
except ValueError:
    print("that is not a number try again")
try:
    dragon_hp = int(input("how much hp does the dragon have?"))
    print("dragon_hp is", dragon_hp)
except ValueError:
    print("that is not a number try again")
try:
    hero_max_dmg = int(input("what is the hero_max_dmg?"))
    print("the hero_max_dmg is", hero_max_dmg)
except ValueError:
    print("that is not a number try again")
try:
    dragon_max_dmg = int(input("what is the dragon_max_dmg?"))
    print("the dragon_max_dmg is", dragon_max_dmg)
except ValueError:
    print("that is not a number try again")
finally:
    print("The dragon with", dragon_hp, "hp attacks out hero with", hero_hp, "hp")

# add a While for an infinite block
# here goes the while:
while True:
    dragon_attack = random.randint(1, dragon_max_dmg)
    # here you need to update the hero hp, you need to subtract the damage that the dragon did
    # add code on this line
    hero_hp = hero_hp - dragon_attack
    print("The dragon does", dragon_attack, "damage and the hero has", hero_hp, "hp left")
    # add an if condition to check if the hero was killed by the dragon
    # here goes the if
    if hero_hp <= 0:
        print("Unfortunately the dragon killed our hero. RIP sir Bravealot")
        break
    hero_attack = random.randint(1, hero_max_dmg)
    # here you need to update the dragon hp, you need to subtract the damage that the hero did
    # add code on this line
    dragon_hp = dragon_hp - hero_attack
    print("The hero does", hero_attack, "damage and the dragon has", dragon_hp, "hp left")
    # add an if condition to check if the dragon was killed by the hero
    # here goes the if
    if dragon_hp <= 0:
        print("Our valiant hero has slain the dragon!")
        break

    input("Round over. Press any key")
