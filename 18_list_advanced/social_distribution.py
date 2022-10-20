"""
On the first line, you will be given the population
(numbers separated by comma and space ", ").
On the second line, you will be given the minimum wealth.
You should distribute the wealth so that no part of the population has less than
the minimum wealth. To do that, you should always take wealth from the wealthiest
part of the population.
There will be cases where the distribution will not be possible.
In that case, print: "No equal distribution possible".
"""


def deficit(lst_pop, min_v):
    # check if there is enough extra wellness to cover poor min threshold
    poor = 0
    for i in lst_pop:
        if i < min_v:
            poor += (min_v - i)
    return poor


def welnes(lst_pop, min_v):
    welt = 0
    for j in lst_pop:
        if j > min_v:
            welt += (j - min_v)
    return welt


def distribution(lst_pop, min_v):
    while any(i < min_v for i in lst_pop):
        for j in range(len(lst_pop) - 1):
            wealthiest_index = lst_pop.index(max(lst_pop))  # look for the richest
            if lst_pop[j] < min_v:
                delta = min_v - lst_pop[j]
                if lst_pop[wealthiest_index] - min_v >= delta:
                    lst_pop[j] += delta  # give to poorest
                    lst_pop[wealthiest_index] -= delta  # take from CURRENTLY RICHEST
                else:
                    delta_richest = lst_pop[wealthiest_index] - min_v
                    lst_pop[j] += delta_richest
                    lst_pop[wealthiest_index] -= delta_richest
    return lst_pop


population = list(map(int, input().split(', ')))
min_value = int(input())

under_wellnes = deficit(population, min_value)
plus_wellnes = welnes(population, min_value)
if under_wellnes > plus_wellnes:
    print("No equal distribution possible")
else:
    population = distribution(population, min_value)
    print(population)
