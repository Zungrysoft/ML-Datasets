import random

with open("./dominion_cards_raw.txt", 'r') as file:
    text = file.read()

replacements = [
    ["–", "-"],
    ["ΓÇô", "-"],
    ["â€“", "-"],
    ["{{Cost|1}}", "$1"],
    ["&nbsp;", " "],
    ["&ldquo;", "\""],
    ["{{nowrap", ""],
    ["'''", ""],
    [".<br>", ". "],
    ["<br>", ". "],
    [".<br />", ". "],
    ["<br />", ". "],
    ["<p>", ""],
    ["</p>", " "],
    ["{{VP|", "VP"],
    ["{{VP", "VP"],
    ["{{Divline}}", " | "],
    ["{{divline}}", " | "],
    ["{{Cost|", "$"],
    ["{{cost|", "$"],
    ["{{Cost", "$"],
    ["{{cost", "$"],
    ["|l}}", ""],
    ["|L}}", ""],
    ["}}", ""],
]

def parse_card(card):
    sections = card.split(" || ")
    
    # Name
    name = sections[0].split("|")[1][:-2]

    # Type
    type = sections[2].replace("Â ", "")

    # Cost
    if "Cost" in sections[3]:
        cost = "$" + sections[3].split("Cost")[1][1:-2]
    else:
        cost = "$0"
    
    # Effect
    effect = sections[4]
    for r in replacements:
        effect = effect.replace(r[0], r[1])
        pass

    return f"Name: {name}, Type: {type}, Cost: {cost}, Effect: {effect}"

card_list = text.split("\n|-\n|")
formatted_card_list = []
for card in card_list:
    card_string = parse_card(card)
    formatted_card_list.append(card_string)

random.shuffle(formatted_card_list)

for card in formatted_card_list:
    print(card)
    pass