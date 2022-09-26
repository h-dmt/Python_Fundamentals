# As a young adventurer, you travel with your group worldwide,
# seeking for gold and glory. But you need to split the profit
# among your companions.
# You will receive a group size. After that, you receive the days of the adventure.
# Every day, you earn 50 coins, but you also spend 2 coins per companion for food.
# Every 3rd (third) day, you organize a motivational party,
# spending 3 coins per companion for drinking water.
# Every 5th (fifth) day, you slay a boss monster and gain 20 coins per companion.
# But if you have a motivational party the same day, you spend additional
# 2 coins per companion.
# Every 10th (tenth) day at the start of the day, 2 (two) of your companions leave,
# but every 15th (fifteenth) day 5 (five) new companions are joined
# at the beginning of the day.
# You should calculate how many coins gets each companion
# at the end of the adventure.

group_size = int(input())
days = int(input())
companions_count = group_size
coins = 0
count_day = 0

for count_day in range(1, days + 1):

    if count_day % 10 == 0:
        companions_count -= 2
    if count_day % 15 == 0:
        companions_count += 5
    if count_day % 3 == 0:
        coins -= 3 * companions_count
    if count_day % 5 == 0:
        coins += 20 * companions_count
        if count_day % 3 == 0:
            coins -= 2 * companions_count

    coins += 50
    coins -= 2 * companions_count

print(f'{companions_count} companions received {int(coins / companions_count)} coins each.')
