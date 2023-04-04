# User Referral Program

## Goal

Almost all sites have a user referral program where you can invite new users to try a given product. Typically, after the new user completes a transaction, you get rewarded with a certain amount of money or credit to be used on the site.

The goal of this challenge is to analyze the data from a referral program and draw conclusions about its effectiveness.

## Challenge Description

Company XYZ has started a new referral program on Oct, 31. Each user who refers a new user will get 10$ in credit when the new user buys something.

The program has been running for almost a month and the Growth Product Manager wants to know if it’s been successful. She is very excited because, since the referral program started, the company saw a spike in number of users and wants you to be able to give her some data she can show to her boss.

- Can you estimate the impact the program had on the site?
- Based on the data, what would you suggest to do as a next step?
- The referral program wasn’t really tested in a rigorous way. It simply started on a given day for all users and you are drawing conclusions by looking at the data before and after the test started. What kinds of risks this approach presents? Can you think of a better way to test the program and measure its impact?

## Data

`referral.csv` ([download](https://github.com/sparsh-ai/assets/files/11149557/referral.csv)) - provides information about each transaction that happens on the site and whether the user came from the referral program or not.

**Columns:**

- **user\_id** : the id of the user
- **date** : date of the purchase
- **country** : user country based on the ip address
- **money\_spent** : how much the item bought costs(USD)
- **is\_referral** : whether the user came from the referral program (1) or not (0)
- **device\_id** : Id of the device used to make the purchase

## Solution

[![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/gist/sparsh-ai/0a351138ace8c61a8ce36d934d7dbfa3/user-referral-program.ipynb)
[![nbviewer](https://camo.githubusercontent.com/a2b8b49ec63c501c07f7f5d73ced6fdee58a337609d4a6962d6ec5b4fbd3fec9/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f72656e6465722d6e627669657765722d6f72616e67652e737667)](https://nbviewer.org/gist/sparsh-ai/0a351138ace8c61a8ce36d934d7dbfa3)
