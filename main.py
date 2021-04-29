import matplotlib.pyplot as plt
from strategy import ProbabilityAlgorithm, GreedyAlgorithm
from analysis import run_all_tests


if __name__ == '__main__':
    run_all_tests(GreedyAlgorithm)
    plt.show()
