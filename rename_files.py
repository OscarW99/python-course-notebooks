import os
import re
from pathlib import Path

# Configuration
chapter_num = 13 #* Changing to
chapter_abbr = "EXEC" #* Changing to
dry_run = False  # Set to False to actually rename files
# dry_run = True 

# Root directory to start from
root_dir = "./Chapter12"  # Update this path as needed

def get_new_filename(old_name, subdir_name):
    """Generate new filename based on the naming convention"""
    # Extract question number from directory name
    match = re.search(r'chapter12\.(\d+)', subdir_name)
    if match:
        question_num = int(match.group(1))
    elif "EndOfChapterProblemSet" in subdir_name:
        question_num = "eoc"  # End of chapter
    else:
        return old_name  # Unable to determine question number
        
    # Determine file type
    if old_name == "instructions.coursemd":
        file_type = "instructions"
        ext = "coursemd"
    elif old_name == "solutions.py":
        file_type = "solution"
        ext = "py"
    elif old_name == "example_solutions.py":
        file_type = "example"
        ext = "py"
    else:
        return old_name  # Not a file we want to rename
    
    # Format question number with leading zeros
    if question_num == "eoc":
        question_str = "eoc"
    else:
        question_str = f"{question_num:02d}"
        
    # Create new filename
    return f"ch{chapter_num:02d}_{chapter_abbr.lower()}_{question_str}_{file_type}.{ext}"

def main():
    """Main function to process files"""
    changes = []
    
    # Walk through the directory structure
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Skip the original_notebooks directory
        if "origional_notebooks" in dirpath:
            continue
            
        subdir_name = os.path.basename(dirpath)
        
        for filename in filenames:
            if filename in ["instructions.coursemd", "solutions.py", "example_solutions.py"]:
                old_path = os.path.join(dirpath, filename)
                new_filename = get_new_filename(filename, subdir_name)
                new_path = os.path.join(dirpath, new_filename)
                
                changes.append((old_path, new_path))
    
    # Display the changes with full paths
    print(f"Found {len(changes)} files to rename:")
    for old, new in changes:
        print(f"  {old} -> {new}")
    
    # Perform the renaming if not in dry run mode
    if not dry_run and changes:
        proceed = input("\nDo you want to proceed with these changes? (y/n): ")
        if proceed.lower() == 'y':
            for old_path, new_path in changes:
                os.rename(old_path, new_path)
            print(f"Renamed {len(changes)} files successfully.")
        else:
            print("Operation cancelled.")
    elif dry_run:
        print("\nThis was a dry run. No files were renamed.")
        print("Set dry_run = False in the script to make actual changes.")

if __name__ == "__main__":
    main()