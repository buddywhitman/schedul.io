# message_parser/nlp_parser.py

import spacy

nlp = spacy.load("en_core_web_sm")

def parse_message(message):
    doc = nlp(message)

    # Placeholder variables for extracted information
    event_details = {
        'summary': '',
        'location': '',
        'description': '',
        'start_time': None,
        'end_time': None,
    }

    # Extracting relevant information using spaCy
    for entity in doc.ents:
        if entity.label_ == "DATE":
            # Extract date information
            event_details['start_time'] = entity.start
            event_details['end_time'] = entity.end
        elif entity.label_ == "EVENT":
            # Extract event title
            event_details['summary'] = entity.text
        elif entity.label_ == "GPE":
            # Extract location information
            event_details['location'] = entity.text

    # Additional logic for extracting other details like description, etc.
    # ...

    return event_details
