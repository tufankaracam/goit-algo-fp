import random
import matplotlib.pyplot as plt


def simulate_dice_throws(n_throws):
    counts = {sum: 0 for sum in range(2, 13)}

    for _ in range(n_throws):
        sum = random.randint(1, 6) + random.randint(1, 6)
        counts[sum] += 1

    probabilities = {sum: counts[sum] / n_throws for sum in counts}

    return probabilities


def display_results(probabilities):

    sums, probs = zip(*sorted(probabilities.items()))

    plt.bar(sums, probs)
    plt.xlabel('Sum')
    plt.ylabel('Probability')
    plt.title('Probability Distribution of Dice Sums')
    plt.xticks(range(2, 13))
    plt.show()

    print("Sum\tProbability")
    for sum, prob in sorted(probabilities.items()):
        print(f"{sum}\t{prob:.4f} ({prob*100:.2f}%)")


n_throws = 1000000
probabilities = simulate_dice_throws(n_throws)
display_results(probabilities)
