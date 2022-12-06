
def print_line():
    print("-" * 13)

def print_tab(tab):
    print_line()
    for i in range(3):
        print ("|", tab[6-i*3], "|", tab[7-i*3], "|", tab[8-i*3], "|")
        print_line()