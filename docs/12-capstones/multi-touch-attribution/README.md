# Multi-touch Attribution

## Abstract

We are living in the digital economy and a customer often exposed to promotional ads on different digital channels like Facebook and google search. If a customer purchased a product after multiple exposures on different channels, then how can we estimate each channel's individual contribution towards that conversion, so that we can assign the marketing budget accordingly? 

Multi-touch attribution is a set of methods and modeling techniques that tries to estimate the digital channel's individual contribution leveraging historical data of customer touchpoints and machine learning methodologies. I started with searching for relevant research papers in this domain, performed a literature review, and created a framework. I selected a publicly available dataset for my work with around 2 million records. I experimented with a lot of models and finally settled with three: Markov chains, Survival analysis, and RNN with attention. Conversion prediction accuracy was used as a proxy for evaluation and model selection but the A/B test should also be done before deploying this model in production.

## Overview

MTA pertains to the question of how much the marketing touchpoints a user was exposed to, contributes to an observed action by the consumer. Understanding the contribution of various marketing touchpoints is an input to good campaign design, to optimal budget allocation and for understanding the reasons for why one campaign worked and one did not. Wrong attribution results in misallocation of resources, inefficient prioritization of touchpoints, and consequently lower return on marketing investments. Consequently, having a good model of attribution is now recognized as critical for marketing planning, design and growth.

The problem of attribution is not new. It arises in traditional advertising channels such as television and print. However, online channels offer a unique opportunity to address the attribution problem, as advertisers have disaggregated individual level data which were not previously available. Given the lack of disaggregate data, the marketing literature has focused primarily on marketing mix, which perform inter-temporal analysis of marketing channels but fail to provide insights at an individual customer level. Granular online advertising data can be used to build rich models of consumer response to online ads.

Any business that’s actively running marketing campaigns should be interested in identifying what marketing channels drive the actual conversions. As the array of platforms on which businesses can market to their customers is increasing, and most customers are engaging with your content on multiple channels, it’s now more important than ever to decide how you’re going to attribute conversions to channels. A 2017 study showed that 92% of consumers visiting a retailer’s website for the first time aren’t there to buy.

