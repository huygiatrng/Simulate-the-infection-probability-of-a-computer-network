from matplotlib import pyplot as plt
import statistics

def histogramData(list, c):
    # Show the histogram of days to finish of literations.
    y, x, _ = plt.hist(list,facecolor='blue',histtype = 'bar', alpha = 0.8)

    # Show amount of data above each bar.
    for i, v in enumerate(y):
        if v != 0:
            plt.text(x[i] , v, str(v))
    # We can add more graph setting with different c var if we want to.
    if c == 0:
        # Show median line.
        plt.axvline(statistics.median(list), color='#fc4f30', label='Median', linewidth=3)
        plt.legend()
        plt.xlabel('Days to finish')
        plt.ylabel('Number of trials')
        plt.title('Histogram of days to finish')
    plt.grid(True)
    plt.show()
