# Bayesian Optimization

Optimization aims to locate the optimal set of parameters of interest across the whole domain through carefully allocating limited resources. For example, when searching for the car key at home before leaving for work in two minutes, we would naturally start with the most promising place where we would usually put the key. If it is not there, think for a little while about the possible locations and go to the next most promising place. This process iterates until the key is found. In this example, the policy is digesting the available information on previous searches and proposing the following promising location. The environment is the house itself, revealing if the key is placed at the proposed location upon each sampling.

Following is an example objective function with the global maximum and its location marked with star. The goal of global optimization is to systematically reason about a series of sampling decisions so as to locate the global maximum as fast as possible:

![527334_1_En_1_Fig2_HTML](https://user-images.githubusercontent.com/62965911/227536844-232bb35e-d1a9-4130-8f92-bb40609ffbe0.jpeg)

Note that this is a nonconvex function, as is often the case in real-life functions we are optimizing. A nonconvex function means we could not resort to first-order gradient-based methods to reliably search for the global optimum since it will likely converge to a local optimum. This is also one of the advantages of Bayesian optimization compared with other gradient-based optimization procedures

