print("Nikhil N,USN:1AY24AI075,SEC:O")
import random
DICE = {
    'green':   ['brain', 'brain', 'brain', 'footsteps', 'footsteps', 'shotgun'],
    'yellow':  ['brain', 'brain', 'footsteps', 'footsteps', 'shotgun', 'shotgun'],
    'red':     ['brain', 'footsteps', 'footsteps', 'shotgun', 'shotgun', 'shotgun']
}

def roll_die(color):
    return random.choice(DICE[color])

def draw_dice(bag, n):
    dice = []
    for _ in range(n):
        if bag:
            die = random.choice(bag)
            bag.remove(die)
            dice.append(die)
    return dice

def bot_decide(brains, shotguns):
    return shotguns < 2 and brains < 2

def play_turn(name):
    bag = ['green']*6 + ['yellow']*4 + ['red']*3
    brains, shotguns, footprints = 0, 0, []
    while True:
        dice_to_roll = footprints + draw_dice(bag, 3 - len(footprints))
        footprints = []
        for d in dice_to_roll:
            face = roll_die(d)
            if face == 'brain':
                brains += 1
            elif face == 'shotgun':
                shotguns += 1
            else:
                footprints.append(d)
        if shotguns >= 3 or not bot_decide(brains, shotguns):
            return 0 if shotguns >=3 else brains

def game():
    scores = {'Bot1':0, 'Bot2':0}
    while True:
        for bot in scores:
            gained = play_turn(bot)
            scores[bot] += gained
            print(f"{bot}: +{gained} brains (total {scores[bot]})")
            if scores[bot] >= 13:
                print(f"{bot} wins!")
                return

game()








