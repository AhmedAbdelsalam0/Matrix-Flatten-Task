import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9],
             [1, 2, 3], [4, 5, 6], [7, 8, 9],
             [1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(a.flatten())
print(a.ravel())

# Both flatten() and ravel() functions are used to flatten arrays

# raven is faster than flatten
# raven is library level function
# raven returns a reference of the original array (view), but flatten returns a copy
