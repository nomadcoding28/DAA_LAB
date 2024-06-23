def galesharply(men_preference,women_preference):
    free_men=list(men_preference.keys())
    engagments={}
    while free_men:
        man=free_men.pop(0)
        man_preference=men_preference[man]
        woman=man_preference.pop(0)
        fiance=engagments.get(woman)
        if not fiance:
            engagments[woman]=man
        else:
            if women_preference[woman].index(man)<women_preference[woman].index(fiance):
                engagments[woman]=man
                free_men.append(fiance)
            else:
                free_men.append(man)
    return engagments
def generate_men_preferences():
    men_preferences = {}
    n_m=int(input("enter the number of men :"))
    for _ in range(n_m):
        m=input("enter the manid: ")
        men_preferences[m]=[]
        n_w=int(input("enter the number of women for this man :"))
        for _ in range(n_w):
            w=input("enter the womenid: ")
            men_preferences[m].append(w)
    return men_preferences
def generate_women_preferences():
    women_preferences = {}
    n_wm=int(input("enter the number of women :"))
    for _ in range(n_wm):
        w=input("enter the womanid: ")
        women_preferences[w]=[]
        n_m=int(input("enter the number of men for this woman :"))
        for _ in range(n_m):
            m=input("enter the manid: ")
            women_preferences[w].append(m)
    return women_preferences
men_preferences=generate_men_preferences()
women_preferences=generate_women_preferences()
list=galesharply(men_preferences,women_preferences)
for man, woman in list.items():
    print(f"{man} is engaged to {woman}")



