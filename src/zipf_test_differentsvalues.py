#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
#import scipy.special as sps
from sympy import harmonic
import time


class Timer:
    def __enter__(self):
        self.start = time.clock()
        return self

    def __exit__(self, *args):
        self.end = time.clock()
        self.interval = self.end - self.start

if __name__ == '__main__':

    with Timer() as t:
    # cdf = harmonic(k, s)/harmonic(N, s)
    #N_tiny = 35983718
    #N_huge = 3129224
    #s = 2
    #list_y_cdf_huge = []
    #list_y_cdf_tiny = []
    #for k in range(1, 101):
    #    cdf_huge = harmonic(k, s)/harmonic(N_huge, s)
    #    cdf_tiny = harmonic(k, s)/harmonic(N_tiny, s)
    #    list_y_cdf_huge.append(cdf_huge)
    #    list_y_cdf_tiny.append(cdf_tiny)

        N_tiny = 100
        #N_huge = 3129224
        #s1 = 0
        #s2 = 0.2
        #s3 = 0.5
        #s4 = 1
        #s5 = 1.2
        #s6 = 1.4
        #s7 = 1.5
        #s8 = 1.7
        s5 = 1
        s6 = 2
        s7 = 3
        s8 = 4
        s9 = 5
        s10 = 6
        s11 = 7
        list_s = [s5, s6, s7, s8, s9, s10, s11]  #, s5, s6, s7, s8, s9, s10]
        colors = ['b', 'r', 'g', 'y', 'k', 'm', 'c']
        #zipped = zip(list_s)
        #list_y_cdf_huge = []
        x = np.arange(0, 1, 0.01)
        list_y_cdf_tiny = [[] for i in range(0, len(list_s))]
        #count = 0
        for j in range(0, len(list_s)):
            for k in range(0, 100):
                #print("k = %d" % k)
            #    cdf_huge = harmonic(k, s)/harmonic(N_huge, s)
                cdf_tiny = harmonic(k, list_s[j])/harmonic(N_tiny, list_s[j])
                #print("cdfs vals = %s" % cdf_tiny)
            #    list_y_cdf_huge.append(cdf_huge)
                list_y_cdf_tiny[j].append(cdf_tiny)
            plt.plot(x, list_y_cdf_tiny[j], linewidth=2, color=colors[j], label='s = %d' % list_s[j])



        #a = 2. # parameter
        #s = np.random.zipf(a, 1000)

        #y = x**(-a)/sps.zetac(a)
        #y = x**(-a)/
        #plt.plot(x, list_y_cdf_huge, linewidth=2, color='r', label='Huge files')
        #plt.plot(x, list_y_cdf_tiny, linewidth=2, color='b', label='s10')
        plt.legend(loc='lower right', title='s values, alpha fixed = 0')
    plt.grid(True)
        #plt.savefig('zipf_temp_cdftry.pdf')
    print('Before plotting took %.03f sec.' % t.interval)
    plt.show()
    #plt.savefig('zpf_diff_svalues.pdf')
