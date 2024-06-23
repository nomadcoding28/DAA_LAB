# import matplotlib.pyplot as plt
# import numpy as np

# def f(n):
#     return 7*n**2+n+5
# def g(n):
#     return n**2
# c1=8
# c2=7

# n_value=np.arange(1,11,1)

# f_values=f(n_value)
# c1g_values=c1*g(n_value)
# c2g_values=c2*g(n_value)

# n0=np.min(n_value[(f_values<=c1g_values)&(c2g_values<=f_values)])


# print(n0)
# print(f_values)
# print(c1g_values)
# print(c2g_values)

# plt.plot(n_value,f_values,label="f(n)=7n^2+n+5")
# plt.plot(n_value,c1g_values,label="c1g(n)=8n^2")
# plt.plot(n_value,c2g_values,label="c2g(n)=7n^2")
# plt.axvline(x=n0,color="r",linestyle="--",label=f'n0 = {n0}')
# plt.xlabel("n")
# plt.ylabel("value")
# plt.title("comp b/w fn,c1gn,c2gn")
# plt.legend()
# plt.grid(True)
# plt.show()


def gale_sharply(men_preferences, woman_preferences):
    # all men and women are free
    free_men = list(men_preferences.keys())
    engagments = {}

    while free_men:
        man = free_men.pop(0)
        man_preference = men_preferences[man]

        woman = man_preference.pop(0)
        fiance = engagments.get(woman)

        if not fiance:
            engagments[man] = woman
        else:
            if woman_preferences[woman].index(man) < woman_preferences[woman].index(
                fiance
            ):
                engagments[man] = woman
                free_men.append(fiance)

            else:
                free_men.append(man)
    return engagments


men_preferences = {
    "m1": ["w1", "w2", "w3"],
    "m2": ["w2", "w3", "w1"],
    "m3": ["w3", "w1", "w2"],
}
woman_preferences = {
    "w1": ["m2", "m3", "m1"],
    "w2": ["m1", "m2", "m3"],
    "w3": ["m1", "m3", "m2"],
}
list = gale_sharply(men_preferences, woman_preferences)
print("gale_sharply stable matching algo")
for man, woman in list.items():
    print(f"{man} is engaged to {woman}")
