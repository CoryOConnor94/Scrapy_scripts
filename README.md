# Various Scrapy projects

## Worldometer Scraper

This is a Scrapy project that scrapes population data from Worldometer. The spider follows links to individual country pages and extracts yearly population statistics.

## Project Structure

```
worldometer_scraping_project/
│── scrapy.cfg
│── worldometer_scraping_project/
│   ├── __init__.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   └── spiders/
│       ├── __init__.py
│       ├── worldometer.py
│── .gitignore
│── README.md
```

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/worldometer_scraping_project.git
   cd worldometer_scraping_project
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## How It Works

### **Spider: `worldometer`**

- **Start URL:** `https://www.worldometers.info/world-population/population-by-country`
- **Extracts country names and their links.**
- **Follows links to individual country pages** and scrapes population data by year.
- **Outputs data in JSON format.**

## Running the Scraper

To run the spider, use the following command:
```bash
scrapy crawl worldometer -o population_data.json
```

This will scrape the data and store it in `population_data.json`.

## Output Example

```json
[
    {
        "Country": "United States",
        "Year": "2023",
        "Population": "331,002,651"
    },
    {
        "Country": "China",
        "Year": "2023",
        "Population": "1,439,323,776"
    }
]
```

## Customizing the Spider

- Modify the `start_urls` list in `worldometer.py` to scrape other pages.
- Adjust XPath selectors if Worldometer's website structure changes.

--------------------

## Audible Scraper

This is a Scrapy spider designed to scrape audiobook data from Audible UK. The spider extracts audiobook titles, authors, lengths, and navigates through multiple pages.

## Project Structure

```
audible_scraper/
│── scrapy.cfg
│── audible_scraper/
│   ├── __init__.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   └── spiders/
│       ├── __init__.py
│       ├── audible_spider.py
│── .gitignore
│── README.md
```

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/audible_scraper.git
   cd audible_scraper
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## How It Works

### **Spider: `audible_spider`**

- **Start URL:** `https://www.audible.co.uk/search`
- **Extracts audiobook information:**
  - Title
  - Author(s)
  - Length
- **Handles pagination:**
  - Follows the "Next" button until the last page.
- **Uses a custom User-Agent** to mimic a browser request.

## Running the Scraper

To run the spider and save the output to a CSV file:
```bash
scrapy crawl audible_spider -o audible_data.csv
```

## Output Example

```csv
Title,Author,Length
"The Hobbit","J.R.R. Tolkien","11 hrs and 5 mins"
"1984","George Orwell","12 hrs and 10 mins"
```

## Customizing the Spider

- Modify the `start_requests` method to scrape a different Audible page.
- Update the XPath selectors if Audible changes its website structure.

## License

This project is licensed under the MIT License.

---

Feel free to contribute or report issues!

