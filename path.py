import os, shutil

os.chdir("/home/aabayomi/Downloads")
# os.listdir()
folder_path = os.getcwd()
# os.remove("kdeconnect-kde-release_25.04-5109-windows-cl-msvc2022-x86_64.exe")
# print(os.uname())


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_squared_list = [numb * numb for numb in my_list]
my_even_list = [numb for numb in my_list if numb % 2 == 0]
# print(my_even_list)

names = ["abayomi", "dolapo", "tolulope", "oreoluwa", "ishola", "darasimi"]
positions = ["first", "second", "third", "forth", "fifth", "sixth", "seventh"]

children = [{names[n]: positions[n]} for n in range(len(positions))]
print(children)