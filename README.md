# German Foreclosure Auction Scraper
This project uses python 3.12
## Questions
## Which libs to analyze pdfs and different sites?
## Do I want to use a generalized scraper or write a scraper for each site?
## How do I scrape from Pdfs with different structures? 
## What to use for Information Extraction/Named Entity Recognition?
## Do I need to use OCR?


### Promising **Libs**

- Langchain

- unstructured
  - https://colab.research.google.com/drive/1BJYYyrPVe0_9EGyXqeNyzmVZDrCRZwsg?usp=sharing

Information Extraction:
- https://www.youtube.com/watch?v=xZzvwR9jdPA
  - Langchain model, llama oder huggingface model -> muss noch getestet werden
  - Kor
  - Code: https://github.com/gkamradt/langchain-tutorials/blob/main/data_generation/Expert%20Structured%20Output%20(Using%20Kor).ipynb
  - https://mychen76.medium.com/practical-techniques-to-constraint-llm-output-in-json-format-e3e72396c670


Finetune LLM:
    - use PDFs and fine tune model https://www.youtube.com/watch?v=pxhkDaKzBaY https://www.youtube.com/watch?v=eC6Hd1hFvos
    - fine tune to generate json output?


- https://discuss.huggingface.co/t/extract-data-from-text-and-parse-it-as-a-json/64971 (https://github.com/1rgs/jsonformer)
- https://python.langchain.com/v0.1/docs/modules/model_io/output_parsers/

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

