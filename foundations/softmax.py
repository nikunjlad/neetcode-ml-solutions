import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)
        stable_logits = z - np.max(z)

        exp_scores = np.exp(stable_logits)
        probs = exp_scores / np.sum(exp_scores)

        return np.round(probs, 4)
