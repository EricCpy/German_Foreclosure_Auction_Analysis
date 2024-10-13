# German Foreclosure Auction Scraper

## Questions
## Which libs to analyze pdfs and different sites?
## Do I want to use a generalized scraper or write a scraper for each site?
## How do I scrape from Pdfs with different structures? 

### Promising **Libs**
- Scrapegraph-ai with ollama
- Marker-pdf parses pdfs to markdown

## German Foreclosure Auction Sites
- https://www.zvg-portal.de/ (official website of the german government where foreclosure auctions can be found for selected regional courts) (Effort: uniform general description, more detailed information in unstructured PDFs, which would need to be extracted)
- https://versteigerungspool.de/ (compiles foreclosures, scrapes the content of the official portal, and presents it more clearly, but sometimes lacks the full description)
- https://www.zvg-online.net/ (shows only a few foreclosures, but provides appraisals and a property exposé, presenting a lot of detailed information about the properties)
- https://www.zwangsversteigerung.de/ (does not show current auction dates, only useful for visualizing foreclosures)



## The datasets for return expectations and normal condition price prediction:
- https://www.kaggle.com/datasets/corrieaar/apartment-rental-offers-in-germany
- https://tradingeconomics.com/germany/rent-inflation
- https://de.statista.com/statistik/daten/studie/1298333/umfrage/mietenniveau-in-deutschland-nach-landkreisen/
- https://www.deutschlandatlas.bund.de/DE/Karten/Wie-wir-wohnen/040-Mieten.html
- https://www.statistikportal.de/de/veroeffentlichungen/wohnen-deutschland

