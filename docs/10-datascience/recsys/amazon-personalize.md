# Amazon Personalize

Amazon Personalize is a machine learning service that makes it easy for developers to create individualized recommendations for customers using their applications. With Amazon Personalize, you provide an activity stream from your application – clicks, page views, signups, purchases, and so forth – as well as an inventory of the items you want to recommend, such as articles, products, videos, or music. You can also choose to provide Amazon Personalize with additional demographic information from your users such as age, or geographic location. Amazon Personalize will process and examine the data, identify what is meaningful, select the right algorithms, and train and optimize a personalization model that is customized for your data. All data analyzed by Amazon Personalize is kept private and secure, and only used for your customized recommendations. You can start serving personalized recommendations via a simple API call. You pay only for what you use, and there are no minimum fees and no upfront commitments.

## Personalize Recipes

- HRNN - Hierarchical recurrent neural network (HRNN), which is able to model the changes in user behavior.
- HRNN-Metadata - Similar to the HRNN recipe with additional features derived from contextual, user, and item metadata (Interactions, Users, and Items datasets, respectively). Provides accuracy benefits over non-metadata models when high quality metadata is available.
- HRNN-Coldstart - Similar to the HRNN-Metadata recipe, while adding personalized exploration of new items. Use this recipe when you are frequently adding new items to the Items dataset and require the items to immediately appear in the recommendations. Popularity-Count - Popularity-count returns the top popular items from a dataset. A popular item is defined by the number of times it occurs in the dataset. The recipe returns the same popular items for all users.
- Personalized-Ranking - Provides a user with a ranked list of items.
- SIMS - Leverages user-item interaction data to recommend items similar to a given item. In the absence of sufficient user behavior data for an item, this recipe recommends popular items.

## Limits of Amazon Personalize

It’s true that a powerful tool such as Amazon Personalize makes automatic most of the work required to set up a full working recommendation system. However, Amazon Personalize has still some limits which may with different degrees make this service less desirable for expert scientists and that could restrict the full performance of the model itself:

- **Amazon Personalize is relatively slow**: most of the operations involving Amazon Personalize takes time to complete. For example, creating a new dataset from the dashboard can take a few minutes while train a model can take hours depending on the size of the dataset but it takes long time even for small datasets. Finally, creating a campaign and a batch inference process also take several minutes.
- **Input data should follow a specific format**: although using Amazon Personalize doesn’t require any machine learning knowledge, however, a team of data scientists is still required to handle the data pre-processing which could be a very time and resource consuming process.
- **Amazon Personalize accepts a maximum of 5 features per user:** consequently, should be used any feature selection algorithm to estimate features’ importance and select the 5 most useful ones.
- **Comparison is not straight-forward**: The fact that Amazon Personalize selects a random test set makes it difficult the comparison with other models with the metrics provided by the system. Thus, we had first to make predictions on the test set, process the result, and manually compute the metrics.

## Amazon Personalize Workflow

The general workflow for training, deploying, and getting recommendations from a campaign is as follows:

1. Prepare data
2. Create related datasets and a dataset group.
3. Get training data.
   - Import historical data to the dataset group.
   - Record user events to the dataset group.
4. Create a solution version (trained model) using a recipe.
5. Evaluate the solution version using metrics.
6. Create a campaign (deploy the solution version).
7. Provide recommendations for users by running Batch or Real-time Recommendation.

## Learnings

1. How to map datasets to Amazon Personalize.
2. Which models or recipes are appropriate for which use cases.
3. How to build models in a programmatic fashion.
4. How to interpret model metrics.
5. How to deploy models in a programmatic fashion.
6. How to obtain results from Personalize.

For the most part, the algorithms in Amazon Personalize (called recipes) look to solve different tasks, explained here:

1. **User Personalization** - New release that supports ALL HRNN workflows / user personalization needs, it will be what we use here.
2. **HRNN & HRNN-Metadata** - Recommends items based on previous user interactions with items.
3. **HRNN-Coldstart** - Recommends new items for which interaction data is not yet available.
4. **Personalized-Ranking** - Takes a collection of items and then orders them in probable order of interest using an HRNN-like approach.
5. **SIMS (Similar Items)** - Given one item, recommends other items also interacted with by users.
6. **Popularity-Count** - Recommends the most popular items, if HRNN or HRNN-Metadata do not have an answer - this is returned by default.

