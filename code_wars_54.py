from math import ceil

def movie(card, ticket, perc):
    system_a = 0
    system_b = card
    n = 0

    while ceil(system_b) >= system_a:
        n += 1
        system_a += ticket
        system_b += ticket * perc ** n

    return n