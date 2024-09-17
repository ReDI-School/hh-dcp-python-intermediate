# Exercise: 5 - String Manipulation

Print the length of the following text:

    ChatGPT (short for Chat Generative Pre-trained Transformer) is a chatbot. It was launched by OpenAI in November 2022. The program is built on top of OpenAI's GPT-3.5 family of large language models. It is fine-tuned with both supervised and reinforcement learning techniques.
    ChatGPT was launched as a prototype on November 30, 2022. The website had more than one billion users after five days. By January 2023, ChatGPT reached over 100 million users. It got attention for its responses and answers in many areas of knowledge. Its uneven accuracy was said to be a major drawback.
    As of December 2022, the chatbot was a 'Research Preview' according to its website. While the chatbot is free to use, there have been announcements and rumours over a paid version called ChatGPT Professional. The website also warns users that the bot may give wrong information or have biased content.

* How many times the small letter "a", "t" and "r" appear in the following text? 
* Print it to the console using string formatting (Format: "The letter 'a' appears x times.")
* Transform the whole text to capital letters and count how many times the capital letter "C" appears in the text. 
* Print it to the console using string formatting (Format: "The letter 'C' appears x times.")
* Remove all punctuation marks (e.g. !;,.')() from the text and print it to the console. 
* You can use the built-in library from python called string. This library has a list of commonly used built-in punctuation characters string.punctuation. To replace the punctuation characters from specific string, you can use the str.replace(old_character, new_character) function.****

## Hints:

* Use for-loop to iterate over the text
* Use str.upper() function to transform the text to capital letters
* Use f-strings or str.format() function to format the string
* To avoid yellow highlighting use import string to import the built-in string library before using string.punctuation