**Api_key:** To use this add-on, you must first set up a Google Gemini API key and configure it here. More information can be found [here](https://docs.cloud.google.com/api-keys/docs/get-started-api-keys). 

**model:** Although the gemini-2.5-flash model is set as the default, any of Google's other text models may be used. If your use-case receives incorrect questions/answers too frequently, consider using a more powerful or recent model. (ex. "gemini-2.5-pro" or "gemini-2.5-pro").

**"remix_reviewed_cards":** Determines whether this add-on will create new versions of cards as they are reviewed during normal study.

**"remix_newly_added_cards":** Determines whether this add-on will create new versions of cards as they are added via the note creator.

**Note Type Setup:** Because this add-on is only meant to work on math cards, it will require the creation of a **"MATH"** note type. This type must implement the fields **"MATH QUESTION"** and **"MATH ANSWER"**, which correspond to the question that will be modified and the answer to that. Additional fields may be added to the MATH note type, but they will not be seen or modified by the add-on.
