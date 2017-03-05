# # Imports the Google Cloud client library
from google.cloud import language

# Instantiates a client
language_client = language.Client()

# The text to analyze
text = 'Hello, world!'
document = language_client.document_from_text(text)

# Detects the sentiment of the text
sentiment = document.analyze_sentiment()

print('Text: {}'.format(text))
print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))


# import pip
# installed_packages = pip.get_installed_distributions()
# installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
#      for i in installed_packages])
# print(installed_packages_list)
