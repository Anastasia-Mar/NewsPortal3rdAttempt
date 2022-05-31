from django import template


register = template.Library()


bad_words = []


@register.filter()
def censor(text):
    if not isinstance(text, str):
        raise ValueError("Cannot censor this line")

    for word in bad_words:
        text = text.replace(word[1:], '*'*(len(word)-1))
    return text
