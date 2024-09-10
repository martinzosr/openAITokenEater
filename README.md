# openAITokenEater
The main goal of this project is to eat/waste/spend as much openai tokens as possible in shortest time.

USE CAUTION: BE SURE, YOU HAVE RIGHT TOKEN!

THIS SCRIPT JUST BURNS MONEY! I am not responsible if you loose money, that is the point!

##Explanation:
OpenAI and their tokens does not need to be introduced. What may need to be introduced are their tier lists. Basically, to get to higher tier, you need to spend at least x amount of money. And if your tier is too low, your api limits are horrendous.

So if you debug your application on your personal API token, and after a lot of debugs and tests you want to use company token, you might need to spend some company money to get better api limits first. But your only option is to use the money in tokens.

Note: I would love to spend the company money in meaningful way. I am sure there are a lot of great projects that coudl benefit from a few milion free tokens. But you do not want to provide your api key to 3rd party, and it would take some time to find right project, run it on my machine and send the results.

##Inner workings:
You set your api key and number of tokens you want to burn (it can overshoot it for cost of one question, aroudn 8000 tokens).

This application makes random string, send it to chatGPT-4 with instruction - answer OK. In the chatGPT answer, there is total number of tokens, that the call has spend. This number is added to already spent tokens, and if already spent token is lower than goal number of tokens, this call is run again.

You should even see nice progress bar in terminal.


This script is able to spend around 1$/min on my machine.
