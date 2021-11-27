# gpu-scraper
A python script for scraping prices of GPUs.
Miners and fellow gamers are welcome.

# How to use it
## Install
`git clone https://github.com/karolproksa/gpu-scraper`
`cd gpu-scraper`
`pip install selenium`
## Run
python gpu-scraper.py
> Make sure you're in the gpu-scraper/ directory

# To Do
* Calculate RoI on GPU taking their prices into account
* Find a way to avoid hitting Allegro's rate limit
* Add support for Allegro, not just Allegro Lokalnie
* Scrape links for easier access

# Limitations
Currently the biggest limitation is Allegro's rate limit. Because of that, usually the last 2 or 3 GPU types will not scrape. I haven't figured out a way to avoid that yet, so for now I'll leave it as is. 
If the GPUs you're looking for didn't show up on the screen after running the script, then you can edit the file `gpu-scraper.py` and comment out a few last lines (there are instuctions in the file how you should do it).

