import textnode
import os
import shutil

def generate():
    path = "../public"
    if (os.path.exists(path)):
        shutil.rmtree(path)
def main():
    node_1 = textnode.TextNode("This is a text node", "bold")
    node_2 = textnode.TextNode("This is a text node", "italic", "https://www.boot.dev")

    print(f"{node_1} is equal to {node_2}: {node_1 == node_2}")
    
    
if __name__ == '__main__':
    main()