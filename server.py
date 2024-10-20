"""
This module creates a Flask web server that performs sentiment analysis
using the `sentiment_analyzer` function from the SentimentAnalysis package.

Routes:
    /sentimentAnalyzer: Analyzes the sentiment of the provided text.
    /: Renders the index page.
"""
from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

# Initiate the Flask app
app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    """
    Analyze the sentiment of the provided text.

    Returns:
        A string with the sentiment label and score, or an error message if the input is invalid.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = sentiment_analyzer(text_to_analyze)

    # Extract the label and score from the response
    label = response['label']
    score = response['score']

    # Check if the label is None, indicating an error or invalid input
    if label is None:
        return "Invalid input! Try again."

    # Return a formatted string with the sentiment label and score
    return f"The given text has been identified as {label.split('_')[1]} with a score of {score}."

@app.route("/")
def render_index_page():
    """
    Render the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
