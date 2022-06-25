from bs4 import BeautifulSoup


stopWords = [
    "#", "##", "a", "about", "above", "after", "again", "against", "all", "am",
    "an", "and", "any", "are", "aren't", "as", "at", "be", "because", "been",
    "before", "being", "below", "between", "both", "but", "by", "can't", "cannot",
    "could", "couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't",
    "down", "during", "each", "few", "for", "from", "further", "had", "hadn't",
    "has", "hasn't", "have", "haven't", "having", "he", "he'd", "he'll", "he's",
    "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how",
    "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "isn't",
    "it", "it's", "its", "itself", "let's", "me", "more", "most", "mustn't", "my",
    "myself", "no", "nor", "not", "of", "off", "on", "once", "only", "or", "other",
    "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "shan't", "she",
    "she'd", "she'll", "she's", "should", "shouldn't", "so", "some", "such", "than", "that",
    "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's",
    "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through",
    "to", "too", "under", "until", "up", "very", "was", "wasn't", "we", "we'd", "we'll",
    "we're", "we've", "were", "weren't", "what", "what's", "when", "when's", "where",
    "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "won't",
    "would", "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your", "yours",
    "yourself", "yourselves"
]


def tags(html):
    """
    Return a list of tags from the HTML.
    """

    # Strip the HTML tags and punctuation and make a list of words
    soup = BeautifulSoup(html, "html.parser")
    content = soup.get_text().lower().replace(".", "").replace(",", "").replace("(", "").replace(")", "").replace("-", " ").replace("?", "").replace("!", "")
    content = content.split()

    # Remove duplicates from tags list
    words = list(dict.fromkeys(content))

    # Remove stopwords
    words = [word for word in words if word not in stopWords]

    # Remove non-alpha-numeric words
    words = [word for word in words if word.isalpha()]

    # Get the 5 most used words
    tagCount = list(map(lambda x: [x, content.count(x)], words))
    tagCount.sort(key=lambda x: x[1], reverse=True)
    tagCount = tagCount[:5]

    result = list(map(lambda x: x[0], tagCount))
    return result





def fixUnicode(text):
    """
    Replace the unicode characters which don't diplay properly in the browser with their nearest ASCII equivalents.
    """
    return text.replace("\u00e2\u20ac\u2122", "'").replace("\u00e2\u20ac\u201c", "-").replace("\u00c3\u00a9", "e")