"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[5681],{3905:(e,t,a)=>{a.d(t,{Zo:()=>m,kt:()=>d});var n=a(67294);function o(e,t,a){return t in e?Object.defineProperty(e,t,{value:a,enumerable:!0,configurable:!0,writable:!0}):e[t]=a,e}function i(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,n)}return a}function r(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?i(Object(a),!0).forEach((function(t){o(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):i(Object(a)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}function s(e,t){if(null==e)return{};var a,n,o=function(e,t){if(null==e)return{};var a,n,o={},i=Object.keys(e);for(n=0;n<i.length;n++)a=i[n],t.indexOf(a)>=0||(o[a]=e[a]);return o}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(n=0;n<i.length;n++)a=i[n],t.indexOf(a)>=0||Object.prototype.propertyIsEnumerable.call(e,a)&&(o[a]=e[a])}return o}var l=n.createContext({}),c=function(e){var t=n.useContext(l),a=t;return e&&(a="function"==typeof e?e(t):r(r({},t),e)),a},m=function(e){var t=c(e.components);return n.createElement(l.Provider,{value:t},e.children)},p={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},u=n.forwardRef((function(e,t){var a=e.components,o=e.mdxType,i=e.originalType,l=e.parentName,m=s(e,["components","mdxType","originalType","parentName"]),u=c(a),d=o,h=u["".concat(l,".").concat(d)]||u[d]||p[d]||i;return a?n.createElement(h,r(r({ref:t},m),{},{components:a})):n.createElement(h,r({ref:t},m))}));function d(e,t){var a=arguments,o=t&&t.mdxType;if("string"==typeof e||o){var i=a.length,r=new Array(i);r[0]=u;var s={};for(var l in t)hasOwnProperty.call(t,l)&&(s[l]=t[l]);s.originalType=e,s.mdxType="string"==typeof e?e:o,r[1]=s;for(var c=2;c<i;c++)r[c]=a[c];return n.createElement.apply(null,r)}return n.createElement.apply(null,a)}u.displayName="MDXCreateElement"},45234:(e,t,a)=>{a.r(t),a.d(t,{assets:()=>l,contentTitle:()=>r,default:()=>p,frontMatter:()=>i,metadata:()=>s,toc:()=>c});var n=a(87462),o=(a(67294),a(3905));const i={},r="Amazon Personalize",s={unversionedId:"datascience/recsys/amazon-personalize",id:"datascience/recsys/amazon-personalize",title:"Amazon Personalize",description:"Amazon Personalize is a machine learning service that makes it easy for developers to create individualized recommendations for customers using their applications. With Amazon Personalize, you provide an activity stream from your application \u2013 clicks, page views, signups, purchases, and so forth \u2013 as well as an inventory of the items you want to recommend, such as articles, products, videos, or music. You can also choose to provide Amazon Personalize with additional demographic information from your users such as age, or geographic location. Amazon Personalize will process and examine the data, identify what is meaningful, select the right algorithms, and train and optimize a personalization model that is customized for your data. All data analyzed by Amazon Personalize is kept private and secure, and only used for your customized recommendations. You can start serving personalized recommendations via a simple API call. You pay only for what you use, and there are no minimum fees and no upfront commitments.",source:"@site/docs/10-datascience/recsys/amazon-personalize.md",sourceDirName:"10-datascience/recsys",slug:"/datascience/recsys/amazon-personalize",permalink:"/docs/datascience/recsys/amazon-personalize",draft:!1,tags:[],version:"current",lastUpdatedBy:"sparsh",lastUpdatedAt:1681047270,formattedLastUpdatedAt:"Apr 9, 2023",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"Recommender Systems",permalink:"/docs/datascience/recsys/"},next:{title:"Graph RecSys Models",permalink:"/docs/datascience/recsys/lab-graph-models/"}},l={},c=[{value:"Personalize Recipes",id:"personalize-recipes",level:2},{value:"Limits of Amazon Personalize",id:"limits-of-amazon-personalize",level:2},{value:"Amazon Personalize Workflow",id:"amazon-personalize-workflow",level:2},{value:"Learnings",id:"learnings",level:2},{value:"Dataset group",id:"dataset-group",level:2},{value:"Evaluation",id:"evaluation",level:2},{value:"Using evaluation metrics",id:"using-evaluation-metrics",level:2},{value:"Amazon Personalize Notes v2",id:"amazon-personalize-notes-v2",level:2},{value:"Amazon Personalize Notes v1",id:"amazon-personalize-notes-v1",level:2},{value:"Amazon Personalize consists of three components:",id:"amazon-personalize-consists-of-three-components",level:2},{value:"References",id:"references",level:2}],m={toc:c};function p(e){let{components:t,...a}=e;return(0,o.kt)("wrapper",(0,n.Z)({},m,a,{components:t,mdxType:"MDXLayout"}),(0,o.kt)("h1",{id:"amazon-personalize"},"Amazon Personalize"),(0,o.kt)("p",null,"Amazon Personalize is a machine learning service that makes it easy for developers to create individualized recommendations for customers using their applications. With Amazon Personalize, you provide an activity stream from your application \u2013 clicks, page views, signups, purchases, and so forth \u2013 as well as an inventory of the items you want to recommend, such as articles, products, videos, or music. You can also choose to provide Amazon Personalize with additional demographic information from your users such as age, or geographic location. Amazon Personalize will process and examine the data, identify what is meaningful, select the right algorithms, and train and optimize a personalization model that is customized for your data. All data analyzed by Amazon Personalize is kept private and secure, and only used for your customized recommendations. You can start serving personalized recommendations via a simple API call. You pay only for what you use, and there are no minimum fees and no upfront commitments."),(0,o.kt)("h2",{id:"personalize-recipes"},"Personalize Recipes"),(0,o.kt)("ul",null,(0,o.kt)("li",{parentName:"ul"},"HRNN - Hierarchical recurrent neural network (HRNN), which is able to model the changes in user behavior."),(0,o.kt)("li",{parentName:"ul"},"HRNN-Metadata - Similar to the HRNN recipe with additional features derived from contextual, user, and item metadata (Interactions, Users, and Items datasets, respectively). Provides accuracy benefits over non-metadata models when high quality metadata is available."),(0,o.kt)("li",{parentName:"ul"},"HRNN-Coldstart - Similar to the HRNN-Metadata recipe, while adding personalized exploration of new items. Use this recipe when you are frequently adding new items to the Items dataset and require the items to immediately appear in the recommendations. Popularity-Count - Popularity-count returns the top popular items from a dataset. A popular item is defined by the number of times it occurs in the dataset. The recipe returns the same popular items for all users."),(0,o.kt)("li",{parentName:"ul"},"Personalized-Ranking - Provides a user with a ranked list of items."),(0,o.kt)("li",{parentName:"ul"},"SIMS - Leverages user-item interaction data to recommend items similar to a given item. In the absence of sufficient user behavior data for an item, this recipe recommends popular items.")),(0,o.kt)("h2",{id:"limits-of-amazon-personalize"},"Limits of Amazon Personalize"),(0,o.kt)("p",null,"It\u2019s true that a powerful tool such as Amazon Personalize makes automatic most of the work required to set up a full working recommendation system. However, Amazon Personalize has still some limits which may with different degrees make this service less desirable for expert scientists and that could restrict the full performance of the model itself:"),(0,o.kt)("ul",null,(0,o.kt)("li",{parentName:"ul"},(0,o.kt)("strong",{parentName:"li"},"Amazon Personalize is relatively slow"),": most of the operations involving Amazon Personalize takes time to complete. For example, creating a new dataset from the dashboard can take a few minutes while train a model can take hours depending on the size of the dataset but it takes long time even for small datasets. Finally, creating a campaign and a batch inference process also take several minutes."),(0,o.kt)("li",{parentName:"ul"},(0,o.kt)("strong",{parentName:"li"},"Input data should follow a specific format"),": although using Amazon Personalize doesn\u2019t require any machine learning knowledge, however, a team of data scientists is still required to handle the data pre-processing which could be a very time and resource consuming process."),(0,o.kt)("li",{parentName:"ul"},(0,o.kt)("strong",{parentName:"li"},"Amazon Personalize accepts a maximum of 5 features per user:"),"\xa0consequently, should be used any feature selection algorithm to estimate features\u2019 importance and select the 5 most useful ones."),(0,o.kt)("li",{parentName:"ul"},(0,o.kt)("strong",{parentName:"li"},"Comparison is not straight-forward"),": The fact that Amazon Personalize selects a random test set makes it difficult the comparison with other models with the metrics provided by the system. Thus, we had first to make predictions on the test set, process the result, and manually compute the metrics.")),(0,o.kt)("h2",{id:"amazon-personalize-workflow"},"Amazon Personalize Workflow"),(0,o.kt)("p",null,"The general workflow for training, deploying, and getting recommendations from a campaign is as follows:"),(0,o.kt)("ol",null,(0,o.kt)("li",{parentName:"ol"},"Prepare data"),(0,o.kt)("li",{parentName:"ol"},"Create related datasets and a dataset group."),(0,o.kt)("li",{parentName:"ol"},"Get training data.",(0,o.kt)("ul",{parentName:"li"},(0,o.kt)("li",{parentName:"ul"},"Import historical data to the dataset group."),(0,o.kt)("li",{parentName:"ul"},"Record user events to the dataset group."))),(0,o.kt)("li",{parentName:"ol"},"Create a solution version (trained model) using a recipe."),(0,o.kt)("li",{parentName:"ol"},"Evaluate the solution version using metrics."),(0,o.kt)("li",{parentName:"ol"},"Create a campaign (deploy the solution version)."),(0,o.kt)("li",{parentName:"ol"},"Provide recommendations for users by running Batch or Real-time Recommendation.")),(0,o.kt)("h2",{id:"learnings"},"Learnings"),(0,o.kt)("ol",null,(0,o.kt)("li",{parentName:"ol"},"How to map datasets to Amazon Personalize."),(0,o.kt)("li",{parentName:"ol"},"Which models or recipes are appropriate for which use cases."),(0,o.kt)("li",{parentName:"ol"},"How to build models in a programmatic fashion."),(0,o.kt)("li",{parentName:"ol"},"How to interpret model metrics."),(0,o.kt)("li",{parentName:"ol"},"How to deploy models in a programmatic fashion."),(0,o.kt)("li",{parentName:"ol"},"How to obtain results from Personalize.")),(0,o.kt)("p",null,"For the most part, the algorithms in Amazon Personalize (called recipes) look to solve different tasks, explained here:"),(0,o.kt)("ol",null,(0,o.kt)("li",{parentName:"ol"},(0,o.kt)("strong",{parentName:"li"},"User Personalization"),"\xa0- New release that supports ALL HRNN workflows / user personalization needs, it will be what we use here."),(0,o.kt)("li",{parentName:"ol"},(0,o.kt)("strong",{parentName:"li"},"HRNN & HRNN-Metadata"),"\xa0- Recommends items based on previous user interactions with items."),(0,o.kt)("li",{parentName:"ol"},(0,o.kt)("strong",{parentName:"li"},"HRNN-Coldstart"),"\xa0- Recommends new items for which interaction data is not yet available."),(0,o.kt)("li",{parentName:"ol"},(0,o.kt)("strong",{parentName:"li"},"Personalized-Ranking"),"\xa0- Takes a collection of items and then orders them in probable order of interest using an HRNN-like approach."),(0,o.kt)("li",{parentName:"ol"},(0,o.kt)("strong",{parentName:"li"},"SIMS (Similar Items)"),"\xa0- Given one item, recommends other items also interacted with by users."),(0,o.kt)("li",{parentName:"ol"},(0,o.kt)("strong",{parentName:"li"},"Popularity-Count"),"\xa0- Recommends the most popular items, if HRNN or HRNN-Metadata do not have an answer - this is returned by default.")),(0,o.kt)("p",null,"No matter the use case, the algorithms all share a base of learning on user-item-interaction data which is defined by 3 core attributes:"),(0,o.kt)("ol",null,(0,o.kt)("li",{parentName:"ol"},(0,o.kt)("strong",{parentName:"li"},"UserID"),"\xa0- The user who interacted"),(0,o.kt)("li",{parentName:"ol"},(0,o.kt)("strong",{parentName:"li"},"ItemID"),"\xa0- The item the user interacted with"),(0,o.kt)("li",{parentName:"ol"},(0,o.kt)("strong",{parentName:"li"},"Timestamp"),"\xa0- The time at which the interaction occurred")),(0,o.kt)("p",null,"We also support event types and event values defined by:"),(0,o.kt)("ol",null,(0,o.kt)("li",{parentName:"ol"},(0,o.kt)("strong",{parentName:"li"},"Event Type"),"\xa0- Categorical label of an event (browse, purchased, rated, etc)."),(0,o.kt)("li",{parentName:"ol"},(0,o.kt)("strong",{parentName:"li"},"Event Value"),"\xa0- A value corresponding to the event type that occurred. Generally speaking, we look for normalized values between 0 and 1 over the event types. For example, if there are three phases to complete a transaction (clicked, added-to-cart, and purchased), then there would be an event_value for each phase as 0.33, 0.66, and 1.0 respectfully.")),(0,o.kt)("p",null,"The event type and event value fields are additional data which can be used to filter the data sent for training the personalization model."),(0,o.kt)("h2",{id:"dataset-group"},"Dataset group"),(0,o.kt)("p",null,"The highest level of isolation and abstraction with Amazon Personalize is a dataset group. Information stored within one of these dataset groups has no impact on any other dataset group or models created from one - they are completely isolated. This allows you to run many experiments and is part of how we keep your models private and fully trained only on your data."),(0,o.kt)("h2",{id:"evaluation"},"Evaluation"),(0,o.kt)("p",null,"We recommend reading\xa0",(0,o.kt)("a",{parentName:"p",href:"https://docs.aws.amazon.com/personalize/latest/dg/working-with-training-metrics.html"},"the documentation"),"\xa0to understand the metrics, but we have also copied parts of the documentation below for convenience."),(0,o.kt)("p",null,"You need to understand the following terms regarding evaluation in Personalize:"),(0,o.kt)("ul",null,(0,o.kt)("li",{parentName:"ul"},(0,o.kt)("em",{parentName:"li"},"Relevant recommendation"),"\xa0refers to a recommendation that matches a value in the testing data for the particular user."),(0,o.kt)("li",{parentName:"ul"},(0,o.kt)("em",{parentName:"li"},"Rank"),"\xa0refers to the position of a recommended item in the list of recommendations. Position 1 (the top of the list) is presumed to be the most relevant to the user."),(0,o.kt)("li",{parentName:"ul"},(0,o.kt)("em",{parentName:"li"},"Query"),"\xa0refers to the internal equivalent of a GetRecommendations call.")),(0,o.kt)("p",null,"The metrics produced by Personalize are:"),(0,o.kt)("ul",null,(0,o.kt)("li",{parentName:"ul"},(0,o.kt)("strong",{parentName:"li"},"coverage"),": The proportion of unique recommended items from all queries out of the total number of unique items in the training data (includes both the Items and Interactions datasets)."),(0,o.kt)("li",{parentName:"ul"},(0,o.kt)("strong",{parentName:"li"},"mean_reciprocal_rank_at_25"),": The\xa0",(0,o.kt)("a",{parentName:"li",href:"https://en.wikipedia.org/wiki/Mean_reciprocal_rank"},"mean of the reciprocal ranks"),"\xa0of the first relevant recommendation out of the top 25 recommendations over all queries. This metric is appropriate if you're interested in the single highest ranked recommendation."),(0,o.kt)("li",{parentName:"ul"},(0,o.kt)("strong",{parentName:"li"},"normalized_discounted_cumulative_gain_at_K"),": Discounted gain assumes that recommendations lower on a list of recommendations are less relevant than higher recommendations. Therefore, each recommendation is discounted (given a lower weight) by a factor dependent on its position. To produce the\xa0",(0,o.kt)("a",{parentName:"li",href:"https://en.wikipedia.org/wiki/Discounted_cumulative_gain"},"cumulative discounted gain"),"\xa0(DCG) at K, each relevant discounted recommendation in the top K recommendations is summed together. The normalized discounted cumulative gain (NDCG) is the DCG divided by the ideal DCG such that NDCG is between 0 - 1. (The ideal DCG is where the top K recommendations are sorted by relevance.) Amazon Personalize uses a weighting factor of 1/log(1 + position), where the top of the list is position 1. This metric rewards relevant items that appear near the top of the list, because the top of a list usually draws more attention."),(0,o.kt)("li",{parentName:"ul"},(0,o.kt)("strong",{parentName:"li"},"precision_at_K"),": The number of relevant recommendations out of the top K recommendations divided by K. This metric rewards precise recommendation of the relevant items.")),(0,o.kt)("h2",{id:"using-evaluation-metrics"},"Using evaluation metrics"),(0,o.kt)("p",null,"It is important to use evaluation metrics carefully. There are a number of factors to keep in mind."),(0,o.kt)("ul",null,(0,o.kt)("li",{parentName:"ul"},"If there is an existing recommendation system in place, this will have influenced the user's interaction history which you use to train your new solutions. This means the evaluation metrics are biased to favor the existing solution. If you work to push the evaluation metrics to match or exceed the existing solution, you may just be pushing the User Personalization to behave like the existing solution and might not end up with something better."),(0,o.kt)("li",{parentName:"ul"},"The HRNN Coldstart recipe is difficult to evaluate using the metrics produced by Amazon Personalize. The aim of the recipe is to recommend items which are new to your business. Therefore, these items will not appear in the existing user transaction data which is used to compute the evaluation metrics. As a result, HRNN Coldstart will never appear to perform better than the other recipes, when compared on the evaluation metrics alone. Note: The User Personalization recipe also includes improved cold start functionality")),(0,o.kt)("p",null,"Keeping in mind these factors, the evaluation metrics produced by Personalize are generally useful for two cases:"),(0,o.kt)("ol",null,(0,o.kt)("li",{parentName:"ol"},"Comparing the performance of solution versions trained on the same recipe, but with different values for the hyperparameters and features (impression data etc)"),(0,o.kt)("li",{parentName:"ol"},"Comparing the performance of solution versions trained on different recipes (except HRNN Coldstart).")),(0,o.kt)("p",null,"Properly evaluating a recommendation system is always best done through A/B testing while measuring actual business outcomes. Since recommendations generated by a system usually influence the user behavior which it is based on, it is better to run small experiments and apply A/B testing for longer periods of time. Over time, the bias from the existing model will fade."),(0,o.kt)("p",null,"The effectiveness of machine learning models is directly tied to the quantity and quality of data input during the training process. For most personalization ML solutions, training data typically comes from clickstream data collected from websites, mobile applications, and other online & offline channels where end-users are interacting with items for which we wish to make recommendations. Examples of clickstream events include viewing items, adding items to a list or cart, and purchasing items. Although an Amazon Personalize Campaign can be started with just new clickstream data, the initial quality of the recommendations will not be as high as a model that has been trained on recent historical data."),(0,o.kt)("h2",{id:"amazon-personalize-notes-v2"},"Amazon Personalize Notes v2"),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867992-a4abe023-168a-460d-a9fd-d8c5ad59b893.png",alt:"content-concepts-raw-amazon-personalize-untitled"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867813-fbbeac29-b382-437a-8794-ca797b8851d8.png",alt:"content-concepts-raw-amazon-personalize-untitled-1"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867817-88dbfd7d-f927-4a6e-ab21-4be611db603a.png",alt:"content-concepts-raw-amazon-personalize-untitled-2"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867820-8d5bb37d-d3b1-4ece-8c63-6f333037ce36.png",alt:"content-concepts-raw-amazon-personalize-untitled-3"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867822-c89d85f9-cd1b-405c-ac08-95b66dd18fad.png",alt:"content-concepts-raw-amazon-personalize-untitled-4"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867823-f1dcd816-dcb1-4b4c-b568-25b48073ffc9.png",alt:"content-concepts-raw-amazon-personalize-untitled-5"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867829-622c9bc9-f388-444b-99d7-a13fea78b2b4.png",alt:"content-concepts-raw-amazon-personalize-untitled-6"})),(0,o.kt)("p",null,"MLOps - Automate the Recommenders"),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867831-d4184b0c-0125-4dee-a4f9-89edd977c057.png",alt:"content-concepts-raw-amazon-personalize-untitled-7"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867833-df5fd62d-f58e-4f58-afc9-8550ca06250a.png",alt:"content-concepts-raw-amazon-personalize-untitled-8"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867835-5dbf78df-0fb2-4942-b4ef-5d23d4305586.png",alt:"content-concepts-raw-amazon-personalize-untitled-9"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867843-aa4b79b9-65f5-4d0f-9681-6b18d9d9ea4c.png",alt:"content-concepts-raw-amazon-personalize-untitled-11"})),(0,o.kt)("h2",{id:"amazon-personalize-notes-v1"},"Amazon Personalize Notes v1"),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867845-9f07aaec-f007-4d5c-9671-2a8e84779537.png",alt:"content-concepts-raw-amazon-personalize-untitled-12"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867847-4581b87e-3993-4936-800b-1b14ce59a9cb.png",alt:"content-concepts-raw-amazon-personalize-untitled-13"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867849-07643e24-675c-4052-aec8-0edd4fc73af9.png",alt:"content-concepts-raw-amazon-personalize-untitled-14"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867854-90634d3f-7200-4f26-894b-884c34c2bf10.png",alt:"content-concepts-raw-amazon-personalize-untitled-15"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867857-81a5b64c-1c1f-40fa-af93-78484ec8bb9a.png",alt:"content-concepts-raw-amazon-personalize-untitled-16"})),(0,o.kt)("p",null,"Popular Use-cases"),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867861-ff4f9384-593f-44ce-b4e2-0921f5145888.png",alt:"content-concepts-raw-amazon-personalize-untitled-17"})),(0,o.kt)("p",null,"Dataset Characteristics"),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867813-fbbeac29-b382-437a-8794-ca797b8851d8.png",alt:"content-concepts-raw-amazon-personalize-untitled-1"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867862-686aea35-5330-4dbb-8306-4b158d34ab3a.png",alt:"content-concepts-raw-amazon-personalize-untitled-18"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867864-fabbbbf4-fba5-4a9f-9f82-0fdf5efd9edc.png",alt:"content-concepts-raw-amazon-personalize-untitled-19"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867822-c89d85f9-cd1b-405c-ac08-95b66dd18fad.png",alt:"content-concepts-raw-amazon-personalize-untitled-4"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867866-03fed4fa-dd9e-4f21-ab9f-7b54dbc8a21b.png",alt:"content-concepts-raw-amazon-personalize-untitled-20"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867823-f1dcd816-dcb1-4b4c-b568-25b48073ffc9.png",alt:"content-concepts-raw-amazon-personalize-untitled-5"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867829-622c9bc9-f388-444b-99d7-a13fea78b2b4.png",alt:"content-concepts-raw-amazon-personalize-untitled-6"})),(0,o.kt)("p",null,"MLOps - Automate the Recommenders"),(0,o.kt)("p",null,(0,o.kt)("a",{parentName:"p",href:"https://www.youtube.com/watch?v=dczs8cORHhg&list=PLN7ADELDRRhiQB9QkFiZolioeJZb3wqPE&index=7"},'"',"Deep Dive on Amazon Personalize",'"'," by: James Jory")),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867868-f3e6e714-9448-43e0-9cfd-ff7388eada52.png",alt:"content-concepts-raw-amazon-personalize-untitled-21"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867871-b8ed6032-eadf-4af0-9cb7-7a2ac16f0092.png",alt:"content-concepts-raw-amazon-personalize-untitled-22"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867873-070868e1-e790-4c5c-a115-339b137b7d2d.png",alt:"content-concepts-raw-amazon-personalize-untitled-23"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867878-f0e0d850-327e-4174-84b1-60691cdf4b7b.png",alt:"content-concepts-raw-amazon-personalize-untitled-24"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867881-16b6ae97-d6f8-41a2-96ba-ef4f1fc630ea.png",alt:"content-concepts-raw-amazon-personalize-untitled-25"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867888-53b1d8b0-fd24-4334-a21c-aa834914e6e2.png",alt:"content-concepts-raw-amazon-personalize-untitled-26"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867831-d4184b0c-0125-4dee-a4f9-89edd977c057.png",alt:"content-concepts-raw-amazon-personalize-untitled-7"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867891-94e3b1bc-968b-412a-afa6-46cd83f66c65.png",alt:"content-concepts-raw-amazon-personalize-untitled-27"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867894-d21216c2-439a-4cce-85c4-8e8e404751eb.png",alt:"content-concepts-raw-amazon-personalize-untitled-28"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867896-6fe3aa08-722d-47d8-be66-9b941b585199.png",alt:"content-concepts-raw-amazon-personalize-untitled-29"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867898-a893aa0c-aafa-444b-acb1-248860e0a830.png",alt:"content-concepts-raw-amazon-personalize-untitled-30"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867902-daaa6463-0ff0-4914-b845-d5092ea329eb.png",alt:"content-concepts-raw-amazon-personalize-untitled-31"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867905-96f85dc5-7cfa-46c1-96be-9280862cc282.png",alt:"content-concepts-raw-amazon-personalize-untitled-32"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867907-9837afcb-9d10-4093-98b1-358a21a57077.png",alt:"content-concepts-raw-amazon-personalize-untitled-33"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867912-42f78ada-202a-4e1c-9028-388e1c191f2e.png",alt:"content-concepts-raw-amazon-personalize-untitled-34"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867919-86db2294-9c1e-490c-8c1a-17fbf0325390.png",alt:"content-concepts-raw-amazon-personalize-untitled-35"})),(0,o.kt)("p",null,(0,o.kt)("a",{parentName:"p",href:"https://www.personalisevideorecs.info/recommend/"},"https://www.personalisevideorecs.info/recommend/")),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867921-553aeab5-8f9d-48b7-9280-7103a0dcfdb6.png",alt:"content-concepts-raw-amazon-personalize-untitled-36"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867924-da81a403-d4cf-496d-a2a6-c27336050312.png",alt:"content-concepts-raw-amazon-personalize-untitled-37"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867925-dd5caa1d-6814-485b-b224-52786046d59f.png",alt:"content-concepts-raw-amazon-personalize-untitled-38"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867927-56b13885-2d0d-4596-9086-204c45db3887.png",alt:"content-concepts-raw-amazon-personalize-untitled-39"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867930-01e9cb22-d8b7-45c4-9b1f-00bc2f371c3d.png",alt:"content-concepts-raw-amazon-personalize-untitled-40"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867935-83bf759a-355f-4791-80fd-fa0cbd375635.png",alt:"content-concepts-raw-amazon-personalize-untitled-41"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867937-bf537550-a35f-482a-9f0b-781d08d8f151.png",alt:"content-concepts-raw-amazon-personalize-untitled-42"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867942-c70ee1ac-1fe7-4920-8928-5c75aecda103.png",alt:"content-concepts-raw-amazon-personalize-untitled-43"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867945-5e0a8675-2763-46df-b5ed-c7cf49ff89e9.png",alt:"content-concepts-raw-amazon-personalize-untitled-44"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867947-3b34eca8-c71c-4bcc-9f2e-4a427b02b580.png",alt:"content-concepts-raw-amazon-personalize-untitled-45"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867951-a5c54839-76ae-4d5c-b056-eb12fd314758.png",alt:"content-concepts-raw-amazon-personalize-untitled-46"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867953-cca589a5-5717-4445-bd20-97055c159a1a.png",alt:"content-concepts-raw-amazon-personalize-untitled-47"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867957-eaecd042-c6d2-4b8e-bb7e-180c5b6aa82a.png",alt:"content-concepts-raw-amazon-personalize-untitled-48"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867959-1dcdd8e9-05b5-491c-818d-d93914b4c80b.png",alt:"content-concepts-raw-amazon-personalize-untitled-49"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867962-4c398afc-8082-49da-83de-9b0d8724a6f2.png",alt:"content-concepts-raw-amazon-personalize-untitled-50"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867964-5d2d6d8c-2bc1-405e-94d7-dcd7cc3d403f.png",alt:"content-concepts-raw-amazon-personalize-untitled-51"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867966-0f89bbb3-465c-4246-a3b9-2fc09e5edbc9.png",alt:"content-concepts-raw-amazon-personalize-untitled-52"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867969-015d54f3-5e07-46f5-9b78-84b7f674a315.png",alt:"content-concepts-raw-amazon-personalize-untitled-53"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867971-3736214a-600c-4109-954b-617190a7c0cf.png",alt:"content-concepts-raw-amazon-personalize-untitled-54"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867973-a294b3e4-55fa-4ba2-afe1-d36b8013aafa.png",alt:"content-concepts-raw-amazon-personalize-untitled-55"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867974-067dc409-1ef6-47fc-a405-aa7d991b12b7.png",alt:"content-concepts-raw-amazon-personalize-untitled-56"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867976-b60df22e-66fb-450d-8c4d-05cbb628df62.png",alt:"content-concepts-raw-amazon-personalize-untitled-57"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867977-e43f35bd-d134-4f6b-bbac-7200d34693a5.png",alt:"content-concepts-raw-amazon-personalize-untitled-58"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867979-419b16d3-c443-4769-8963-5a1a1c1f170c.png",alt:"content-concepts-raw-amazon-personalize-untitled-59"})),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867986-ac2019ab-9fd9-4d86-989b-62b9d589a236.png",alt:"content-concepts-raw-amazon-personalize-untitled-60"})),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre",className:"language-python"},"get_recommendations_response = personalize_runtime.get_recommendations(\n        campaignArn = campaign_arn,\n        userId = user_id\n)\n\nitem_list = get_recommendations_response['itemList']\nrecommendation_list = []\nfor item in item_list:\n    item_id = get_movie_by_id(item['itemId'])\nrecommendation_list.append(item_id)\n")),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867987-a7596579-fc72-47d7-bd4a-36b741f6e026.png",alt:"content-concepts-raw-amazon-personalize-untitled-61"})),(0,o.kt)("h2",{id:"amazon-personalize-consists-of-three-components"},"Amazon Personalize consists of three components:"),(0,o.kt)("ul",null,(0,o.kt)("li",{parentName:"ul"},"Amazon Personalize \u2013 used to create, manage and deploy solution versions."),(0,o.kt)("li",{parentName:"ul"},"Amazon Personalize events \u2013 used to record user events for training data."),(0,o.kt)("li",{parentName:"ul"},"Amazon Personalize Runtime \u2013 used to get recommendations from a campaign.")),(0,o.kt)("p",null,"Amazon Personalize can utilize real time user event data and process it individually or combined with historical data to produce more accurate and relevant recommendations. Unlike historical data, new recorded data is used automatically when getting recommendations. Minimum requirements for new user data are:"),(0,o.kt)("ul",null,(0,o.kt)("li",{parentName:"ul"},"1,000 records of combined interaction data"),(0,o.kt)("li",{parentName:"ul"},"25 unique users with a minimum of 2 interactions each")),(0,o.kt)("h2",{id:"references"},"References"),(0,o.kt)("ol",null,(0,o.kt)("li",{parentName:"ol"},(0,o.kt)("a",{parentName:"li",href:"https://youtu.be/2s7vUQDQPNY?list=PLL0J-WXH0lL6gV50tYSkJPv-irCkA9ods"},"Keynote 6: Personalization For The World - Anoop Deoras (Amazon)")," ",(0,o.kt)("inlineCode",{parentName:"li"},"video"))),(0,o.kt)("p",null,"Amazon Personalize is a fully managed machine learning service that goes beyond rigid static rule based recommendation systems and trains, tunes, and deploys custom ML models to deliver highly customized recommendations to customers across industries such as retail and media and entertainment."),(0,o.kt)("p",null,"It covers 6 use-cases:"),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867857-81a5b64c-1c1f-40fa-af93-78484ec8bb9a.png",alt:"content-concepts-raw-amazon-personalize-untitled-16"})),(0,o.kt)("p",null,"Popular Use-cases"),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867957-eaecd042-c6d2-4b8e-bb7e-180c5b6aa82a.png",alt:"content-concepts-raw-amazon-personalize-untitled-48"})),(0,o.kt)("p",null,"Following are the hands-on tutorials:"),(0,o.kt)("ol",null,(0,o.kt)("li",{parentName:"ol"},(0,o.kt)("a",{parentName:"li",href:"https://github.com/data-science-on-aws/workshop/tree/937f6e4fed53fcc6c22bfac42c2c18a687317995/oreilly_book/02_usecases/personalize_recommendations"},"Data Science on AWS Workshop - Personalize Recommendations",(0,o.kt)("strong",{parentName:"a"},"p"))),(0,o.kt)("li",{parentName:"ol"},(0,o.kt)("a",{parentName:"li",href:"https://aws.amazon.com/blogs/machine-learning/creating-a-recommendation-engine-using-amazon-personalize/"},"https://aws.amazon.com/blogs/machine-learning/creating-a-recommendation-engine-using-amazon-personalize/")),(0,o.kt)("li",{parentName:"ol"},(0,o.kt)("a",{parentName:"li",href:"https://aws.amazon.com/blogs/machine-learning/omnichannel-personalization-with-amazon-personalize/"},"https://aws.amazon.com/blogs/machine-learning/omnichannel-personalization-with-amazon-personalize/")),(0,o.kt)("li",{parentName:"ol"},(0,o.kt)("a",{parentName:"li",href:"https://aws.amazon.com/blogs/machine-learning/using-a-b-testing-to-measure-the-efficacy-of-recommendations-generated-by-amazon-personalize/"},"https://aws.amazon.com/blogs/machine-learning/using-a-b-testing-to-measure-the-efficacy-of-recommendations-generated-by-amazon-personalize/"))),(0,o.kt)("p",null,"Also checkout these resources:"),(0,o.kt)("ol",null,(0,o.kt)("li",{parentName:"ol"},(0,o.kt)("a",{parentName:"li",href:"https://www.youtube.com/playlist?list=PLN7ADELDRRhiQB9QkFiZolioeJZb3wqPE"},"https://www.youtube.com/playlist?list=PLN7ADELDRRhiQB9QkFiZolioeJZb3wqPE"))),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/62965911/219867990-84f50e3f-8106-47bd-b63c-0dc044c37198.png",alt:"content-concepts-raw-amazon-personalize-untitled-62"})))}p.isMDXComponent=!0}}]);