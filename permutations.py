from collections import defaultdict

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        integer_counts = defaultdict(int)
        for i in A:
            integer_counts[i] += 1
        current_permutation = []
        unique_permutations = []
        self.get_permutations(A, unique_permutations, current_permutation, integer_counts)
        return unique_permutations

    def get_permutations(self, A, unique_permutations, current_permutation, integer_counts):
        for k in set(A):
            if (integer_counts[k] == 0):
                continue
            current_permutation.append(k)
            integer_counts[k] -= 1
            if (len(current_permutation) == len(A)):
                unique_permutations.append(list(current_permutation))
            else:
                self.get_permutations(A, unique_permutations, current_permutation, integer_counts)
            integer_counts[k] += 1
            current_permutation.pop()
