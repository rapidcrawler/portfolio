import streamlit as st
from textblob import TextBlob
# import spacy

# Function to suggest emojis based on sentiment
def get_emoji_suggestions(text):
    # Analyzing the sentiment of the text using TextBlob
    sentiment = TextBlob(text).sentiment.polarity

    # Placeholder for emoji suggestions
    emoji_suggestions = ""

    # Sentiment-based emoji suggestions
    if sentiment > 0:
        emoji_suggestions += "😊 👍 🎉"  # Positive sentiment emojis
    elif sentiment < 0:
        emoji_suggestions += "😞 👎 😢"  # Negative sentiment emojis
    else:
        emoji_suggestions += "😐 🤔"  # Neutral sentiment emojis

    # # Placeholder for future entity-based emoji suggestions using spaCy
    # # Entity-based emoji suggestions
    # for entity in entities:
    #     entity_lower = entity.lower()
    #     if entity_lower in ["new york", "london", "paris", "tokyo"]:
    #         emoji_suggestions += " 🏙️"  # City emoji
    #     elif entity_lower in ["usa", "india", "france", "japan"]:
    #         emoji_suggestions += " 🇺🇸 🇮🇳 🇫🇷 🇯🇵"  # Country flags
    #     elif "phone" in entity_lower:
    #         emoji_suggestions += " 📱"  # Phone emoji
    #     elif "car" in entity_lower:
    #         emoji_suggestions += " 🚗"  # Car emoji
    #     elif "coffee" in entity_lower:
    #         emoji_suggestions += " ☕"  # Coffee emoji
    #     elif "pizza" in entity_lower:
    #         emoji_suggestions += " 🍕"  # Pizza emoji
    #     # You can add more objects and their respective emojis as needed

    return emoji_suggestions

def emoji_suggestion():
    st.title("Emoji Suggestion 😇🧐")
    
    st.divider()
    # User input text
    user_input = st.text_area("Enter your text here:")
    
    # If user has entered text, suggest emojis
    if user_input:
        suggested_emojis = get_emoji_suggestions(user_input)
        st.write(f"Suggested emojis for your text: {suggested_emojis}")
        
    st.divider()
    st.caption(":blue[Future Updates] :sunglasses:")
    st.caption(
        """
        1. Using Spacy's NER recognition to add more emojis related to object and places mentioned in the input text
        2. Replacing _Textblob with Vader_ for sentiment identification , for more precise results, specially mixture of emotions
        """
    )
    st.divider()
    # st.write("[Code Notebook](https://github.com/rapidcrawler/hobby_projects/tree/main/emoji_recommender)")

# Running the app
if __name__ == "__main__":
    emoji_suggestion()
