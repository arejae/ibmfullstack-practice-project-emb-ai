import json
from sentiment_analysis import sentiment_analyzer
response = sentiment_analyzer("I love this new technology")
formatted_response = json.loads(response)
print(formatted_response)

response = sentiment_analyzer("I hate this new technology")