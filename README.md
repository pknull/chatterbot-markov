# chatterbot-markov
A markov generator forked from the low confidence logic adapter. Effectively spewing nonsense in the face of
uncertainty.

For more information about ChatterBot see https://github.com/gunthercox/ChatterBot

Installation
------------

.. code-block:: bash

   pip install chatterbot-weather

Example
-------

.. code-block:: python

   from chatterbot import ChatBot

   chatbot = ChatBot(
       'My Weather Bot',
       logic_adapters=[
           'chatterbot-markov.WeatherLogicAdapter'
       ]
   )

Contributors Welcomed!
----------------------

This was made as a kind of fast add to keep the bot from saying something bland like "I don't know"
while still showing progression and collection of phrases passed to it via chat. However, it was written
in a late night coding session and frankly, is probably needing a bit of love.
