def make_pizza(*topings):
    print(topings)   # tuple
    for topin in topings:
        print(topin)

pramod = make_pizza("tomato")
bhargav =  make_pizza("Olives", "mushroom", "paneer")