### HSR Artifact Rater Main Script ###
### Author: Stone Provo ###

### Imports ###
import os
import json
### Imports ###

def load_char_data(filepath="data/characters.json"):
    with open(filepath, "r") as file:
        return json.load(file)

# Function to rate relics based on character priorities
def rate_relic(rPiece, rSet, mainStat, subStats, character_data):
    # Initialize leaderboard with a placeholder
    leaderboard = [{"character": "None", "score": 0}]

    # Iterate over each character
    for char_name, char_info in character_data.items():
        score = 0

        # Check main stat priority
        main_stat_priority = char_info.get("stat_priority", {}).get(mainStat, 0)
        score += (main_stat_priority * 3)

        # Check substat priorities
        substat_priority = sum(char_info.get("stat_priority", {}).get(substat, 0) for substat in subStats)
        score += substat_priority

        # Check relic set priority
        for relic in char_info.get("best_relics", []):
            if relic.get("set_name") == rSet:
                score += relic.get("priority", 0)

        # Check planar ornament priority
        for relic in char_info.get("best_ornaments", []):
            if relic.get("set_name") == rSet:
                score += relic.get("priority", 0)

        # Update the leaderboard
        for i, entry in enumerate(leaderboard):
            if score > entry["score"]:
                leaderboard.insert(i, {
                    "character": char_name,
                    "image": char_info.get("image", ""),
                    "score": score,
                    "tier": get_tier(score),
                    "color": char_info.get("color", "#000000") # Default to White
                })
                break
    
    # Remove the placeholder
    leaderboard.remove({"character": "None", "score": 0})
    return leaderboard

def get_tier(score):
    if score == 26:
        return "S++ Tier"
    elif score == 25:
        return "S+ Tier"
    elif score == 24:
        return "S Tier"
    elif 20 <= score <= 23:
        return "A Tier"
    elif 15 <= score < 20:
        return "B Tier"
    elif 10 <= score < 15:
        return "C Tier"
    else:
        return "D Tier"
