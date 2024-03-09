import numpy as np
import matplotlib.pyplot as plt

n = 100

def sign(x):
    if x >= 0:
        return 1
    else:
        return -1
# generate a random pattern
def generate_pattern():
    x = np.random.choice([-1, 1], size=(n))
    return x

# applying dot product to network
def imprint_patterns(pattern):
    weights = np.zeros((n, n))
    for p in pattern:
        for i in range(n):
            for j in range(n):
                if i != j:
                    weights[i][j] += p[i] * p[j]
                # weights[j][i] += p[i] * p[j]

    weights /= n
    np.fill_diagonal(weights, 0)
    return weights
# checking stability of each imprint
def is_stable(weights, pattern):
    num_stable, num_unstable = 0, 0
    pp =0
    for p in range(len(pattern)):
   
        patterns = pattern[p].copy()
        for i in range(n):
            h = np.sum(weights[i, :] * patterns)
            patterns[i] = sign(h)
        if np.array_equal(pattern[p], patterns):
            num_stable += 1
        else:
            num_unstable += 1

   
    return num_stable  , num_unstable / len(pattern)

#run the experiment 
def run(num_patterns=50):
    unstable_fractions, stable_fractions = [], []
    for i in range(1, num_patterns +1 ):
        patterns = [generate_pattern() for _ in range(i)]
        weights = imprint_patterns(patterns)
        stable_prob, unstable_prob = is_stable(weights, patterns)
        stable_fractions.append(stable_prob)
        unstable_fractions.append(unstable_prob)
    return unstable_fractions, stable_fractions

all_unstable_fractions = [[] for _ in range(5)]
all_stable_fractions = [[] for _ in range(5)]

for i in range(5):
    unstable_fractions, stable_fractions = run(50)
    for j in unstable_fractions:
        all_unstable_fractions[i].append(j)
    for j in stable_fractions:
        all_stable_fractions[i].append(j)




# graphing 
plt.figure(figsize=(10, 5))
for i in range(5):
    plt.plot(range(1, 51), all_stable_fractions[i], label=f'Experiment {i+1}')

plt.xlabel('Number of Imprints')
plt.ylabel('Number of Stable Imprints')
plt.title('Stable Imprints vs Number of Imprint')
plt.legend()
plt.show()

plt.figure(figsize=(10, 5))
for i in range(5):
    plt.plot(range(1, 51), all_unstable_fractions[i], label=f'Experiment {i+1}')

plt.xlabel('Number of Imprints (p)')
plt.ylabel('Fraction of Unstable Imprints')
plt.title('Unstable Fraction vs Number of Imprint')
plt.legend()
plt.show()

avg_unstable = np.mean(all_unstable_fractions, axis=0)
std_unstable = np.std(all_unstable_fractions, axis=0)

avg_stable = np.mean(all_stable_fractions, axis= 0)
std_stable = np.std(all_stable_fractions, axis= 0)

plt.figure(figsize=(10, 5))
plt.plot(range(1, 50 + 1), avg_unstable, label="Average")
plt.fill_between(range(1, 50 + 1), avg_unstable + std_unstable, avg_unstable - std_unstable, alpha=0.2, label="Standard Deviation")

plt.xlabel("Number of Imprints (p)")
plt.ylabel("Fraction of Unstable Imprints")
plt.title("Average Fraction of Unstable Imprints with Standard Deviation")
plt.legend()
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(range(1, 50 + 1), avg_stable, label="Average")
plt.fill_between(range(1, 50 + 1), avg_stable + std_stable, avg_stable - std_stable, alpha=0.2, label="Standard Deviation")

plt.xlabel("Number of Imprints (p)")
plt.ylabel("Number of Stable Imprints")
plt.title("Average number of Stable Imprints with Standard Deviation")
plt.legend()
plt.show()
