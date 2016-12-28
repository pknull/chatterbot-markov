from __future__ import unicode_literals
from chatterbot.conversation import Statement
from chatterbot.logic.best_match import BestMatch

import markovify
import os


class MarkovAdapter(BestMatch):
    def __init__(self, **kwargs):
        super(MarkovAdapter, self).__init__(**kwargs)

        self.confidence_threshold = kwargs.get('threshold', 0.6)
        self.default_response = kwargs.get(
            'default_response',
            "I'm learning..."
        )

    def process(self, input_statement):
        """
        Return a default response with a high confidence if
        a high confidence response is not known.
        """
        # Select the closest match to the input statement
        confidence, closest_match = self.get(input_statement)

        self.add_to_brain(input_statement.text)
        self.text_model = self.load_brain()
        # Confidence should be high only if it is less than the threshold
        if confidence < self.confidence_threshold:
            confidence = 1
        else:
            confidence = 0

        if confidence:
            output = self.generate_sentence()
        else:
            output = None

        if output is None:
            output = self.default_response

        return confidence, Statement(output)


    def add_to_brain(self, msg):
        f = open('training_text.txt', 'a')
        f.write(str(msg) + '\n')
        f.close()

    def generate_sentence(self):
        return self.text_model.make_short_sentence(300)

    def load_brain(self):
        if os.path.exists('training_text.txt'):
            with open("training_text.txt") as f:
                text = f.read()
            print('Brain Reloaded')
            f.close()
            return markovify.NewlineText(text)
