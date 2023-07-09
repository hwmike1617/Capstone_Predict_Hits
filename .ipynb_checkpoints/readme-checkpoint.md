# Capstone Problem Statement and Dataset

## Problem Statement

Although the Singapore music scene is diverse and draws influences from various cultures and genres, the success of the local English music scene with American and European audiences, such as The Sam Willows, has been limited.

The objective of this project is to create a machine learning model that can predict the probability of a new song becoming a Billboard big hit by scrutinizing particular audio characteristics and lyrics from past hit songs.

The machine learning model developed in this project could help solve the challenge of predicting the commercial success of new songs in the Singapore music industry. By analyzing specific audio features and lyrics from past hit songs, the model can provide insights into what attributes make a song successful and predict the likelihood of a new song becoming a hit. This can be valuable information for music producers, artists, and record labels, as it can help them make more informed decisions about which songs to invest time and resources in promoting and marketing, potentially leading to more successful and profitable releases. Overall, the model could help improve the efficiency and effectiveness of the music industry in Singapore by reducing the risk associated with releasing new music.


## Methods and Models
The project will begin by identifying the unique audio characteristics and lyrics of past Billboard Top Ten hit songs and building a dataset of these features for training the model. 
The audio features will scrapped from Spotify API.
The lyrics will bebscrapped from Genius API.

The preprocessing tools will be:-
- goose for tokenizing of the lyrics.

Models used tentatively Naive-Bayes, Random Forest, CNN.
The model will be evaluated using established performance metrics such as accuracy, precision, and AUC to assess its ability to predict hit songs. The project will conclude by discussing the potential of the developed model to accurately predict the success of new, previously unseen songs and explaining why the model has the potential to make accurate predictions.

## Risks and Assumptions
There is currently no charts in the world that says a song is a dud or not a hit. So the assumption here will be using the number of weeks a song stays in the Billboard Top Ten charts as a predicator of success or not.

## Data Source
- Billboard Top Ten charts scrapped from Wikipedia.
- Audio Features from Spotify.
- Lyrics from Genius API.

## Target Audience
This project will provide valuable insights to the music industry, record labels, artists, and streaming services, enabling them to make more informed decisions about the potential success of new songs. The primary stakeholders of this project are music industry professionals who require accurate predictions of successful songs for business decisions. The secondary stakeholders are music enthusiasts and data scientists interested in the application of machine learning to the music industry. The project will consider both current and past trends in the music industry to ensure that the model is relevant and accurate.

## Project Milestone
<img src="CapstoneMilestone.png"></img>