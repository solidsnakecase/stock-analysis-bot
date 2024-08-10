# Stock Analysis Bot

## Purpose

This originally was intended to be a full dividend growth stock picker based on Gordon Growth, but due to limitations of the free tier API, I decided to repurpose the code to help perform analysis of individual stock tickers instead.<p>

~~The API it is based around is provided by AlphaVantage, and is only designed for informative purposes only.  As such, the free tier API is limited to 25 Calls/day.  If you find the bot helpful, feel free to subscribe to their API for a higher daily limit.~~<p>

**I started using the yfinance library instead which has a 2000 Call/hour limit, much more than needed for this project with no API key necessary.  It still does not fully meet my needs for the dividend training boy mentioned earlier, but for this repo it works perfectly.  Even though there are more than enough calls for this project, I implemented caching all the same.**<p>

Initially, I had intended to provide both a ChatGPT description of each choice, as well as provide an option for a web browser that shows the potential performance of the stock, but this is now out of scope as now this bot does not serve the purposes I need anymore due to the changes, and my time is rather restricted due to other priorities.<p>

I will, however, provide the jupyter notebook in lieu of a website, in order to provide a visual representation of the data if you so choose.  However, this will not be able to be run through the docker container, and you will probably need to install the dependencies through poetry (or manually) in order to view the notebook.<p>

I hope you find it informative, as I will be using the model created from this repo in other projects myself, and hope that by making it public it may provide some use.<p>

### Roadmap
- Complete MVP
    1. ~~Perform/Complete EDA Notebook~~
    2. Update/Complete Pipeline
    3. Transfer to Model
    4. Modify .conf
    5. Complete main.py
- Create new Dockerfile
- Error Handling
- Model Options/Improvements

### Observations

The predictive analysis so far seems to only perform well under a bull market.  There has been a few large down days within the last few weeks, and it seems as though for tech stocks, the predictive analysis is substantially diminished.

