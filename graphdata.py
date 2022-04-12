from matplotlib import pyplot as plt
import statistics

def histogramData(list, c):
    # Show the histogram of days to finish of literations.
    y, x, _ = plt.hist(list,facecolor='blue',histtype = 'bar', alpha = 0.8)

    # Show amount of data above each bar.
    for i, v in enumerate(y):
        if v != 0:
            plt.text(x[i] , v, str(v))

    # Show median line.
    if c == 0:
        plt.axvline(statistics.median(list), color='#fc4f30', label='Median', linewidth=3)
        plt.legend()
        plt.xlabel('Days to finish')
        plt.ylabel('Number of trials')
        plt.title('Histogram of days to finish')
    elif c==1:
        plt.axvline(statistics.median(list), color='#fc4f30', label='Median', linewidth=3)
        plt.legend()
        plt.title('Probability that each computer gets infected at least once')
    elif c==2:
        plt.axvline(statistics.median(list), color='#fc4f30', label='Median', linewidth=3)
        plt.legend()
        plt.xlabel('Expected number of computers get infected')
        plt.ylabel('Number of trials')
        plt.title('The expected number of computers that get infected')
    plt.grid(True)
    plt.show()