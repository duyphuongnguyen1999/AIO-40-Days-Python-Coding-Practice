import matplotlib.pyplot as plt
import os


def read_code_from_file(file_path):
    with open(file_path, "r") as file:
        code = file.read()
    return code


def save_code_as_image(code, output_path):
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.text(0.5, 0.5, code, fontsize=12, ha="left", va="center")
    ax.axis("off")
    plt.savefig(output_path, bbox_inches="tight", pad_inches=0.1)


# Get current path
current_file_path = os.path.abspath(__file__)
# Get current
current_dir = os.path.dirname(current_file_path)

# Read code from file
code_file_name = "file_name.py"
code_file_path = os.path.join(current_dir, code_file_name)
code = read_code_from_file(code_file_path)

# Save code
output_path = os.path.join(current_dir, "file_name_code.png")
save_code_as_image(code, output_path)
