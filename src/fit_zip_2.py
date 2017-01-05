#!/usr/bin/env python

__author__ = 'Federico G. Padua'

'''
Here I assume the zipf distributed cdf, and also that we want to fit only one parameter:
alpha as referred to other papers (Web caching...)
'''

import sympy as sp
from sympy import *
import numpy as np
import scipy as sc
import scipy_data_fitting as sdf

import os
import time
import matplotlib.pyplot as plt
import json



N = 100

class Timer:
    def __enter__(self):
        self.start = time.clock()
        return self

    def __exit__(self, *args):
        self.end = time.clock()
        self.interval = self.end - self.start


def plot_data_file(data_passed):

    fig, ax = plt.subplots()
    ax.plot(data_passed[0], data_passed[1])
    ax.axis('tight')
    ax.set_title('cdf zipf-like')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    plt.show()


def personal_cdfzipf_like(x, params):  # s= param[0], N, param[1], alpha= param[2]
    #x.astype(int)
    y_val = []
    #print("N= %d" % N)
    for a in x:
        num = sum(1./pow(x_, params) for x_ in range(1, a+1))
        eccolo = (num/sum(1./pow(n, params) for n in range(1, int(N)+1)))*100
        y_val.append(eccolo)
    y_fina = np.array(y_val)
    return y_fina
    #return (sum(1./x_**p0 for x_ in range(1, x+1)) / sum(1./n**p0 for n in range(1, int(p1)+1)))*100


def personal_cdfzipf_like1(x, params):  # s= param[0], N, param[1], alpha= param[2]
    return (sum(1./x_**params[0] for x_ in range(1, int(x)+1)) / sum(1./n**params[0] for n in range(1, params[1]+1)))*100
#     return (1/x**params[0]) / dd


def cdf_zipf_likefunc(x, *params):  # k is the x; params[0]=s, params[1]=N, params[2]=alpha
    #print("Now entered the fit function!!!!!")
    # y_val = []
    # for a in x:
    #     num = sp.harmonic(a, params[0])
    #     eccolo = (num/sp.harmonic(params[1], params[0]))*100
    #     y_val.append(eccolo)
    # y_fina = np.array(y_val)
    # return y_fina

    return ((sp.harmonic(x, params[0])/sp.harmonic(params[1], params[0]))*100)   # ** (1 - params[2]))*100)



def func(x_, p1, p2, p3):  # k is the x; params[3]=x params[0]=s, params[1]=N, params[2]=alpha
    #print("Now entered the fit function!!!!!")
    return ((sp.harmonic(x_, p1)/sp.harmonic(p2, p1)) ** (1 - p3))*100


def zipf_pmf(x, s, alpha, n):
    return 1/(sp.harmonic(n, s) * (x ** s))


def zipf_like_pmf(x, s, alpha, n):
    return (1/(sp.harmonic(n, s) * (x ** s))) ** (1 - alpha)


def prova_zipf_cdf(x, a):
    return ((zetac(x)+1)/(zetac(a)+1))


def save_example_fit(fit):
    """
    Save fit result to a json file and a plot to an svg file.
    """
    #json_directory = os.path.join('examples', 'json')
    #plot_directory = os.path.join('examples', 'plots')
    #if not os.path.isdir(json_directory): os.makedirs(json_directory)
    #if not os.path.isdir(plot_directory): os.makedirs(plot_directory)

    fit.to_json(os.path.join(os.getcwd(), fit.name + '.json'), meta=fit.metadata)

    plot = sdf.Plot(fit)
    plot.save(os.path.join(os.getcwd(), fit.name + '.svg'))
    plot.close()

