import paralleldots

paralleldots.set_api_key('881c25d9bf8687370bd5531a9faf41bb7f63b9a8')

def ner_text(text):
    result =paralleldots.ner(text)
    return result
