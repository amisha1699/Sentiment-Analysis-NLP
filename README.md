# Sentiment-Analysis-NLP
This project analyzes the sentiment of Twitter/Reddit posts on a specific topic using sentiment analysis techniques. It preprocesses the posts, calculates sentiment scores, labels them as positive or negative, and visualizes the results with various plots. Additionally, it generates a word cloud of the most common words in the posts.

## Features
- **Retrievs Posts**: The script uses Reddit's/Twitter's API to retrieve 100 posts related the specific topic.
- **Preprocessing**: Cleans and preprocesses the posts by removing stop words, URLs, and unwanted characters.
- **Sentiment Analysis**: Analyzes the sentiment of Reddit posts using TextBlob.
- **CSV Export**: Saves the posts, sentiment scores, labels, and timestamps to a CSV file.
- **Visualization**: Provides scatter plots of sentiment scores, a time-series plot of average sentiment, and a word cloud of common words.

## Requirements
- `Python 3.x`
- `praw`
- `tweepy`
- `nltk`
- `textblob`
- `matplotlib`
- `wordcloud`
- `pandas`

Additionally a twitter/reddit developer account is required. The twitter API is not free to use, so the script was tested using Reddit's API.

## Usage
1. Clone the repository:
   ```git clone https://github.com/your-username/reddit-sentiment-analysis.git
   cd reddit-sentiment-analysis
   ```

2. Install the required python packages
    ```pip install -r requirements.txt```

3. Set up your Reddit/Twitter API credentials:
    For Reddit:
    * Create a Reddit app at [Reddit](https://www.reddit.com/prefs/apps).
    * Update the findPosts function with your client_id, client_secret, and user_agent.