![260222_mta_b_0](https://user-images.githubusercontent.com/62965911/224530353-1a9afb26-08bc-4f58-a92f-e300d3626a2b.png)

As marketing moves more and more towards the consumer driven side of things, identifying the right channels to target customers has become critical for companies. This helps companies optimize their marketing spends and target the right customers in the right places.

Because the various touchpoints can interact in complex ways to affect the final outcome, the problem of parsing the individual contributions and allocating credit is a complex one. Given the complexity, many firms and platforms use rule-based methods such as last-touch, first-touch, equally-weighted, or time-decayed attribution. Because these rules may not always reflect actuality, modern approaches propose data-driven attribution schemes that use rules derived from actual marketplace data to allocate credit.

More often than not, companies usually invest in the last channel which customers encounter before making the final purchase. However, this may not always be the right approach. There are multiple channels preceding that channel which eventually drive the customer conversion. The underlying concept to study this behavior is known as **‘multi-channel attribution modeling.’**

**Problem Statement:** To quantify the impact of different media channels on sales volume

**Proposed Solution:** Data-driven Multi-touch attribution modeling

**In Scope:**

- Digital Channels including social media ad, paid search ad, display ad, email.
- Fixed time period/window: week, month, campaign duration.
- Models: Markov chain models, Survival analysis models, Attention based Recurrent neural net (RNN) models

**Out of Scope:** Offline channels (e.g. TV, Radio, Print, OOH, Direct marketing)

## Code

[![](https://img.shields.io/badge/jupyter-notebook-informational?logo=jupyter)](https://nbviewer.org/github/recohut/notebook/blob/master/_notebooks/2022-01-29-mta.ipynb)

## List of variables and Data dictionary

![260222_mta_a_0](https://user-images.githubusercontent.com/62965911/224530321-a8b1d284-c318-421e-94d9-3206a19b7830.png)

## Preprocessing

### Dataset 1

![260222_mta_a_1](https://user-images.githubusercontent.com/62965911/224530322-456797b9-3e23-49a0-9521-e1769c930923.png)

![260222_mta_a_2](https://user-images.githubusercontent.com/62965911/224530324-81ff2619-f33f-4f7d-8f7e-4630d9b55a0d.png)

### Dataset 2

![260222_mta_a_3](https://user-images.githubusercontent.com/62965911/224530325-accb04c4-23ce-4cf7-9dc7-32c3f6d865fb.png)

Criteo is a pioneering company in online advertising research. They have published this dataset for attribution modeling in real-time auction based advertising. This dataset is formed of Criteo live traffic data in a period of 30 days. It has more than 16 million impressions and 45 thousand conversions over 700 campaigns.

The impressions in this dataset may derive click actions so each touch point along the user action sequence has a label of whether a click has occurred, and the corresponding conversion ID if this sequence of touch points leads to a conversion event.

![260222_mta_a_4](https://user-images.githubusercontent.com/62965911/224530326-ac602ee7-c51f-4e42-bcf6-8a04e4436a5f.png)

## Exploratory Data Analysis

![260222_mta_a_5](https://user-images.githubusercontent.com/62965911/224530328-eb969c5b-fd50-4c0e-92a5-344acc9e28d3.png)

## Modeling Approaches

### Heuristic approaches to Multi-touch attribution

1. **Last Touch Attribution (LTA)**
    1. ****As the name suggests, Last Touch is the attribution approach where any revenue generated is attributed to the marketing channel that a user last engaged with.
    2. ****While this approach has its advantage in its simplicity, you run the risk of oversimplifying your attribution, as the last touch isn’t necessarily the marketing activity that generates the purchase.
2. **First Touch Attribution (FTA)**
    1. The revenue generated by the purchase is attributed to the first marketing channel the user engaged with, on the journey towards the purchase.
    2. Just as with the Last Touch approach, First Touch Attribution has its advantages in simplicity, but again you risk oversimplifying your attribution approach.
3. **Linear Attribution**
    1. In this approach, the attribution is divided evenly among all the marketing channels touched by the user on the journey leading to a purchase.
    2. This approach is better suited to capture the trend of the multi-channel touch behavior we’re seeing in consumer behavior. However, it does not distinguish between the different channels, and since not all consumer engagements with marketing efforts are equal this is a clear drawback of this model.
    
    ![260222_mta_b_1](https://user-images.githubusercontent.com/62965911/224530359-a0a1384e-3a1e-427f-8703-bad09cf223ac.png)
    

### Data-driven approaches to Multi-touch attribution

![260222_mta_a_6](https://user-images.githubusercontent.com/62965911/224530331-f460c190-bcf5-43ed-8c8d-d3070008ba67.png)

## Markov Chain model

### Basics

1. **What is Markov Chain?**
    1. A Markov chain is a stochastic model describing a sequence of possible events in which the probability of each event depends only on the state attained in the previous event. These events are also known as states. These states together form what is known as State Space.
    2. The probability of next event or next state depends only on the present state and not on the previous states. This property of Markov Chain is called Memoryless property. It doesn’t care what happened in the past event and focuses only on the present information to predict what happens in the next state.
    3. A Markov Chain provides **Information about the current state** & **Transition probabilities of moving from one state to another**. Using the above two information, we can predict the next state. Final State = Initial State * Transition Matrix. 
    4. So, if we multiply the Initial state matrix by the transition matrix, we obtain the first state matrix. If the first state matrix is multiplied by the transition matrix we obtain the second state matrix
2. **What is Transition Matrix?**
    1. The transition probability (the probability that a customer will go from one Sequence A to Sequence B) is given by:
    
    ![260222_mta_a_7](https://user-images.githubusercontent.com/62965911/224530332-34da37e5-a36a-4a18-8c2d-26066c680e2c.png)
    
    ![260222_mta_b_2](https://user-images.githubusercontent.com/62965911/224530360-8074a7c6-f59a-415f-a8d3-3744acf71cae.png)
    
3. **An Example showing how Markov chain and Transition matrix works**
    
    Assume that we need to know what the state the customer is after 6 months of launching the product. There are 200,000 customers which could be in any of the four states – Awareness, Consideration, Purchase, No Purchase. **Final State of Customers = Initial State Vector * Transition Matrix**
    
    ![260222_mta_b_3](https://user-images.githubusercontent.com/62965911/224530362-a1e07929-b9d1-4471-b21d-478162a0ef1a.png)
    

![260222_mta_b_4](https://user-images.githubusercontent.com/62965911/224530365-8ecae697-2249-43cc-b872-35a5cc54cd51.png)

![260222_mta_b_5](https://user-images.githubusercontent.com/62965911/224530366-558f51af-083f-4fa1-8fd2-0e09377bbeac.png)

### Model results

![260222_mta_b_6](https://user-images.githubusercontent.com/62965911/224530368-1ef1088b-a237-4855-8318-048ed318239e.png)

![260222_mta_b_7](https://user-images.githubusercontent.com/62965911/224530370-87be3aa7-49f8-4060-8d0c-4bf606e64236.png)

![260222_mta_b_8](https://user-images.githubusercontent.com/62965911/224530373-6baf0823-d723-4e23-acb3-83944380a129.png)

### User-conversion simulation using Transition matrix

**Problem Statement**: Let’s assume that we are going to attract 1000 visits from Paid Search and we want to model how many conversions we will obtain?

![260222_mta_a_8](https://user-images.githubusercontent.com/62965911/224530333-5de57b85-2dfc-4351-acef-58969af3b68f.png)

![260222_mta_a_9](https://user-images.githubusercontent.com/62965911/224530334-9a571e3e-6bdb-480e-b93e-55ad2b578631.png)

### Time gap analysis & Rule-based customer value inference

![260222_mta_a_10](https://user-images.githubusercontent.com/62965911/224530335-2f12026a-fb42-4640-b61d-a7fd40af6be8.png)

![260222_mta_a_11](https://user-images.githubusercontent.com/62965911/224530337-19aae5df-7de2-4e00-b5f6-ef400d9a1898.png)

**Inference from the above 2 Views**

1. ****So if Person A watched our Facebook ad for the first time 25 days ago and no contact since then – Customer is fruitless for us. **Customer Value = Low**
2. ****If Person B also watched our Facebook ad for the first time 25 days ago and visited website 14 days ago – Customer is fruitless for us. **Customer Value = Low**
3. ****If Person C also watched our Facebook ad for the first time 25 days ago and visited website 7 days ago – customer is still fruitful for us. **Customer Value = Mid-High**

## Additive Hazard Model

![260222_mta_a_12](https://user-images.githubusercontent.com/62965911/224530347-9c87635f-3830-4169-81b1-af3656f80718.png)

![260222_mta_a_13](https://user-images.githubusercontent.com/62965911/224530349-8664f396-ccda-4d7f-9674-7b3ff6ba5e92.png)

## Model Comparison on conversion Probability

![260222_mta_a_14](https://user-images.githubusercontent.com/62965911/224530350-368fa934-7979-4ca5-b966-3861db80434c.png)

![260222_mta_a_15](https://user-images.githubusercontent.com/62965911/224530352-464f0c7b-1e0c-4584-be14-25029b8dc240.png)

## References

1. [https://www.stat.auckland.ac.nz/~fewster/325/notes/ch8.pdf](https://www.stat.auckland.ac.nz/~fewster/325/notes/ch8.pdf)
2. [https://towardsdatascience.com/marketing-analytics-through-markov-chain-a9c7357da2e8](https://towardsdatascience.com/marketing-analytics-through-markov-chain-a9c7357da2e8)
3. [http://www3.govst.edu/kriordan/files/ssc/math161/pdf/Chapter10ppt.pdf](http://www3.govst.edu/kriordan/files/ssc/math161/pdf/Chapter10ppt.pdf)
4. [http://math.furman.edu/~tlewis/math13/markov1.pdf](http://math.furman.edu/~tlewis/math13/markov1.pdf) 
5. Markov chains concept - [https://analyzecore.com/2016/08/03/attribution-model-r-part-1/](https://analyzecore.com/2016/08/03/attribution-model-r-part-1/)
6. Slides: [https://www.slideshare.net/adavide1982/markov-model-for-the-multichannel-attribution-problem](https://www.slideshare.net/adavide1982/markov-model-for-the-multichannel-attribution-problem)
7. PDF Report: [https://aaltodoc.aalto.fi/bitstream/handle/123456789/13898/master_Rentola_Olli_2014.pdf?sequence=1](https://aaltodoc.aalto.fi/bitstream/handle/123456789/13898/master_Rentola_Olli_2014.pdf?sequence=1)
8. Advertising Attribution Modeling in the Movie Industry - [https://mc-stan.org/events/stancon2017-notebooks/stancon2017-lei-sanders-dawson-ad-attribution.html](https://mc-stan.org/events/stancon2017-notebooks/stancon2017-lei-sanders-dawson-ad-attribution.html)
9. [http://datafeedtoolbox.com/attribution-theory-the-two-best-models-for-algorithmic-marketing-attribution-implemented-in-apache-spark-and-r/](http://datafeedtoolbox.com/attribution-theory-the-two-best-models-for-algorithmic-marketing-attribution-implemented-in-apache-spark-and-r/)
10. [https://www.bounteous.com/insights/2016/06/30/marketing-channel-attribution-markov-models-r/?ns=l](https://www.bounteous.com/insights/2016/06/30/marketing-channel-attribution-markov-models-r/?ns=l)
11. Google Analytics Multi-channel funnels: [https://support.google.com/analytics/answer/1191180?hl=en](https://support.google.com/analytics/answer/1191180?hl=en)
12. R Package - [https://github.com/cran/ChannelAttribution](https://github.com/cran/ChannelAttribution)
13. [Original dataset from ‘Criteo - online advertising research company’](http://ailab.criteo.com/criteo-attribution-modeling-bidding-dataset/)
14. [https://sequentpartners.com/wp-content/uploads/2017/01/ADMAP-DECEMBER-2016-.pdf](https://sequentpartners.com/wp-content/uploads/2017/01/ADMAP-DECEMBER-2016-.pdf)
15. [https://www.visualiq.com/resource-center/newsletter/marketing-modeling-attribution-together](https://www.visualiq.com/resource-center/newsletter/marketing-modeling-attribution-together)
16. [https://www.iquanti.com/wp-content/uploads/2018/10/iQuantiINSIGHTS_Hybrid-Approach-to-Attribution-Modeling_Whitepaper.pdf](https://www.iquanti.com/wp-content/uploads/2018/10/iQuantiINSIGHTS_Hybrid-Approach-to-Attribution-Modeling_Whitepaper.pdf) 
17. [https://pdfs.semanticscholar.org/9ecf/f16d2044a2a296d78262fb083ef29296a445.pdf](https://pdfs.semanticscholar.org/9ecf/f16d2044a2a296d78262fb083ef29296a445.pdf) 
18. [http://eprints.bbk.ac.uk/16166/1/CIKM2016_582.pdf](http://eprints.bbk.ac.uk/16166/1/CIKM2016_582.pdf) 
19. [http://www0.cs.ucl.ac.uk/staff/w.zhang/rtb-papers/data-conv-att.pdf](http://www0.cs.ucl.ac.uk/staff/w.zhang/rtb-papers/data-conv-att.pdf) 
20. [https://arxiv.org/pdf/1808.03737.pdf](https://arxiv.org/pdf/1808.03737.pdf) 
21. [https://arxiv.org/pdf/1809.02230.pdf](https://arxiv.org/pdf/1809.02230.pdf) 
22. [https://arxiv.org/pdf/1902.00215.pdf](https://arxiv.org/pdf/1902.00215.pdf) 
23. [https://www.sas.com/content/dam/SAS/support/en/sas-global-forum-proceedings/2018/2111-2018.pdf](https://www.sas.com/content/dam/SAS/support/en/sas-global-forum-proceedings/2018/2111-2018.pdf) 
24. [https://storage.googleapis.com/pub-tools-public-publication-data/pdf/de1c3ab14fd52301fb193237fdffd45352159d5c.pdf](https://storage.googleapis.com/pub-tools-public-publication-data/pdf/de1c3ab14fd52301fb193237fdffd45352159d5c.pdf) 
25. [https://pure.tue.nl/ws/files/96724049/Master_Thesis_Robbert_Alblas.pdf](https://pure.tue.nl/ws/files/96724049/Master_Thesis_Robbert_Alblas.pdf) 
26. [https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/45766.pdf](https://static.googleusercontent.com/media/research.google.com/en/pubs/archive/45766.pdf) 
27. [https://storage.googleapis.com/pub-tools-public-publication-data/pdf/45331.pdf](https://storage.googleapis.com/pub-tools-public-publication-data/pdf/45331.pdf) 
28. [https://www.nielsen.com/us/en/insights/news/2019/methods-models-a-guide-to-multi-touch-attribution.html](https://www.nielsen.com/us/en/insights/news/2019/methods-models-a-guide-to-multi-touch-attribution.html) 
29. [https://www.r-bloggers.com/marketing-multi-channel-attribution-model-with-r-part-2-practical-issues/](https://www.r-bloggers.com/marketing-multi-channel-attribution-model-with-r-part-2-practical-issues/) 
30. [http://delivery.acm.org/10.1145/3320000/3313470/p1376-nuara.pdf?ip=122.15.228.208&id=3313470&acc=OPEN&key=4D4702B0C3E38B35%2E4D4702B0C3E38B35%2E4D4702B0C3E38B35%2E6D218144511F3437&__acm__=1559618525_b1614c5976fcf5f1a9328b3050f56256](http://delivery.acm.org/10.1145/3320000/3313470/p1376-nuara.pdf?ip=122.15.228.208&id=3313470&acc=OPEN&key=4D4702B0C3E38B35%2E4D4702B0C3E38B35%2E4D4702B0C3E38B35%2E6D218144511F3437&__acm__=1559618525_b1614c5976fcf5f1a9328b3050f56256) 
31. [https://arxiv.org/ftp/arxiv/papers/1804/1804.05327.pdf](https://arxiv.org/ftp/arxiv/papers/1804/1804.05327.pdf) 
32. [https://ahsanijaz.github.io/2016-10-21-ChannelAttribution/](https://ahsanijaz.github.io/2016-10-21-ChannelAttribution/) 
33. [http://184pc128.csie.ntnu.edu.tw/presentation/17-02-21/A%20Probabilistic%20Multi-Touch%20Attribution%20Model%20for%20Online%20Advertising_slide.pdf](http://184pc128.csie.ntnu.edu.tw/presentation/17-02-21/A%20Probabilistic%20Multi-Touch%20Attribution%20Model%20for%20Online%20Advertising_slide.pdf) 
34. [http://www.saying.ren/slides/deep-conv-attr.pdf](http://www.saying.ren/slides/deep-conv-attr.pdf) 
35. [https://dl.acm.org/citation.cfm?id=3313470](https://dl.acm.org/citation.cfm?id=3313470) 
36. [http://gen.lib.rus.ec/scimag/?q=Mapping+The+Customer+Journey%3A+Lessons+Learned+From+Graph-Based+Online+Attribution+Modeling](http://gen.lib.rus.ec/scimag/?q=Mapping+The+Customer+Journey%3A+Lessons+Learned+From+Graph-Based+Online+Attribution+Modeling)
37. [https://github.com/rk2900/deep-conv-attr](https://github.com/rk2900/deep-conv-attr) 
38. [https://github.com/eeghor/mta](https://github.com/eeghor/mta) 
39. [https://github.com/LouisBIGDATA/Channel-Attribution-Modeling-in-Marketing](https://github.com/LouisBIGDATA/Channel-Attribution-Modeling-in-Marketing) 
40. [https://github.com/cran/ahaz](https://github.com/cran/ahaz)