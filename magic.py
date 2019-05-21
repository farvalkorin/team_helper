import pandas as filemagic

from itertools import product as cartesian_product

from tqdm import tqdm

df = filemagic.read_csv('input.csv')
tupes = [tuple(x) for x in df.values]

p = cartesian_product(tupes, tupes, tupes, tupes, tupes, tupes)

def magicNumber1(p):
    for batch in p:
        ((player1, sr1, position1), (player2, sr2, position2),
         (player3, sr3, position3), (player4, sr4, position4),
         (player5, sr5, position5), (player6, sr6, position6)) = batch
        players = set()
        positions = set()
        sr_sum = 0
        for player, sr, position in batch:
            if player in players:
                continue
            if position in positions:
                continue
            positions.add(position)
            players.add(player)
            sr_sum = sr_sum + sr

        if sr_sum > 17600:
            continue

        yield sr_sum, tuple(sorted(list(players))), sorted(list(positions))

def magicNumber2(p):
    another_set = set()
    for sr_sum, sorted_list_of_players, positions_covered in p:
        if sorted_list_of_players in another_set:
            continue
        if len(sorted_list_of_players) != 6:
            continue
        another_set.add(sorted_list_of_players)
        yield sr_sum, sorted_list_of_players


print('SR    : Team Members')
for set_ in sorted(magicNumber2(tqdm(magicNumber1(p))), reverse=True):
    team_sr, sorted_players = set_
    print('% 5d: %s' % (team_sr, ', '.join(sorted_players)))

