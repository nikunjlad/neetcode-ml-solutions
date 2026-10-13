class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places

        # check if iterations are 0, if so, just return the initial value
        if iterations == 0:
            return init

        x = float(init)     # set initial value as float

        # loop over each iteration. 
        # for every iteration, update the rule 
        for i in range(iterations):
            x -= learning_rate * (2 * x)

        # finally return the rounded answer to 5 decimal places
        return round(x,5)
