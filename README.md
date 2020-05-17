# Tendency Analysis on Yahoo Finance Stocks Comments (NLP-service)
## Background
To establish a NLP service Project, our group decided to analyze the trendency of comments under each stocks those performed good or bad by webcarpering Yahoo Finance. For midterm, we build up two ways to analyze comment text and fit them into SVM model. We add on webscraper service in final project.
## Preparation and Installation
To run this program properly, you need to download the appropriate version of chromedriver-exe file for webscraper use.  
This project uses pandas, sklearn, selenium and vaderSentiment. Carefully check whether they are already installed locally, before you run the program.

## Introduciton of this project
### 1.Files in this project
There are two main PY files (named Input Stock Code Here.py and craper.py) and one chromedrive.exe used during the procedure.

### 2.How to use
To run the program, you need to download all three file under the same catalog and change the address to your catalog in craper.py (There is a function called get_comment(). Just under the function and after "driver=", you will see the address.)  
Open the Input Stock Code Here.py file with any python editor and run it. Please do not do anything to the opening website, which would cause error to the webscraper. During the program processing, there will be a input require for you to type the stock code you want to analyse from the console. The program will not continue until the code already input. 

### 3.logic of this project
Initially, we picked out 25 phenomenal stocks, marking them 5 per group as "High-performing", "well-performing", "stable", "badly-performing", "horriblely performing" by looking their performing last three months.   
In order to fit SVM model, we cannot use text content to train and test, so we import TfidfVectorizer to convert words to matrixs. Then we use converted comments under those 25 stocks as traindata, converted comment of new input stocks as teatdata, fitting them into svm regression to get the score.   
After that, we apply sentiment analysis on each single test stocks comment, getting a mean score of them. Finally, we get two scores can be used to determine the trendency shown by those comments.  

## Conclusion
After testing on both well performing and badly performing stocks many times by applying our program, we find that those comments can neither help us to predict the future nor clearly show expectaion of those investors. People actually comments tons of useless words and usually driven by the price flow(showing slightly on the score).

## Contributing 
<!-- ALL-CONTRIBUTORS-LIST: START - Do not remove or modify this section -->
<!-- ALL-CONTRIBUTORS-LIST:END -->
all-contributors generate
