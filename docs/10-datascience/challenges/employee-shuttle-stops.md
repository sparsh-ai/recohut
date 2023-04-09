# Optimization of Employee Shuttle Stops

## Goal

It is a common practice for tech companies to use shuttle buses to ferry their employees from home to the office.  
The goal of this exercise is to figure out the optimal stops for a bus shuttle. The company is based in Mountain View and the shuttle provides transportation form employees based in San Francisco.

With the explosion of location and user data, data science can be used to optimize many of the services cities offer to their citizens. Transportation optimization is an example of that, but there are so many other possible applications. All this often goes under the name of “[smart city](https://en.wikipedia.org/wiki/Smart_city)” and it is one of the most interesting future applications of data science.

## Challenge Description

Company XYZ has decided to offer a shuttle bus to help its employees commute from San Francisco to Mountain View.  
The city of San Francisco has given the company a list of potential bus stop locations to choose from and asked to not have more than 10 stops within the city.

You have been given the home address of all employees interested in taking the shuttle and asked to come up with the ten most efficient stops.  
While you have been given a certain freedom in defining what is “efficient”, the general consensus within the company is that the most efficient way to select the bus stops is to minimize the overall walking distance between employee homes and the 10 bus stops.

Estimating all possible 10 stop combinations would require a lot of time (how many combinations would that be?). Therefore, your boss is fine with simplifying the problem and returning 10 stops that have a high probability of being the best stops.

You should write an algorithm that returns the best 10 stops in your opinion. Also, please explain the rationale behind the algorithm.

## Data

We have 2 tables:

**Potential\_Bus\_Stops** - this is the list of potential bus stops given by San Francisco to the company. It is a list of intersections in the city.

**Columns:**

- **Street\_One** : one of the two streets intersecting
- **Street\_Two** : the other street intersecting

**Employee\_Addresses** - the home address of each employee interested in taking the shuttle.

**Columns:**

- **address** : employee address
- **employee\_id** : employee id, unique by employee

## Solution

[![nbviewer](https://camo.githubusercontent.com/a2b8b49ec63c501c07f7f5d73ced6fdee58a337609d4a6962d6ec5b4fbd3fec9/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f72656e6465722d6e627669657765722d6f72616e67652e737667)](https://nbviewer.org/gist/sparsh-ai/014f298ef36ec5a9ca109884c2ea3634)