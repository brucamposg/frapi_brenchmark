import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def min_max(arr):
    min = arr[0]
    max = arr[0]

    for num in arr:
        if num < min:
            min = num
        elif num > max:
            max = num
    return min, max

def normalize(arr):
    min, max = min_max(arr)

    res = []
    for num in arr:
        res.append((num - min) / (max - min))

    return res


matched_scores_arr = np.loadtxt('similarity_matched.txt')
mismatched_scores_arr = np.loadtxt('similarity_mismatched.txt')

x_frr = []
y_frr = []

cp = len(matched_scores_arr) 

for x in range(20, 101):
    fn = 0
    for score in matched_scores_arr:
        if score < x:
            fn += 1

    tp = cp - fn
    fnr = fn / cp

    frr = fnr * fn / (tp + fn)
    x_frr.append(x)
    y_frr.append(frr)

#plt.plot(x_frr, y_frr, 'r')
#plt.show()

x_far = []
y_far = []

cn = len(mismatched_scores_arr)

for x in range(-100, -19):
    fp = 0
    for score in mismatched_scores_arr:
        if score > x:
            fp += 1
    fpr = fp / cn
    x_far.append(x)
    y_far.append(fpr)

#plt.plot(x_far, y_far, 'g')
#plt.show()

plt.plot(normalize(x_frr), normalize(y_frr), 'r', normalize(x_far), normalize(y_far), 'g')
plt.show()

