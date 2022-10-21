#!/usr/bin/env python3

import os 

class Tree:
    class Node:
        def __init__(self, data):
            self.children = []
            self.data = data
        def get_children(self, node):
            return self.children
   
    def __init__(self, root_node):
        self.root = root_node

    def get_root(self):
        return root

def check_file_standard(path):
    # Add a thing that logs links like [location|name_here] so that everytime you see name_here without a link you suggest updating it.
    # So like if you see [group_theory/groups#defition of group | group] in some file, then if you see somewhere else a sentence that says:
    # "We can see this is in fact a group", then you suggest changing "group" to "[group_theory/groups#group]".
    # You should only replace the first mention of the words in the block. If in one block the same thing is used twice, only suggest that the first one be changed.



def main():
    print("main") 
    given_path = "/home/loris/Obsidian-notes/Topic_Notes"
    for path, dirs, files in os.walk(given_path):
        print(path)
        for f in files:
            print(f)

if (__name__ == "__main__"):
    main()
