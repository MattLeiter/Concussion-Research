#! /usr/bin/env python3.4

import numpy as np

def single_sim(cumthresh, linmean, linthresh, hiddenthresh):
    exptrials = cumthresh / linmean
    expthis = np.floor(3*exptrials)
    ranthresh = linmean - hiddenthresh
    rawmags = np.array([hiddenthresh + np.random.exponential(ranthresh, expthis)])
    low_values_indices = rawmags <= hiddenthresh
    rawmags[low_values_indices] = 0
    summags = np.cumsum(rawmags)
    keyindx = np.argwhere(summags >= cumthresh)[0]
    rawmag_unlist = rawmags[0]
    return(keyindx, rawmag_unlist[keyindx], np.mean(rawmag_unlist), rawmags.round()[0])




if __name__ == "__main__":
   single_sim(1000, 20, 15, 10)
