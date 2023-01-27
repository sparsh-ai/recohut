# Spotify Discover Weekly Playlist

This case study uses information from various presentations that engineers from Spotify delivered in 2015, mainly the “[From Idea to Execution: Spotify’s Discover Weekly](https://oreil.ly/Njos2)” presentation. They may no longer use some of the techniques or technologies discussed, but the core takeaways from this case study are still relevant.

Spotify is one of the biggest brands in the music industry right now after revolutionizing the way people listen to their favorite music in the modern world. It’s also no secret that their key to success is their impressive use of data to keep users coming back to the service by making new music discovery seamless.

One of the key features that users love, and which keeps users coming back to the platform week after week, is their Discover Weekly playlist. The Discover Weekly playlist is a heavily personalized playlist that is curated using data and delivered to every user on the platform each week. This personalized touch and ability to provide new, relevant music to each user on the platform on a weekly basis is unique and is only made possible through solid data engineering backing up amazing data science models. This section will walk through each of the data engineering topics discussed in this report and how they apply to Discover Weekly playlist curation.

## Extraction and Real Time

When Spotify published their quarterly statement in fiscal quarter 1 (Q1) of 2019 they had 217 million active users per month (as seen in Figure). Each of these users performs searches, listens to songs, skips tracks, curates playlists, and likes songs, all from different areas of the app on a variety of different platforms.

As mentioned in the introduction to this report, this move toward capturing more granular data has been key to the success of the tech giants, because with this data they are able to better understand user behavior and make changes to support what users want. In the case of Spotify, all this log data needs to be captured, and due to the scale of the platform, they have chosen to streamline the process using data streams.

![weekly-stats](https://user-images.githubusercontent.com/62965911/215029091-e87addc1-15f7-42ba-ad53-6e01a0db8d8c.png)

Log data is fed onto an Apache Kafka queue so it can be processed downstream and extracted into a data lake. This is a consistently open queue that allows the logs to be streamed directly into the data warehouse. This heavily reduces the amount of time between logs being recorded to logs becoming useful. Due to the sheer volume, it also alleviates speed issues with batching this amount of data and copying it over. Even copying batches of this data in hourly intervals for a platform producing data at Spotify’s scale would be a mammoth task.

This means that most of the data extraction that takes place is via consumers of the Apache Kafka queues as these queues can directly output data into the data warehouse. On top of the data produced by the platform itself they also have metadata about albums and tracks that are added when artists upload music, and they also extract text data from blogs, news stories, and other online sources—and even song lyrics. These tasks can be performed in isolation from the main Kafka pipeline, and although they don’t specifically say how this is done, you can imagine this data is pulled at frequent intervals during the day from various APIs or using web-scraping techniques.

You can see that just managing the logistics of the log data being produced by users of the application is a huge piece of the data engineering in itself and is something that even 10 years ago would have seemed too expensive and practically impossible based on the way data systems were architected at that time.

Now, thanks to the scalability of modern queue platforms such as Kafka, a business producing logs to the scale of Spotify can get access to this data in near–real time, decreasing the time to insight and all at a relatively small price.

## Transformation

Now that we know that the raw log data from the platform is being fed into the data warehouse and is streamed via the Kafka queue, we can take a look at how Spotify transforms this into something useful.

The first thing to note is that new data is constantly being added so transformations need to be able to deal with this too. But just because data is continuously arriving doesn’t mean you have to process it in real time. In Spotify’s case the reason the data is arriving frequently is due to the size; frequent transformations on smaller data sets in this case make sense. This would keep processing times down and again speed up the time from the logs being created to them being transformed into something meaningful and usable downstream.

For Discover Weekly to work, Spotify first needs the logs transformed and data points engineered into features that are put into the model. A simple example is the use of other people’s playlists. Imagine you listened to Stronger by Kanye West and other songs that fall into that genre (in Spotify’s case songs aren’t forced into one genre and instead are tagged with multiple labels). Other users who have included that song on playlists themselves in the past week and who also listen to similar genres will likely have put songs into their playlist that you may also like.

Transforming the raw logs to better understand user playlists, listens, and favorite genres all sounds fairly reasonable and something you would expect in order for a feature like this to work; however, Spotify doesn’t stop here.

Not only do they use logs of user behavior, but natural language processing (NLP) is also used to transform raw text into something more meaningful and hopefully provide a little more context about what a song or playlist is conveying. As seen in Figure, this is performed on news and blog data that is pulled from various sources to help understand how a particular album, song, or artist is described and to again gain more insight and metadata that can be used in building better recommendations.

![kakfa](https://user-images.githubusercontent.com/62965911/215029086-f3752385-3770-4e0f-953a-7c41b096acc2.png)

This same technique is even used on playlists. Using the songs within a playlist as words, NLP can be used to try and understand more about the type of playlist based just on the names of the tracks within them. Although I don’t know the specifics of Spotify’s proprietary process, I can take an informed guess that all of this requires transforming the raw text data, via NLP, into data sets that show frequently used adjectives to describe an artist or album and to even understand the particular “feel” or emotion of a playlist based on track names.

## Load

Once the transformation has taken place and the data has made its way through the Discover Weekly recommendation model, they then need to load the playlist for each user back into the platform each week on Sunday night. Let’s see how this is done.

First of all, we need to cover where the raw data is loaded once it has been extracted from the Kafka queue. Spotify uses Hadoop as their data lake platform of choice. Hadoop is very flexible in terms of the type of data it can store. We know that the majority of the data is log data extracted from the platform, which can naturally be written to files for processing later. They also process audio files, which wouldn’t be suited to traditional database storage so the flexibility of Hadoop allows them to store their audio files alongside the rest of their data. This makes the data easily accessible for use with other data sets.

Hadoop isn’t where the final output from the data model is stored though, so let’s talk through what the final load process looks like. Loading the final output of Discover Weekly requires refreshing around 75 million playlists on a Sunday, taking time zones into account, so that come Monday morning every user has their own uniquely curated playlist of new songs. This is taking the “load” part of ETL to the next level in terms of extremity and required some clever engineering to make it happen.

Again due to scale, queues were used so that the system could be easily scaled to deal with the throughput. The recommendation system would spit out playlists onto a Rabbit MQ queue (a style of technology similar to Kafka) that would take each playlist, fetch the user’s most recent profile picture from Facebook to use as the playlist cover picture, and load them into the database where user playlists are stored. This means the recommendation system can work systematically through users to curate their playlist and add them to the queue, and the queueing system can take care of delivering the playlist to the correct user at the correct time.

As you can see, all the techniques discussed in this report play a huge role in just a single feature of Spotify. Data engineering is used not only to bring data into a data warehouse, but to do it efficiently at scale, where it can be used within machine learning and AI models that are then also engineered into a data pipeline to recommend playlists and deliver them to users consistently, week after week.

These modern data engineering techniques, paired with data science, are what move businesses away from simply understanding what is happening to predicting and dictating what happens next. At Spotify this all happens because of readily scalable architectures that can ingest and quickly materialize raw data into insights of user behavior. This is where most businesses would stop as they now have insight of what their users are doing. What Spotify has successfully done here is take the understanding of what users are doing to help them do more, by providing new but relevant music that keeps them coming back to the platform.