import random

DICE_ART = {
    1: ("┌─────────┐", "│         │", "│    ●    │", "│         │", "└─────────┘"),
    2: ("┌─────────┐", "│  ●      │", "│         │", "│      ●  │", "└─────────┘"),
    3: ("┌─────────┐", "│  ●      │", "│    ●    │", "│      ●  │", "└─────────┘"),
    4: ("┌─────────┐", "│  ●   ●  │", "│         │", "│  ●   ●  │", "└─────────┘"),
    5: ("┌─────────┐", "│  ●   ●  │", "│    ●    │", "│  ●   ●  │", "└─────────┘"),
    6: ("┌─────────┐", "│  ●   ●  │", "│  ●   ●  │", "│  ●   ●  │", "└─────────┘"),
}
DIE_HEIGHT = len(DICE_ART[1])
DIE_FACE_SEPARATOR = " "

def parse_input(input_string):
    """Validate the user's input."""
    if input_string.strip().isdigit():
        return int(input_string)
    else:
        print("Invalid input. Please enter a number between 1 and 6.")
        raise SystemExit(1)

def roll_dice(num_dice):
    """Roll the specified number of dice."""
    return [random.randint(1, 6) for _ in range(num_dice)]

def generate_dice_faces_diagram(dice_values):
    """Generate a diagram of the dice faces."""
    dice_faces = [DICE_ART[value] for value in dice_values]
    dice_faces_rows = [
        DIE_FACE_SEPARATOR.join(die[row_idx] for die in dice_faces)
        for row_idx in range(DIE_HEIGHT)
    ]
    width = len(dice_faces_rows[0])
    diagram_header = " RESULTS ".center(width, "~")
    return "\n".join([diagram_header] + dice_faces_rows)

num_dice_input = input("How many dice would you like to roll? ")
num_dice = parse_input(num_dice_input)
roll_result = roll_dice(num_dice)
dice_face = generate_dice_faces_diagram(roll_result)
print(f"Roll result: {dice_face}")