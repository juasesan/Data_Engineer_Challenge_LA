import emoji


def first_mode(series):
    """"
    Obtiene el valor más común dentro de una serie (moda)
    Args:
        series: Serie de valores
    Returns:
        El valor de moda
    """
    return series.mode().iloc[0]


def extract_emojis(tweet):
    """Extract emojis from a string."""
    return [match['emoji'] for match in emoji.emoji_list(tweet)]