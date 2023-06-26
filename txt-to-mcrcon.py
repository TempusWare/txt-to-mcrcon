from mcrcon import MCRcon
from watchfiles import watch
from config import CONFIG_INFO
import json
import random

mobs = json.load(open("./data/mobs.json", "r"))
entities = json.load(open("./data/entities.json", "r"))

inputPath = "./readfromme.txt"
player = CONFIG_INFO["playerName"]


def getRandomMob(type):
    list = mobs if type == "mob" or type == "mobs" else entities
    rand = random.randint(0, len(list) - 1)
    return list[rand]


def getTellRaw(message, colour="white"):
    return 'tellraw @a {"text": "%s", "color": "%s"}' % (message, colour)


def getTitle(message, colour="white", location="title"):
    return 'title @a %s {"text": "%s", "color": "%s"}' % (location, message, colour)


def getSubtitle(message, colour="white", location="subtitle"):
    return 'title @a %s {"text": "%s", "color": "%s"}' % (location, message, colour)


print("Running")

text = ""
for changes in watch(inputPath):
    with open(inputPath, "r") as reader:
        input = reader.read()
    print("File updated. File reads: {}".format(input))

    if text == input:
        continue
    text = input
    if len(text) < 1 or "|" not in text:
        continue

    with open(inputPath, "w") as writer:
        writer.write("")
    print("File wiped.")

    trigger, action = input.strip().split("|")
    print(f"Input updated. trigger: {trigger}, action: {action}")

    commands = []

    commands.append(getTellRaw(f"{player} said {trigger}", "gray"))

    validAction = True

    match action:
        case "kill":
            commands.append(f"kill {player}")
        case "mob" | "entity":
            mob = getRandomMob(trigger)
            commands.append(f"spawnmob {mob} 1 {player}")
            commands.append(getTellRaw(f"Spawning {mob}", "blue"))
        case "mobs" | "entities":
            mob = getRandomMob(trigger)
            amount = random.randint(1, 10)
            plural = "s" if amount > 1 else ""
            commands.append(f"spawnmob {mob} {amount} {player}")
            commands.append(getTellRaw(f"Spawning {amount} {mob}{plural}", "blue"))
        case "bees":
            mob = "bee"
            amount = 36
            commands.append(f"spawnmob {mob} {amount} {player}")
            commands.append(getTellRaw(f"Spawning {amount} {mob}s", "yellow"))
        case _:
            validAction = False

    if not validAction:
        print("Not a valid action: {}".format(action))
        continue

    with MCRcon(CONFIG_INFO["serverIP"], CONFIG_INFO["rconPassword"]) as mcr:
        for cmd in commands:
            response = mcr.command(cmd)
            print(response)
