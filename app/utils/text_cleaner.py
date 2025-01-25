import re
import emoji

def clean_text(text):
    # Remove extra newlines and whitespace
    text = re.sub(r'\n+', '\n', text)
    text = re.sub(r'\s+', ' ', text)
    
    # Remove hyphenation
    text = re.sub(r'(\w+)-\n(\w+)', r'\1\2', text)
    
    # Remove emojis
    text = emoji.replace_emoji(text, '')
    
    # Remove special characters (keep alphanumeric, spaces, and basic punctuation)
    text = re.sub(r'[^a-zA-Z0-9\s.,!?]', '', text)
    
    return text.strip()