No matter the use case, the algorithms all share a base of learning on user-item-interaction data which is defined by 3 core attributes:

1. **UserID** - The user who interacted
2. **ItemID** - The item the user interacted with
3. **Timestamp** - The time at which the interaction occurred

We also support event types and event values defined by:

1. **Event Type** - Categorical label of an event (browse, purchased, rated, etc).
2. **Event Value** - A value corresponding to the event type that occurred. Generally speaking, we look for normalized values between 0 and 1 over the event types. For example, if there are three phases to complete a transaction (clicked, added-to-cart, and purchased), then there would be an event_value for each phase as 0.33, 0.66, and 1.0 respectfully.

The event type and event value fields are additional data which can be used to filter the data sent for training the personalization model.

## Dataset group

The highest level of isolation and abstraction with Amazon Personalize is a dataset group. Information stored within one of these dataset groups has no impact on any other dataset group or models created from one - they are completely isolated. This allows you to run many experiments and is part of how we keep your models private and fully trained only on your data.

## Evaluation

We recommend reading [the documentation](https://docs.aws.amazon.com/personalize/latest/dg/working-with-training-metrics.html) to understand the metrics, but we have also copied parts of the documentation below for convenience.

You need to understand the following terms regarding evaluation in Personalize:

- *Relevant recommendation* refers to a recommendation that matches a value in the testing data for the particular user.
- *Rank* refers to the position of a recommended item in the list of recommendations. Position 1 (the top of the list) is presumed to be the most relevant to the user.
- *Query* refers to the internal equivalent of a GetRecommendations call.

The metrics produced by Personalize are:

- **coverage**: The proportion of unique recommended items from all queries out of the total number of unique items in the training data (includes both the Items and Interactions datasets).
- **mean_reciprocal_rank_at_25**: The [mean of the reciprocal ranks](https://en.wikipedia.org/wiki/Mean_reciprocal_rank) of the first relevant recommendation out of the top 25 recommendations over all queries. This metric is appropriate if you're interested in the single highest ranked recommendation.
- **normalized_discounted_cumulative_gain_at_K**: Discounted gain assumes that recommendations lower on a list of recommendations are less relevant than higher recommendations. Therefore, each recommendation is discounted (given a lower weight) by a factor dependent on its position. To produce the [cumulative discounted gain](https://en.wikipedia.org/wiki/Discounted_cumulative_gain) (DCG) at K, each relevant discounted recommendation in the top K recommendations is summed together. The normalized discounted cumulative gain (NDCG) is the DCG divided by the ideal DCG such that NDCG is between 0 - 1. (The ideal DCG is where the top K recommendations are sorted by relevance.) Amazon Personalize uses a weighting factor of 1/log(1 + position), where the top of the list is position 1. This metric rewards relevant items that appear near the top of the list, because the top of a list usually draws more attention.
- **precision_at_K**: The number of relevant recommendations out of the top K recommendations divided by K. This metric rewards precise recommendation of the relevant items.

## Using evaluation metrics

It is important to use evaluation metrics carefully. There are a number of factors to keep in mind.

- If there is an existing recommendation system in place, this will have influenced the user's interaction history which you use to train your new solutions. This means the evaluation metrics are biased to favor the existing solution. If you work to push the evaluation metrics to match or exceed the existing solution, you may just be pushing the User Personalization to behave like the existing solution and might not end up with something better.
- The HRNN Coldstart recipe is difficult to evaluate using the metrics produced by Amazon Personalize. The aim of the recipe is to recommend items which are new to your business. Therefore, these items will not appear in the existing user transaction data which is used to compute the evaluation metrics. As a result, HRNN Coldstart will never appear to perform better than the other recipes, when compared on the evaluation metrics alone. Note: The User Personalization recipe also includes improved cold start functionality

Keeping in mind these factors, the evaluation metrics produced by Personalize are generally useful for two cases:

1. Comparing the performance of solution versions trained on the same recipe, but with different values for the hyperparameters and features (impression data etc)
2. Comparing the performance of solution versions trained on different recipes (except HRNN Coldstart).

Properly evaluating a recommendation system is always best done through A/B testing while measuring actual business outcomes. Since recommendations generated by a system usually influence the user behavior which it is based on, it is better to run small experiments and apply A/B testing for longer periods of time. Over time, the bias from the existing model will fade.

The effectiveness of machine learning models is directly tied to the quantity and quality of data input during the training process. For most personalization ML solutions, training data typically comes from clickstream data collected from websites, mobile applications, and other online & offline channels where end-users are interacting with items for which we wish to make recommendations. Examples of clickstream events include viewing items, adding items to a list or cart, and purchasing items. Although an Amazon Personalize Campaign can be started with just new clickstream data, the initial quality of the recommendations will not be as high as a model that has been trained on recent historical data.

## Amazon Personalize Notes v2

![content-concepts-raw-amazon-personalize-untitled](https://user-images.githubusercontent.com/62965911/219867992-a4abe023-168a-460d-a9fd-d8c5ad59b893.png)

![content-concepts-raw-amazon-personalize-untitled-1](https://user-images.githubusercontent.com/62965911/219867813-fbbeac29-b382-437a-8794-ca797b8851d8.png)

![content-concepts-raw-amazon-personalize-untitled-2](https://user-images.githubusercontent.com/62965911/219867817-88dbfd7d-f927-4a6e-ab21-4be611db603a.png)

![content-concepts-raw-amazon-personalize-untitled-3](https://user-images.githubusercontent.com/62965911/219867820-8d5bb37d-d3b1-4ece-8c63-6f333037ce36.png)

![content-concepts-raw-amazon-personalize-untitled-4](https://user-images.githubusercontent.com/62965911/219867822-c89d85f9-cd1b-405c-ac08-95b66dd18fad.png)

![content-concepts-raw-amazon-personalize-untitled-5](https://user-images.githubusercontent.com/62965911/219867823-f1dcd816-dcb1-4b4c-b568-25b48073ffc9.png)

![content-concepts-raw-amazon-personalize-untitled-6](https://user-images.githubusercontent.com/62965911/219867829-622c9bc9-f388-444b-99d7-a13fea78b2b4.png)

MLOps - Automate the Recommenders

![content-concepts-raw-amazon-personalize-untitled-7](https://user-images.githubusercontent.com/62965911/219867831-d4184b0c-0125-4dee-a4f9-89edd977c057.png)

![content-concepts-raw-amazon-personalize-untitled-8](https://user-images.githubusercontent.com/62965911/219867833-df5fd62d-f58e-4f58-afc9-8550ca06250a.png)

![content-concepts-raw-amazon-personalize-untitled-9](https://user-images.githubusercontent.com/62965911/219867835-5dbf78df-0fb2-4942-b4ef-5d23d4305586.png)

![content-concepts-raw-amazon-personalize-untitled-11](https://user-images.githubusercontent.com/62965911/219867843-aa4b79b9-65f5-4d0f-9681-6b18d9d9ea4c.png)

## Amazon Personalize Notes v1

![content-concepts-raw-amazon-personalize-untitled-12](https://user-images.githubusercontent.com/62965911/219867845-9f07aaec-f007-4d5c-9671-2a8e84779537.png)

![content-concepts-raw-amazon-personalize-untitled-13](https://user-images.githubusercontent.com/62965911/219867847-4581b87e-3993-4936-800b-1b14ce59a9cb.png)

![content-concepts-raw-amazon-personalize-untitled-14](https://user-images.githubusercontent.com/62965911/219867849-07643e24-675c-4052-aec8-0edd4fc73af9.png)

![content-concepts-raw-amazon-personalize-untitled-15](https://user-images.githubusercontent.com/62965911/219867854-90634d3f-7200-4f26-894b-884c34c2bf10.png)

![content-concepts-raw-amazon-personalize-untitled-16](https://user-images.githubusercontent.com/62965911/219867857-81a5b64c-1c1f-40fa-af93-78484ec8bb9a.png)

Popular Use-cases

![content-concepts-raw-amazon-personalize-untitled-17](https://user-images.githubusercontent.com/62965911/219867861-ff4f9384-593f-44ce-b4e2-0921f5145888.png)

Dataset Characteristics

![content-concepts-raw-amazon-personalize-untitled-1](https://user-images.githubusercontent.com/62965911/219867813-fbbeac29-b382-437a-8794-ca797b8851d8.png)

![content-concepts-raw-amazon-personalize-untitled-18](https://user-images.githubusercontent.com/62965911/219867862-686aea35-5330-4dbb-8306-4b158d34ab3a.png)

![content-concepts-raw-amazon-personalize-untitled-19](https://user-images.githubusercontent.com/62965911/219867864-fabbbbf4-fba5-4a9f-9f82-0fdf5efd9edc.png)

![content-concepts-raw-amazon-personalize-untitled-4](https://user-images.githubusercontent.com/62965911/219867822-c89d85f9-cd1b-405c-ac08-95b66dd18fad.png)

![content-concepts-raw-amazon-personalize-untitled-20](https://user-images.githubusercontent.com/62965911/219867866-03fed4fa-dd9e-4f21-ab9f-7b54dbc8a21b.png)

![content-concepts-raw-amazon-personalize-untitled-5](https://user-images.githubusercontent.com/62965911/219867823-f1dcd816-dcb1-4b4c-b568-25b48073ffc9.png)

![content-concepts-raw-amazon-personalize-untitled-6](https://user-images.githubusercontent.com/62965911/219867829-622c9bc9-f388-444b-99d7-a13fea78b2b4.png)

MLOps - Automate the Recommenders

[&#34;Deep Dive on Amazon Personalize&#34; by: James Jory](https://www.youtube.com/watch?v=dczs8cORHhg&list=PLN7ADELDRRhiQB9QkFiZolioeJZb3wqPE&index=7)

![content-concepts-raw-amazon-personalize-untitled-21](https://user-images.githubusercontent.com/62965911/219867868-f3e6e714-9448-43e0-9cfd-ff7388eada52.png)

![content-concepts-raw-amazon-personalize-untitled-22](https://user-images.githubusercontent.com/62965911/219867871-b8ed6032-eadf-4af0-9cb7-7a2ac16f0092.png)

![content-concepts-raw-amazon-personalize-untitled-23](https://user-images.githubusercontent.com/62965911/219867873-070868e1-e790-4c5c-a115-339b137b7d2d.png)

![content-concepts-raw-amazon-personalize-untitled-24](https://user-images.githubusercontent.com/62965911/219867878-f0e0d850-327e-4174-84b1-60691cdf4b7b.png)

![content-concepts-raw-amazon-personalize-untitled-25](https://user-images.githubusercontent.com/62965911/219867881-16b6ae97-d6f8-41a2-96ba-ef4f1fc630ea.png)

![content-concepts-raw-amazon-personalize-untitled-26](https://user-images.githubusercontent.com/62965911/219867888-53b1d8b0-fd24-4334-a21c-aa834914e6e2.png)

![content-concepts-raw-amazon-personalize-untitled-7](https://user-images.githubusercontent.com/62965911/219867831-d4184b0c-0125-4dee-a4f9-89edd977c057.png)

![content-concepts-raw-amazon-personalize-untitled-27](https://user-images.githubusercontent.com/62965911/219867891-94e3b1bc-968b-412a-afa6-46cd83f66c65.png)

![content-concepts-raw-amazon-personalize-untitled-28](https://user-images.githubusercontent.com/62965911/219867894-d21216c2-439a-4cce-85c4-8e8e404751eb.png)

![content-concepts-raw-amazon-personalize-untitled-29](https://user-images.githubusercontent.com/62965911/219867896-6fe3aa08-722d-47d8-be66-9b941b585199.png)

![content-concepts-raw-amazon-personalize-untitled-30](https://user-images.githubusercontent.com/62965911/219867898-a893aa0c-aafa-444b-acb1-248860e0a830.png)

![content-concepts-raw-amazon-personalize-untitled-31](https://user-images.githubusercontent.com/62965911/219867902-daaa6463-0ff0-4914-b845-d5092ea329eb.png)

![content-concepts-raw-amazon-personalize-untitled-32](https://user-images.githubusercontent.com/62965911/219867905-96f85dc5-7cfa-46c1-96be-9280862cc282.png)

![content-concepts-raw-amazon-personalize-untitled-33](https://user-images.githubusercontent.com/62965911/219867907-9837afcb-9d10-4093-98b1-358a21a57077.png)

![content-concepts-raw-amazon-personalize-untitled-34](https://user-images.githubusercontent.com/62965911/219867912-42f78ada-202a-4e1c-9028-388e1c191f2e.png)

![content-concepts-raw-amazon-personalize-untitled-35](https://user-images.githubusercontent.com/62965911/219867919-86db2294-9c1e-490c-8c1a-17fbf0325390.png)

[https://www.personalisevideorecs.info/recommend/](https://www.personalisevideorecs.info/recommend/)

![content-concepts-raw-amazon-personalize-untitled-36](https://user-images.githubusercontent.com/62965911/219867921-553aeab5-8f9d-48b7-9280-7103a0dcfdb6.png)

![content-concepts-raw-amazon-personalize-untitled-37](https://user-images.githubusercontent.com/62965911/219867924-da81a403-d4cf-496d-a2a6-c27336050312.png)

![content-concepts-raw-amazon-personalize-untitled-38](https://user-images.githubusercontent.com/62965911/219867925-dd5caa1d-6814-485b-b224-52786046d59f.png)

![content-concepts-raw-amazon-personalize-untitled-39](https://user-images.githubusercontent.com/62965911/219867927-56b13885-2d0d-4596-9086-204c45db3887.png)

![content-concepts-raw-amazon-personalize-untitled-40](https://user-images.githubusercontent.com/62965911/219867930-01e9cb22-d8b7-45c4-9b1f-00bc2f371c3d.png)

![content-concepts-raw-amazon-personalize-untitled-41](https://user-images.githubusercontent.com/62965911/219867935-83bf759a-355f-4791-80fd-fa0cbd375635.png)

![content-concepts-raw-amazon-personalize-untitled-42](https://user-images.githubusercontent.com/62965911/219867937-bf537550-a35f-482a-9f0b-781d08d8f151.png)

![content-concepts-raw-amazon-personalize-untitled-43](https://user-images.githubusercontent.com/62965911/219867942-c70ee1ac-1fe7-4920-8928-5c75aecda103.png)

![content-concepts-raw-amazon-personalize-untitled-44](https://user-images.githubusercontent.com/62965911/219867945-5e0a8675-2763-46df-b5ed-c7cf49ff89e9.png)

![content-concepts-raw-amazon-personalize-untitled-45](https://user-images.githubusercontent.com/62965911/219867947-3b34eca8-c71c-4bcc-9f2e-4a427b02b580.png)

![content-concepts-raw-amazon-personalize-untitled-46](https://user-images.githubusercontent.com/62965911/219867951-a5c54839-76ae-4d5c-b056-eb12fd314758.png)

![content-concepts-raw-amazon-personalize-untitled-47](https://user-images.githubusercontent.com/62965911/219867953-cca589a5-5717-4445-bd20-97055c159a1a.png)

![content-concepts-raw-amazon-personalize-untitled-48](https://user-images.githubusercontent.com/62965911/219867957-eaecd042-c6d2-4b8e-bb7e-180c5b6aa82a.png)

![content-concepts-raw-amazon-personalize-untitled-49](https://user-images.githubusercontent.com/62965911/219867959-1dcdd8e9-05b5-491c-818d-d93914b4c80b.png)

![content-concepts-raw-amazon-personalize-untitled-50](https://user-images.githubusercontent.com/62965911/219867962-4c398afc-8082-49da-83de-9b0d8724a6f2.png)

![content-concepts-raw-amazon-personalize-untitled-51](https://user-images.githubusercontent.com/62965911/219867964-5d2d6d8c-2bc1-405e-94d7-dcd7cc3d403f.png)

![content-concepts-raw-amazon-personalize-untitled-52](https://user-images.githubusercontent.com/62965911/219867966-0f89bbb3-465c-4246-a3b9-2fc09e5edbc9.png)

![content-concepts-raw-amazon-personalize-untitled-53](https://user-images.githubusercontent.com/62965911/219867969-015d54f3-5e07-46f5-9b78-84b7f674a315.png)

![content-concepts-raw-amazon-personalize-untitled-54](https://user-images.githubusercontent.com/62965911/219867971-3736214a-600c-4109-954b-617190a7c0cf.png)

![content-concepts-raw-amazon-personalize-untitled-55](https://user-images.githubusercontent.com/62965911/219867973-a294b3e4-55fa-4ba2-afe1-d36b8013aafa.png)

![content-concepts-raw-amazon-personalize-untitled-56](https://user-images.githubusercontent.com/62965911/219867974-067dc409-1ef6-47fc-a405-aa7d991b12b7.png)

![content-concepts-raw-amazon-personalize-untitled-57](https://user-images.githubusercontent.com/62965911/219867976-b60df22e-66fb-450d-8c4d-05cbb628df62.png)

![content-concepts-raw-amazon-personalize-untitled-58](https://user-images.githubusercontent.com/62965911/219867977-e43f35bd-d134-4f6b-bbac-7200d34693a5.png)

![content-concepts-raw-amazon-personalize-untitled-59](https://user-images.githubusercontent.com/62965911/219867979-419b16d3-c443-4769-8963-5a1a1c1f170c.png)

![content-concepts-raw-amazon-personalize-untitled-60](https://user-images.githubusercontent.com/62965911/219867986-ac2019ab-9fd9-4d86-989b-62b9d589a236.png)

```python
get_recommendations_response = personalize_runtime.get_recommendations(
        campaignArn = campaign_arn,
        userId = user_id
)

item_list = get_recommendations_response['itemList']
recommendation_list = []
for item in item_list:
    item_id = get_movie_by_id(item['itemId'])
recommendation_list.append(item_id)
```

![content-concepts-raw-amazon-personalize-untitled-61](https://user-images.githubusercontent.com/62965911/219867987-a7596579-fc72-47d7-bd4a-36b741f6e026.png)

## Amazon Personalize consists of three components:

- Amazon Personalize – used to create, manage and deploy solution versions.
- Amazon Personalize events – used to record user events for training data.
- Amazon Personalize Runtime – used to get recommendations from a campaign.

Amazon Personalize can utilize real time user event data and process it individually or combined with historical data to produce more accurate and relevant recommendations. Unlike historical data, new recorded data is used automatically when getting recommendations. Minimum requirements for new user data are:

- 1,000 records of combined interaction data
- 25 unique users with a minimum of 2 interactions each

## References

1. [Keynote 6: Personalization For The World - Anoop Deoras (Amazon)](https://youtu.be/2s7vUQDQPNY?list=PLL0J-WXH0lL6gV50tYSkJPv-irCkA9ods) `video`

Amazon Personalize is a fully managed machine learning service that goes beyond rigid static rule based recommendation systems and trains, tunes, and deploys custom ML models to deliver highly customized recommendations to customers across industries such as retail and media and entertainment.

It covers 6 use-cases:

![content-concepts-raw-amazon-personalize-untitled-16](https://user-images.githubusercontent.com/62965911/219867857-81a5b64c-1c1f-40fa-af93-78484ec8bb9a.png)

Popular Use-cases

![content-concepts-raw-amazon-personalize-untitled-48](https://user-images.githubusercontent.com/62965911/219867957-eaecd042-c6d2-4b8e-bb7e-180c5b6aa82a.png)

Following are the hands-on tutorials:

1. [Data Science on AWS Workshop - Personalize Recommendations**p**](https://github.com/data-science-on-aws/workshop/tree/937f6e4fed53fcc6c22bfac42c2c18a687317995/oreilly_book/02_usecases/personalize_recommendations)
2. [https://aws.amazon.com/blogs/machine-learning/creating-a-recommendation-engine-using-amazon-personalize/](https://aws.amazon.com/blogs/machine-learning/creating-a-recommendation-engine-using-amazon-personalize/)
3. [https://aws.amazon.com/blogs/machine-learning/omnichannel-personalization-with-amazon-personalize/](https://aws.amazon.com/blogs/machine-learning/omnichannel-personalization-with-amazon-personalize/)
4. [https://aws.amazon.com/blogs/machine-learning/using-a-b-testing-to-measure-the-efficacy-of-recommendations-generated-by-amazon-personalize/](https://aws.amazon.com/blogs/machine-learning/using-a-b-testing-to-measure-the-efficacy-of-recommendations-generated-by-amazon-personalize/)

Also checkout these resources:

1. [https://www.youtube.com/playlist?list=PLN7ADELDRRhiQB9QkFiZolioeJZb3wqPE](https://www.youtube.com/playlist?list=PLN7ADELDRRhiQB9QkFiZolioeJZb3wqPE)

![content-concepts-raw-amazon-personalize-untitled-62](https://user-images.githubusercontent.com/62965911/219867990-84f50e3f-8106-47bd-b63c-0dc044c37198.png)
