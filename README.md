# Tweets2Stance_dataset
This dataset refers to [Tweets2Stance: Users stance detection exploiting Zero-Shot Learning Algorithms on Tweets](https://arxiv.org/abs/2204.10710)
Raw datasets D<sub>i</sub> used for Tweets2Stance (Italian Political Elections May 26, 2019). D<sub>i</sub> contains _i_ months of tweets

|            | D<sub>3</sub>            |      D<sub>4</sub>       |      D<sub>5</sub>       |      D<sub>7</sub>       |
|:----------:|:-------------------------|:------------------------:|:------------------------:|:------------------------:|
|   Period   | [2019-03-01, 2019-05-25] | [2019-02-01, 2019-05-25] | [2019-01-01, 2019-05-25] | [2018-11-01, 2019-05-25] |
|  # tweets  | 20'266                   |          25'979          |          34'736          |          44'370          |


Each dataset is saved into a `.pkl` file that you can open through the `load_pickle()` method in `utils.py`. The pickle file contains a pandas dataframe having the following structure:

|       | created_at | tweet_id | user_id | user_screen_name | tweet | referenced_tweets | str_referenced_tweets |
|:-----:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|:----------:|
|type   |str         |str         |str         |str         |str         |list         |str         |
|example|2019-05-24T16:52:24.000Z| 1234| 1235| pippo| This is a tweet| [{"id": 1236, "type": "retweeted"}...]| '[{"id": 1236, "type": "retweeted"}...]'

Tweets were downloaded using the Twitter API V2.0, then refer to [the documentation](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet) for further info about the `referenced_tweets` field. In our study, we used every type of tweet.

The `dict_ground_of_truth_VAA_Italy_2019.pkl` file contains the ground of truth for each political party and socio-political sentence. The mapping is the following:

|Stance|Value|
|------|-----|
|Completely Disagree | 1 |
|Disagree | 2 |
|Neither Disagree, Nor Agree | 3 |
|Agree| 4 |
|Completely Agree | 5|


If you have any trouble or question, please let me know at `m.gambini@iit.cnr.it`
