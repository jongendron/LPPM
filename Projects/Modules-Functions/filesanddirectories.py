# Modules, functions, and classes create scopes!
import os


# Create custom walk function w/ recursion
def list_dir(s):
    
    def dir_list(d):
        #global tab_stop  # checks global scope (doesn't work)
        nonlocal tab_stop # checks in enclosing scope/function but not local or global (&no declarations)
        files = os.listdir(d)
        for f in files:
            current_dir = os.path.join(d, f) # put directory w/ file
            if os.path.isdir(current_dir):
                print("\t" * tab_stop + "Directory: " + f)
                tab_stop += 1
                dir_list(current_dir)
                tab_stop -= 1
            else:
                print("\t" * tab_stop + f)
    
    tab_stop = 0
    if os.path.exists(s):
        print("Directory listing: " + s)
        dir_list(s)
    else:
        print(s + " does not exist")

# Test our walk() function
list_dir('.')

# Testing OS.walk()
# listing = os.walk('.')
# for root, directories, files in listing:
#     print(root)
#     for d in directories:
#         print('\t', d)
#     for f in files:
#         print('\t', f)

