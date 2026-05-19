import json
import os

FILE_NAME = "data/game_stats.json"

def update_stats(player_name, won):

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as f:
            stats = json.load(f)
    else:
        stats = {}

    if player_name in stats:

        stats[player_name]["matches"] += 1
        if won:
            stats[player_name]["wins"] += 1
        else:
            stats[player_name]["losses"] += 1
    else:
        stats[player_name] = {
            "matches": 1,
            "wins": 1 if won else 0,
            "losses": 0 if won else 1
        }

    # 3. نحفظ البيانات تاني في الملف
    with open(FILE_NAME, 'w') as f:
        json.dump(stats, f, indent=4)