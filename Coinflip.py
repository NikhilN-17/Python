#coinflip
print("Nikhil N,USN:1AY24AI075,SEC:O")
import random
def coin_flip_streaks():
    flips = [random.choice(['H', 'T']) for _ in range(100)]
    streak_count = 0
    current_streak = 1

    for i in range(1, len(flips)):
        if flips[i] == flips[i - 1]:
            current_streak += 1
            if current_streak == 6:
                streak_count += 1
        else:
            current_streak = 1

    print(f"Flipped 100 coins.")
    print(f"Streaks of 6 in a row found: {streak_count}")
coin_flip_streaks()
