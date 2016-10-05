#!/usr/bin/python

import random
import collections
import math
import sys
from collections import Counter
from util import *


############################################################
# Problem 3: binary classification
############################################################

############################################################
# Problem 3a: feature extraction

def extractWordFeatures(x):
    """
    Extract word features for a string x. Words are delimited by
    whitespace characters only.
    @param string x: 
    @return dict: feature vector representation of x.
    Example: "I am what I am" --> {'I': 2, 'am': 2, 'what': 1}
    """
    # BEGIN_YOUR_CODE (our solution is 4 lines of code, but don't worry if you deviate from this)
    word_features = dict()
    for i in x.split(' '):
        if i not in word_features:
            word_features[i]=1
        else:
            word_features[i]+=1
    return word_features
    # END_YOUR_CODE

############################################################
# Problem 3b: stochastic gradient descent

def wtimesphi(weights, word_features):
    val = 0
    for i in word_features.keys():
        if i in weights:
            val+=weights[i]*word_features[i]
    return val

def learnPredictor(trainExamples, testExamples, featureExtractor, numIters, eta):
    '''
    Given |trainExamples| and |testExamples| (each one is a list of (x,y)
    pairs), a |featureExtractor| to apply to x, and the number of iterations to
    train |numIters|, the step size |eta|, return the weight vector (sparse
    feature vector) learned.

    You should implement stochastic gradient descent.

    Note: only use the trainExamples for training!
    You should call evaluatePredictor() on both trainExamples and testExamples
    to see how you're doing as you learn after each iteration.
    '''

    weights = {}  # feature => weight
    for i in range(numIters):
        for example in trainExamples:
            word_features = extractWordFeatures(example[0])
            otherLoss = 1 - wtimesphi(weights, word_features)*example[1]
            # print "otherloss" + str(otherLoss)
            if otherLoss > 0:
                # print "otherLoss is bigger than 0"
                for i in word_features:
                    if i not in weights:
                        weights[i] = 0
                    
                    weights[i]+=eta*word_features[i]*example[1]
            
            def predictor(x):
                value = 0
                word_features = extractWordFeatures(x)
                for i in word_features.keys():
                    if i in weights:
                        value+=weights[i]*word_features[i]
                if value>0:
                    return 1
                elif value <0:
                    return -1
                else:
                    return 0
        print "Train error: " + str(evaluatePredictor(trainExamples, predictor))
        print "Test error: " + str(evaluatePredictor(testExamples, predictor))

    # BEGIN_YOUR_CODE (our solution is 12 lines of code, but don't worry if you deviate from this)
    # END_YOUR_CODE
    return weights

############################################################
# Problem 3c: generate test case

def generateDataset(numExamples, weights):
    '''
    Return a set of examples (phi(x), y) randomly which are classified correctly by
    |weights|.
    '''
    random.seed(42)
    phi = {}
    # Return a single example (phi(x), y).
    # phi(x) should be a dict whose keys are a subset of the keys in weights
    # and values can be anything (randomize!) with a nonzero score under the given weight vector.
    # y should be 1 or -1 as classified by the weight vector.
    def generateExample():
        # BEGIN_YOUR_CODE (our solution is 2 lines of code, but don't worry if you deviate from this)
        while (True):
            for i in random.sample(weights.keys(), random.randint(0, len(weights.keys()))):
                phi[i] = random.randint(0,10)
            # END_YOUR_CODE
            val = 0
            for i in phi.keys():
                val+=phi[i]*weights[i]
            if val>0:
                y = 1
            elif val<0:
                y = -1
            else:
                continue
            break
        return (phi, y)
    return [generateExample() for _ in range(numExamples)]

############################################################
# Problem 3e: character features

def extractCharacterFeatures(n):
    '''
    Return a function that takes a string |x| and returns a sparse feature
    vector consisting of all n-grams of |x| without spaces.
    EXAMPLE: (n = 3) "I like tacos" --> {'Ili': 1, 'lik': 1, 'ike': 1, ...
    You may assume that n >= 1.
    '''
    def extract(x):
        # BEGIN_YOUR_CODE (our solution is 6 lines of code, but don't worry if you deviate from this)
        x = "".join(x.split())
        bulla = {}
        for i in range(0, len(x) - n + 1):
            if x[i:i+n] not in bulla:
                bulla[x[i:i+n]] = 0
            bulla[x[i:i+n]]+=1
        return bulla

        # END_YOUR_CODE
    return extract

############################################################
# Problem 4: k-means
############################################################


def kmeans(examples, K, maxIters):
    '''
    examples: list of examples, each example is a string-to-double dict representing a sparse vector.
    K: number of desired clusters. Assume that 0 < K <= |examples|.
    maxIters: maximum number of iterations to run for (you should terminate early if the algorithm converges).
    Return: (length K list of cluster centroids,
            list of assignments, (i.e. if examples[i] belongs to centers[j], then assignments[i] = j)
            final reconstruction loss)
    '''
    # BEGIN_YOUR_CODE (our solution is 32 lines of code, but don't worry if you deviate from this)
    raise Exception("Not implemented yet")
    # END_YOUR_CODE
