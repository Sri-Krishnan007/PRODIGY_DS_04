# PRODIGY_DS_04: Sentiment Analysis with Twitter Data

## Overview

PRODIGY_DS_04 is a data science project focused on conducting sentiment analysis using Twitter data. This project extracts tweets, processes the text data, and applies machine learning/NLP techniques to determine the sentiment (positive, negative, or neutral) expressed in tweets.

## Features

- Fetch tweets using Twitter API
- Preprocess and clean tweet text
- Analyze sentiment using NLP models
- Visualize sentiment distribution

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/Sri-Krishnan007/PRODIGY_DS_04.git
    cd PRODIGY_DS_04
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Set up your Twitter API credentials (see `config.py` or `.env` file for details).
2. Run the main analysis script:
    ```bash
    python sentiment_analysis.py
    ```
3. View output results and visualizations in the `output/` directory.

## Project Structure

- `sentiment_analysis.py` — Main script for running sentiment analysis.
- `data/` — Folder to store raw and processed data.
- `output/` — Visualizations and result files.
- `requirements.txt` — Python dependencies.

## Requirements

- Python 3.x
- Tweepy or snscrape (for fetching tweets)
- pandas, numpy
- scikit-learn
- nltk or TextBlob
- matplotlib or seaborn

## Example

```python
# Example: Analyzing the sentiment of tweets about "AI"
python sentiment_analysis.py --query "AI" --count 100
```

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.

## Contact

For questions or suggestions, contact [Sri-Krishnan007](https://github.com/Sri-Krishnan007).
