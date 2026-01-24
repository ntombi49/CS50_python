import inflect
p=inflect.engine()

names=[]

while True:
    try:
        name=input("Name: ").title().strip()
        #when control +D is pressed
    except EOFError:
        print()
        break
    #add to the names list
    else:
        names.append(name)
#
print(f"Adieu, adieu, to {p.join(names)}")



