# Sample Data - Mocked for Demonstration Purposes
translations_data = {
    'apple': {'Spanish': 'manzana', 'French': 'pomme'},
    'love': {'French': 'amour', 'Spanish': 'amor'}
}

synonyms_data = {
    'quick': {'English': ['fast', 'rapid', 'speedy', 'swift']},
    'amour': {'French': ['passion', 'affection', 'tendresse']}
}

pronunciation_data = {
    'joie': {'French': '[ʒwa]'},
    'apple': {'English': '[ˈæpəl]'}
}

etymology_data = {
    'psychology': "Derived from Greek ψυχή (psukhḗ, 'soul') + -λογία (-logía, 'study of').",
    'love': "Originates from Old English 'lufu' and is related to 'lief,' meaning 'dear.'"
}

# Functions for Bot Commands

def translate(word, target_language):
    """Fetches the translation of a word into a target language."""
    translation = translations_data.get(word, {}).get(target_language)
    if translation:
        return f"Translation of '{word}' in {target_language}: {translation}"
    else:
        return f"No translation found for '{word}' in {target_language}."

def synonym(word, language):
    """Fetches synonyms of a word in a specified language."""
    synonym_list = synonyms_data.get(word, {}).get(language)
    if synonym_list:
        synonyms = ', '.join(synonym_list)
        return f"Synonyms for '{word}' in {language}: {synonyms}"
    else:
        return f"No synonyms found for '{word}' in {language}."

def translate_and_synonym(word, target_language):
    """Fetches both translation and synonyms of a word in a target language."""
    translation = translations_data.get(word, {}).get(target_language)
    synonym_list = synonyms_data.get(translation, {}).get(target_language)
    result = ""
    
    if translation:
        result += f"Translation of '{word}' in {target_language}: {translation}\n"
    else:
        result += f"No translation found for '{word}' in {target_language}.\n"
    
    if synonym_list:
        synonyms = ', '.join(synonym_list)
        result += f"Synonyms for '{translation}' in {target_language}: {synonyms}"
    else:
        result += f"No synonyms found for '{translation}' in {target_language}."
    
    return result

def pronounce(word, language):
    """Fetches the pronunciation of a word in a specified language."""
    pronunciation = pronunciation_data.get(word, {}).get(language)
    if pronunciation:
        return f"Pronunciation of '{word}' in {language}: {pronunciation}"
    else:
        return f"No pronunciation found for '{word}' in {language}."

def etymology(word):
    """Fetches the etymology of a word."""
    etymology_info = etymology_data.get(word)
    if etymology_info:
        return f"Etymology of '{word}': {etymology_info}"
    else:
        return f"No etymology found for '{word}'."

# Example Usage
print(translate("apple", "Spanish"))
print(synonym("quick", "English"))
print(translate_and_synonym("love", "French"))
print(pronounce("joie", "French"))
print(etymology("psychology"))



# Explanation of Code
# Mock Data: We use dictionaries to store translations, synonyms, pronunciation, and etymology. This simulates data you might get from Wiktionary.

# Functions:

# translate(word, target_language): Retrieves the translation of word in target_language.
# synonym(word, language): Retrieves synonyms of word in language.
# translate_and_synonym(word, target_language): Combines translation and synonym retrieval for word in target_language.
# pronounce(word, language): Retrieves pronunciation for word in language.
# etymology(word): Retrieves etymology of word.
# Example Usage: At the end, we demonstrate how these functions work.

# This structure allows easy extension to more languages and words. In a production environment, API access or web scraping would replace the mock data. If web scraping is an option, BeautifulSoup could parse the Wiktionary HTML to fetch this information dynamically.