import random

RIGHT_RESULTS = [
"زوجين",
"متتالية",
"ثلاثة",
"فل هاوس",
"اربعة"
]

LEFT_RESULTS = [
"زوج",
"متتالية نفس النوع",
"AA",
"زوج و متتالية",
"لاشيء"
]


def monte_carlo_simulation(iterations=1000):

    results = {}

    for r in RIGHT_RESULTS:
        results[r] = 0

    for _ in range(iterations):

        move = random.choice(RIGHT_RESULTS)

        results[move] += 1

    best = max(results, key=results.get)

    probability = round((results[best] / iterations) * 100, 2)

    return best, probability
