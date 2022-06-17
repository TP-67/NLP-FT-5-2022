import numpy as np

# Define 'while' function to loop through all the inputs until meeting 'exit' or wrong strings.
while True:
    input_str = input('Please input two words with comma:\n')
    # String cleaning
    processed_str = input_str.replace(' ', '').split(',')

    # End the loop when users input 'exit'.
    if processed_str[0] == 'exit':
        break

    # Input validation check
    assert len(processed_str) == 2, 'Wrong input!'

    # Input words
    # word1 = 'intention'
    # word2 = 'execution'
    word1 = processed_str[0]
    word2 = processed_str[1]

    # Get length
    m = len(word1)
    n = len(word2)

    # Initialize distance matrix
    distance_matrix = np.zeros((m + 1, n + 1))
    distance_matrix[0] = np.array([i for i in range(n + 1)])
    distance_matrix[:, 0] = np.array([i for i in range(m + 1)])

    # Calculate distance matrix
    """
    The value of each position is calculated using its left, bottom, and diagonal neighbors.
    (1) If the current characters from both original and target strings are the same, then the diagonal difference is 1. Otherwise, it's 2.
    (2) The differences between current position and its left and bottom neighbors are 1.
    (3) Return the minimum value amoung three above mentioned values as the new value of the current position.
    """
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            temp = 0 if word1[i - 1] == word2[j - 1] else 2
            distance_matrix[i, j] = min(distance_matrix[i - 1, j] + 1,
                                        distance_matrix[i - 1, j - 1] + temp,
                                        distance_matrix[i, j - 1] + 1)

    # Results
    print('Distance Matrix: \n', distance_matrix)
    print('Minimum Edit Distance:', int(distance_matrix[m, n]), '\n')

    # Backtrace
    # Initialize backtracking indexes
    i, j = m, n
    # Count the steps
    count = 1
    # Loop until reaching the first index of both original and target words.
    while i >= 0 and j >= 0:
        # If the current characters from both words are the same, no operation has been taken. We move indexes along the diagonal.
        if word1[i - 1] == word2[j - 1] and distance_matrix[i, j] == distance_matrix[i - 1, j - 1]:
            i -= 1
            j -= 1
            print('Step', count, ': Do Nothing')
            count += 1
        # If the current characters are different and the difference between current position and its diagonal neighbor is 2,
        # a substitution operatino has been taken. We move the indexes along the diagonal.
        elif word1[i - 1] != word2[j - 1] and distance_matrix[i, j] == distance_matrix[i - 1, j - 1] + 2:
            i -= 1
            j -= 1
            print('Step', count, ': Substitution')
            count += 1
        # If we can not move along the diagonal, we need to find whether we need to go down or go left based on
        # the difference between current position and its left and bottom neighbors.
        elif distance_matrix[i, j] == distance_matrix[i - 1, j] + 1:
            i -= 1
            print('Step', count, ': Insertion')
            count += 1
        elif distance_matrix[i, j] == distance_matrix[i, j - 1] + 1:
            j -= 1
            print('Step', count, ': Deletion')
        else:
            break

    print('Over!')
