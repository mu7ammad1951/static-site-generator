import textnode
import os
import shutil

def generate(source_path, destination_path):
    if os.path.exists(destination_path):
        shutil.rmtree(destination_path)
    os.mkdir(destination_path)    
    dir_contents = os.listdir(source_path)
    for file in dir_contents:
        file_path = os.path.join(source_path, file)
        if os.path.isfile(file_path):
            shutil.copy(file_path, destination_path)
        else:
            generate(file_path, os.path.join(destination_path, file))


def main():
    generate("./static", "./public")
    node_1 = textnode.TextNode("This is a text node", "bold")
    node_2 = textnode.TextNode("This is a text node", "italic", "https://www.boot.dev")

    print(f"{node_1} is equal to {node_2}: {node_1 == node_2}")
    
    
if __name__ == '__main__':
    main()