import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob

# Step 2: Load Data
file_path = r'C:\Users\srikr\Desktop\COLLEGE\Extra\twitter_training.csv'
df = pd.read_csv(file_path)

# Check the column names in your dataframe
print(df.columns)

# Step 3: Perform Sentiment Analysis
def get_sentiment(text):
    if isinstance(text, str):  # Check if the value is a string
        analysis = TextBlob(text)
        return 'positive' if analysis.sentiment.polarity > 0 else 'negative' if analysis.sentiment.polarity < 0 else 'neutral'
    else:
        return 'unknown'

df['Sentiment'] = df['Tweet'].apply(get_sentiment)

# Step 4: Visualize Sentiment Distribution
plt.figure(figsize=(8, 6))
df['Sentiment'].value_counts().plot(kind='bar', color=['green', 'red', 'blue'])
plt.title('Sentiment Distribution')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.show()

# Step 5: Analyze Sentiment Over Time (if timestamp is available)
if 'Timestamp' in df.columns:
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df.set_index('Timestamp', inplace=True)

    plt.figure(figsize=(12, 8))
    df['Sentiment'].resample('D').value_counts().unstack().plot(kind='bar', stacked=True)
    plt.title('Sentiment Over Time')
    plt.xlabel('Date')
    plt.ylabel('Count')
    plt.legend(title='Sentiment')
    plt.show()
else:
    print("Timestamp column not found. Skipping sentiment over time analysis.")
