# gpu-scraper
A python script for scraping prices of GPUs.
Miners and fellow gamers are welcome.

# Features
* Scraping names of Allegro Lokalnie offers
* Scraping prices of GPUs
* Scraping current profitability
* Calculating GPU's RoI based on its price and current profitability
# How to use it
### Install
`git clone https://github.com/karolproksa/gpu-scraper` <br>
`cd gpu-scraper` <br>
`pip install selenium` <br>
### Run
`python gpu-scraper.py`
> Make sure you're in the gpu-scraper/ directory

# To Do
* Find a way to avoid hitting Allegro's rate limit
* Add support for Allegro, not just Allegro Lokalnie
* Scrape links for easier access

# Limitations
Currently the biggest limitation is Allegro's rate limit. Because of that, usually the last 2 or 3 GPU types will not scrape. I haven't figured out a way to avoid that yet, so for now I'll leave it as is. 
If the GPUs you're looking for didn't show up on the screen after running the script, then you can edit the file `gpu-scraper.py` and comment out a few last lines (there are instuctions in the file on how you should do it).

