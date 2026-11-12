# Scrapy learning spiders

Earlier Python/Scrapy exercises for extracting article and job-listing data and exporting JSON. The Scrapy project is `postscrape`; spiders live under `postscrape/spiders`.

[Current software engineering portfolio](https://amenibensaada.tn/?utm_source=github&utm_medium=profile&utm_campaign=personal_brand).

## Inspect the spiders

```sh
python3 -m venv .venv
# Activate .venv using your shell's command
pip install scrapy
scrapy list
```

Review each spider’s target, fields and selectors before using `scrapy crawl <name>`. The repository reflects historical sites/selectors; they may require updates. Existing JSON files are sample historical outputs, not current job listings. No locked Python environment or automated test suite is claimed.

Use only sites/data you are permitted to access, respect site terms and request limits, and keep extracted personal data out of newly published examples. Scrapy and dependency attribution remains with their authors.
