from os import scandir
import os
from os.path import splitext, exists, join
from shutil import move

# folder to track e.g.: "C:\\Users\\UserName\\Downloads"
src_dir = ""

# create a folder call 'dup' (to store all duplicates)
dup_dir = os.path.join(src_dir, "dup")


def check_name(name):
    file_name, file_extension = splitext(name)

    file_name_split = file_name.split(" ")

    print(file_name_split)

    name_dup = False

    if file_name_split[-1] == "(1)":
        name_dup = True

    return name_dup


def move_file(dest, entry, name):
    if exists(f"{dest}/{name}"):
        print(f"file '{name}' already exist!")
    else:
        new_file_dest = join(dest, name)
        move(entry, new_file_dest)


def main():
    with scandir(src_dir) as entries:
        for entry in entries:
            file_full_name = entry.name
            file_name_dup = check_name(name=file_full_name)
            # print(file_name_dup)
            if file_name_dup == True:
                move_file(dup_dir, entry, file_full_name)
                print("file has been moved!")

    print("\nFinish running!")


if __name__ == "__main__":
    main()
