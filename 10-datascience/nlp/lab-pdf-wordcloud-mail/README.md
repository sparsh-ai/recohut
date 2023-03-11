# PDF to Wordcloud via Email

[![](https://img.shields.io/badge/download-notebook-blueviolet)](https://nbviewer.org/github/datalaker/jupyter/blob/main/pdf-to-wordcloud-mail.ipyn)

Receive a pdf via outlook mail and send back the wordcloud of that pdf in the reply

## Process Flow

- Step 1 - PyPDF2 library to read PDF text in Python
- Step 2 - Import the supporting libraries
- Step 3 - Count No. of Pages for this pdf and extract text for each page using loop
- Step 4 - Build Text corpus by simply attaching text of next page to all the previous ones
- Step 5 - Creating word frequency dataframe by first splitting text into words and counting the frequency of each word
- Step 6.1 - Pre-process text i.e. removing stopwords (using nltk library), grouping common words.
- Step 6.2 - Used regex to extract alphabets only, lower all chracters, and sorting as per decreasing order of frequency.
- Step 7 - Creating Wordcloud using matplotlib and wordcloud libraries
- Step 8 - Importing required libraries like smtplib, MIME, win32 for sending the mail
- Step 9 - Create outlook mail object with supporting data like filepath attachment, recepient address, mail body etc.
- Step 10 - Sending the mail with required wordcloud image file attached and checking if mail is received or not!
