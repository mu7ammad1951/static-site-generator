import textnode
import os
import shutil
from block_text_functions import copy_static, generate_page_recursive



def main():
    copy_static("./static", "./public")
    generate_page_recursive("./content", "./template.html", "./public")
    
    
if __name__ == '__main__':
    main()