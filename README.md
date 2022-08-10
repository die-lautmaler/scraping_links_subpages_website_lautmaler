# scraping_links_subpages_website_lautmaler
Our own customization for scraping 1. the links that contain subpages on a website and subsequently 2. scrape all the text elements.
Find the relevant HTML elements in this spreadsheet: https://docs.google.com/spreadsheets/d/132kpiAua8ni51hm4gb3SrysMAuu7kLOlumjiJ75-itY/

### collect the links to ./links/provider.json
`python -m link_collector https://www.provider.de/glossar`

### scrape the text from the links to ./csv/provider.csv
`python -m text_collector provider .text-class`