# Author: StevenChaoo
# -*- coding:UTF-8 -*-


import os
import colorama as c


paper_path = "./"
paper_idx_dict = {}
while True:
    print(c.Fore.BLUE)
    search_str = input("\nPlease enter command (MODE + KEY WORDS): ")
    search_str_list = search_str.strip().split()
    mode = search_str_list[0]
    print(c.Style.RESET_ALL)
    if mode == "s":
        key_words = " ".join(search_str_list[1:])
        count = 0
        files = os.listdir(paper_path)
        for file_name in files:
            lower_file_name = file_name.lower()
            if key_words in lower_file_name:
                count += 1
                paper_idx_dict[count] = file_name
                print("{}. {}".format(count, file_name))
    elif mode == "o":
        idx = int(search_str_list[-1])
        paper_name = paper_idx_dict[idx]
        paper_name_list = paper_name.strip().split()
        paper_name = "\ ".join(paper_name_list)
        os.system("open ./{}".format(paper_name))
        print(c.Fore.GREEN)
        print("Opened {}".format(paper_name))