if __name__ == '__main__':

    with Timer() as t:
        x = np.arange(0, 100, dtype=int)
        #x = np.linspace(1, 100, 100)
        #N = 100
        alpha_r = -0.2
        s_r = 0.43
        y_list = []
        y_pmflist = []
        y_zipf_likepmflist = []
        #print(x)
        parametri = (s_r)
        #parametri = [s_r, N, alpha_r]
        #for p in x:
         #   print p
            #print(fitfunc(p, s_r, alpha_r, N))
            #y_list.append(cdf_zipf_likefunc(p, parametri))
            #y_list.append(personal_cdfzipf_like1(p, parametri))
            #y_zipf_likepmflist.append(zipf_like_pmf(p, s_r, alpha_r, N))
        #print(y_list)
        #y = np.array(y_list, dtype=float)
        y = personal_cdfzipf_like(x, parametri)
        #print y
        #y_pmf = np.array(y_pmflist, dtype=float)
        #y_zipflikepmf = np.array(y_zipf_likepmflist, dtype=float)
        #print(y_pmf)
        #print(y)
        #print(y)
        #np.savetxt('data_to_fit.csv', (x, y), delimiter=',')   # x,y,z equal sized 1D arrays
        #data = np.genfromtxt('data_to_fit.csv', delimiter=',')
        #print(data)
        #print(data.shape)
        # plot data produced
        #print(data[0])
        #print(data[1])
        #plot_data_file(data)

        # create a real csv file for the data you have
        #a = x.flatten()
        #y_cdfzipflike = y.flatten()
        #print(a.shape)
        #print(y_cdfzipflike.shape)
        #output = np.column_stack((a, y_cdfzipflike))
        #print(output)
        #np.savetxt('data_to_fit_columnsformat.csv', output, delimiter=',')

        #plt.plot(x, y, marker='o', markersize=2, linestyle='None', color='k')
        #plt.plot(x, y_pmf, marker='o', markersize=2, linestyle='None', color='k')
        #plt.loglog(x, y_pmf, marker='o', markersize=2, linestyle='None', color='k')
        #plt.loglog(x, y_zipflikepmf, marker='o', markersize=2, linestyle='None', color='r')
        #plt.grid(True)

        #plt.show()

        #x0 = sc.array([0.9, 90], dtype=float)
        x0 = sc.array([20], dtype=float)
        #print(x.shape)
        #print(y.shape)
        #print(x0.shape)
        #primo, secondo = sc.optimize.curve_fit(personal_cdfzipf_like, x, y, p0=x0)
        #y_sigma =
        #try:
        p, cov = sc.optimize.curve_fit(personal_cdfzipf_like, x, y, p0=x0)
        #except:
        #    p, cov = x0, None
        #print p
        #print(p[0])
        #print(len(p))

        #dof = len(x) - len(p)
        #print(dof)
        print "\nCovariance Matrix evaluated by Scipy (is already reduced): \n", cov, "\n"

        perr = np.sqrt(np.diag(cov))
        #print perr
        print "\nEstimated parameters and uncertainties (with initial guesses)"
        for i in range(len(p)):   # to be checked!!!!
            print ("   p[%d] = %e +/- %e      (%e)" % (i, p[i], perr, x0[i]))

        # keep the code below just for reference
        #for i in range(len(p)):
        #    print ("   p[%d] = %10.5f +/- %10.5f      (%10.5f)" % (i, p[i], sqrt(cov[i, i]), x0[i]))
        # try:
        #     # Calculate Chi-squared
        #     chisq = sum(((y-personal_cdfzipf_like(x, p[0]))/1)**2)
        #     # WARNING : Scipy seems to use non-standard poorly documented notation for cov,
        #     #   which misleads many people. See "cov_x" on
        #     #   http://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.leastsq.html#scipy.optimize.leastsq
        #     #   (which underlies curve_fit) and also discussion at
        #     #   http://stackoverflow.com/questions/14854339/in-scipy-how-and-why-does-curve-fit-calculate-the-covariance-of-the-parameter-es.
        #     #   I think this agrees with @cdeil at http://nbviewer.ipython.org/5014170/.
        #     #   THANKS to Wes Watters <wwatters@wellesley.edu> for pointing this out to me (16 September 2013)
        #     #
        #     # Convert Scipy cov matrix to standard covariance matrix.
        #     cov = cov*dof/chisq
        #     #print("d.o.f. = %d" % dof)
        #     #print("Chi square = %f" % float(chisq))
        #     #print("chisq/dof = %f" % float(chisq)/dof)
        #     print "Standard covariance"
        #     print(cov)
        #     print "Correlation Matrix :"
        #     for i, row in enumerate(cov):
        #         for j in range(len(p)):
        #             print "%10f" % (cov[i, j]/np.sqrt(cov[i, i]*cov[j, j])),
        #                 # Note: comma at end of print statement suppresses new line
        #         print
        #     print "\nEstimated parameters and uncertainties (with initial guesses)"
        # #  Note: If the fit is poor, i.e. chisq/dof is large, the uncertainties
        # #   are scaled up. If the fit is too good, i.e. chisq/dof << 1, it suggests
        # #   that the uncertainties have been overestimated, but the uncertainties
        # #   are not scaled down.
        #     #print("chisq divided by dof")
        #     #print(np.sqrt(chisq/dof))
        #     #for i in range(len(p)):
        #     #    print ("   p[%d] = %10.5f +/- %10.5f      (%10.5f)" % (i, p[i], sqrt(cov[i, i])), x0[i])
        #     for i in range(len(p)):   # to be checked!!!!
        #         print ("   p[%d] = %10.5f +/- %10.5f      (%10.5f)" % (i, p[i], cov[i, i]**0.5*max(1, np.sqrt(chisq/dof)), x0[i]))
        #
        #
        # # If cov has not been calculated because of a bad fit, the above block
        # #   will cause a python TypeError which is caught by this try-except structure.
        # except TypeError:
        #     print "**** BAD FIT ****"
        #     print "Parameters were: ", p
        #     # Calculate Chi-squared for current parameters
        #     chisq = sum(((y-personal_cdfzipf_like(x, p))/1.)**2)
        #     print "Chi-Squared/dof for these parameter values = %10.5f, CDF = %10.5f%%"\
        #         % (chisq/dof, 100.*float(sc.special.chdtrc(dof, chisq)))
        #     print "Uncertainties not calculated."
        #     print
        #     print "Try a different initial guess for the fit parameters."
        #     print "Or if these parameters appear close to a good fit, try giving"
        #     print "    the fitting program more time by increasing the value of maxfev."
        #     chisq = None


        #print(col)
        #print(cov)
        #print sc.optimize.curve_fit(cdf_zipf_likefunc, x, y, p0=x0)
        #yyyy = []
        #for p in x:
        #    yyyy.append(personal_cdfzipf_like(x, col[0], col[1]))
        # jau = personal_cdfzipf_like(x, p)
        # #plt.plot(x, jau, linestyle='-', color='r')
        # #plt.show()
        #
        # fig1 = plt.figure(1)
        # #Plot Data-model
        # frame1 = fig1.add_axes((.1, .3, .8, .6))
        # #xstart, ystart, xend, yend [units are fraction of the image frame, from bottom left corner]
        # plt.plot(x, y, '.b') #Noisy data
        # plt.plot(x, jau, '-r') #Best fit model
        # frame1.set_xticklabels([]) #Remove x-tic labels for the first frame
        # plt.grid()
        #
        # #Residual plot
        # difference = jau - y
        # frame2 = fig1.add_axes((.1, .1, .8, .2))
        # plt.plot(x, difference, 'or')
        # plt.grid()
        # plt.show()

        #for i in enumerate(y):
        #y_fit = personal_cdfzipf_like(x, p)
        #y_residual = y - y_fit

        ## Plot

        # # create figure with light gray background
        # fig = plt.figure(facecolor="0.98")
        # # 3 rows, 1 column, subplot 1
        # #   3 rows are declared, but there are only 2 plots; this leaves room for text
        # #       in the empty 3rd row
        # fit = fig.add_subplot(311)
        # # remove tick labels from upper plot (for clean look)
        # fit.set_xticklabels( () )
        #
        # # Plot data as red circles, and fitted function as (default) line
        # #   (The sort is in case the x data are not in sequential order.)
        # fit.plot(x, y, 'ro', np.sort(x), personal_cdfzipf_like(np.sort(x), p))
        # #   draw starting guess as dashed green line ('r-')
        # #fit.plot(x_func, initial_plot, 'g-', label="Start", linestyle="--")
        # # Add error bars on data as red crosses.
        # #fit.errorbar(x, y, yerr=y_sigma, fmt='r+')
        #
        # # separate plot to show residuals
        # residuals = fig.add_subplot(312) # 3 rows, 1 column, subplot 2
        # residuals.plot(x, y_residual, label="Residuals")
        # # make sure residual plot has same x axis as fit plot
        # residuals.set_xlim(fit.get_xlim())
        # residuals.axhline(y=0) # draw horizontal line at 0 on vertical axis
        # # Label axes
        # plt.xlabel("energy [KeV]")
        # plt.ylabel("Counts")
        # # These data look better if 'plain', not scientific, notation is used,
        # #   and if the tick labels are not offset by a constant (as is done by default).
        # #   Note: This only works for matplotlib version 1.0 and newer, so it is
        # #           enclosed in a "try" to avoid errors.
        # try:
        #     plt.ticklabel_format(style='plain', useOffset=False, axis='x')
        # except:
        #     pass
        #
        # # print selected information in empty 3rd plot row
        # try:
        #     plt.figtext(0.05, 0.25, "Converged with ChiSq = " + str(chisq) + ", DOF = " +
        #         str(dof) + ", CDF = " + str(100*sc.special.chdtrc(dof, chisq))+"%")
        #     for i, value in enumerate(p):
        #         plt.figtext(0.08, 0.16-i*0.03, "p["+str(i)+"]" + " = " +
        #                    str(p[i]).ljust(18) + " +/- " +
        #                    str(np.sqrt(cov[i, i])),
        #                    fontdict=None)
        #         # Note: Including family="Monospace" in the above figtext call will
        #         #       produce nicer looking output, but can cause problems with
        #         #       some older python installations.
        # except TypeError:
        #     plt.figtext(0.05, 0.25, "BAD FIT.  Guess again.")

        jau = personal_cdfzipf_like(x, p[0])
        #plt.plot(x, jau, linestyle='-', color='r')
        #plt.show()

        fig1 = plt.figure(1)
        #Plot Data-model
        frame1 = fig1.add_axes((.1, .3, .8, .6))
        #xstart, ystart, xend, yend [units are fraction of the image frame, from bottom left corner]
        plt.plot(x, y, '.b') #Noisy data
        plt.plot(x, jau, '-r') #Best fit model
        frame1.set_xticklabels([]) #Remove x-tic labels for the first frame
        plt.grid()

        #Residual plot
        difference = jau - y
        #print difference
        frame2 = fig1.add_axes((.1, .1, .8, .2))

        plt.plot(x, difference, 'or')
        plt.ylim(-5e-14, 5e-14)
        plt.grid()
        #Display the plot
        plt.show()
        #plt.savefig('zpf_cdf_fit_%s.pdf' % 'tiny')


    print('Time to do the fit = %.03f sec.' % t.interval)