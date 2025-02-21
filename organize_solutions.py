import os
import shutil

# Define root directory
root_dir = os.path.join(os.getcwd(), "COURSE_PRACTICE_QUESTIONS")

# Define ExampleSolutions directory
target_base = os.path.join(root_dir, "ExampleSolutions")

# Ensure ExampleSolutions directory exists
os.makedirs(target_base, exist_ok=True)

# Store files to move for dry run
files_to_move = []

# Walk through COURSE_PRACTICE_QUESTIONS directory
for root, _, files in os.walk(root_dir):
    # Skip ExampleSolutions folder itself
    if root.startswith(target_base):
        continue

    for file in files:
        if "example" in file and file.endswith(".py"):  # Match example.py files
            relative_root = os.path.relpath(root, root_dir)  # Get relative path
            path_parts = relative_root.split(os.sep)  # Split into folder structure

            # Extract chapter name
            chapter_name = path_parts[0]

            # If there's a deeper folder (e.g., question1, question2), use it
            subfolder_name = path_parts[1] if len(path_parts) > 1 else ""

            # Define new destination path
            target_folder = os.path.join(target_base, chapter_name, subfolder_name)
            source_path = os.path.join(root, file)
            target_path = os.path.join(target_folder, file)

            # Store relative paths for dry run
            rel_source = os.path.relpath(source_path, root_dir)
            rel_target = os.path.relpath(target_path, root_dir)
            files_to_move.append((rel_source, rel_target))

# Dry run - preview moves
print("Dry Run - Files to Move:")
for src, dst in files_to_move:
    print(f"{src} -> {dst}")

# Ask for confirmation
confirm = input("\nProceed with file move? (yes/no): ").strip().lower()

if confirm == "yes":
    for src, dst in files_to_move:
        full_src = os.path.join(root_dir, src)
        full_dst = os.path.join(root_dir, dst)

        os.makedirs(os.path.dirname(full_dst), exist_ok=True)  # Create necessary folders
        shutil.move(full_src, full_dst)
        print(f"Moved: {src} -> {dst}")
else:
    print("Operation canceled.")
