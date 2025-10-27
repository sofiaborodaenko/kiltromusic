import os
from typing import override
from dotenv import load_dotenv

load_dotenv()

# Scrapy settings for scrappingtickets project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "scrappingtickets"

SPIDER_MODULES = ["scrappingtickets.spiders"]
NEWSPIDER_MODULE = "scrappingtickets.spiders"

FEEDS = {
   'ticketdata.json': {'format': 'json', 'overwrite': True}
}

ADDONS = {}

SCRAPEOPS_API_KEY = os.getenv("SCRAPEOPS_API_KEY")

SCRAPEOPS_FAKE_BROWSER_HEADER_ENDPOINT = "https://headers.scrapeops.io/v1/browser-headers"
# SCRAPEOPS_FAKE_USER_AGENTS_ENDPOINT = "https://headers.scrapeops.io/v1/user-agents"

SCRAPEOPS_FAKE_BROWSER_HEADER_ENABLED = True
# SCRAPEOPS_FAKE_USER_AGENTS_ENABLED = True

SCRAPEOPS_NUM_RESULTS = 50

if not SCRAPEOPS_API_KEY:
    raise ValueError("API key not found")


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "scrappingtickets (+http://www.yourdomain.com)"


# Obey robots.txt rules
ROBOTSTXT_OBEY = False


# Concurrency and throttling settings
#CONCURRENT_REQUESTS = 16
CONCURRENT_REQUESTS_PER_DOMAIN = 1
DOWNLOAD_DELAY = 1

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "scrappingtickets.middlewares.ScrappingticketsSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
#    "scrappingtickets.middlewares.ScrappingticketsDownloaderMiddleware": 543,
   'scrappingtickets.middlewares.ScrapeOpsFakeUserAgentMiddleware': 400,
}
# lower number has higher priority

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   "scrappingtickets.pipelines.ScrappingticketsPipeline": 300,
   "scrappingtickets.pipelines.SaveToMySQLPipeline": 400,
} 

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
FEED_EXPORT_ENCODING = "utf-8"


# Enable scrapy-playwright
DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}

TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

# Optional: adjust concurrency or page timeout
PLAYWRIGHT_BROWSER_TYPE = "chromium"

FEEDS = {
    'ticketdata.json': {'format': 'json', 'overwrite': True}
}
