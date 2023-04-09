# Video Sharing Analysis

## Goal

The company of this challenge allows users to upload videos online, just like YouTube.

This company is interested in knowing whether a video is “hot” (i.e. trending up in terms of popularity), stable or going down. Understanding this would allow to optimize the videos promoted on the home-page and, therefore, maximize ads revenue.

## Challenge Description

Company XYZ is an online video streaming company, just like YouTube or Dailymotion.

The Head of Product has identified as a major problem for the site a very high home page drop-off rate. That is, users come to the home-page and then leave the site without taking any action or watching any video.  
Since customer acquisition costs are very high, this is a huge problem: the company is spending a lot of money to acquire users who don’t generate any revenue by clicking on ads.

Currently, the videos shown on the home page to new users are manually chosen. The Head of Product had this idea of creating a new recommended video section on the home page.

He asked you the following:

- Classify each video into one these 3 categories:
    - ”Hot” - means trending up. These videos are candidate to be shown.
    - “Stable and Popular” - video view counts are flat, but very high. These videos are candidates to be shown too.
    - “Everything else” - these videos won’t be shown.  
- What are the main characteristics of the “hot videos”?
- After having identified the characteristics of the hot videos, how would you use this information from a product standpoint?

## Data

We have 2 tables:

**video_count** - provides information about how many times each video was seen each day.

**Columns:**

- **video_id** : video id, unique by video and joinable to the video id in the other table
- **count** : total count of views for each video
- **date** : on which day that video was watched that many times

**video_features** - characteristics of the video.

**Columns:**

- **video_id** : video id, unique by video and joinable to the video id in the other table
- **video_length** : length of the video in seconds
- **video_language** : language of the video, as selected by the user when she uploaded the video
- **video_upload_date** : when the video was uploaded
- **video_quality** : quality of the video. It can be \[ 240p, 360p, 480p, 720p, 1080p\]

## Solution

[![nbviewer](https://camo.githubusercontent.com/a2b8b49ec63c501c07f7f5d73ced6fdee58a337609d4a6962d6ec5b4fbd3fec9/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f72656e6465722d6e627669657765722d6f72616e67652e737667)](https://nbviewer.org/gist/sparsh-ai/061621635fbd033a9e8dbca8361abc41)
