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

# Go up two levels to save the data
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
DATA_DIR = os.path.join(BASE_DIR, 'data')

FEEDS = {
    os.path.join(DATA_DIR, 'ticketdata.json'): {'format': 'json', 'overwrite': True}
}

ADDONS = {}

SCRAPEOPS_API_KEY = os.getenv("SCRAPEOPS_API_KEY")
SCRAPEOPS_PROXY_ENABLED = True

# SCRAPEOPS_PROXY_LIST = [
#     '189.201.191.67:4145',
#     '177.105.68.123:4153',
#     '43.134.164.175:443',
# ]

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
#    'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
#    'rotating_proxies.middlewares.BanDetectionMiddleware': 620
    'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk': 725,
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
   "scrappingtickets.pipelines.SaveToPostgreSQLPipeline": 400,
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

# PLAYWRIGHT_LAUNCH_OPTIONS = {
#     "headless": True,
#     "proxy": {
#         "server": "http://proxy.scrapeops.io:5353",
#         "username": "scrapeops",
#         "password": os.getenv("SCRAPEOPS_API_KEY"),
#     },
# }

# PLAYWRIGHT_CONTEXTS = {
#     "default": {
#         "ignore_https_errors": True,
#     }
# }

# import requests

# response = requests.get(
# url='https://proxy.scrapeops.io/v1/',
# params={
#         'api_key': 'e92cce3a-caab-456c-b47f-ad618573e305',
#         'url': 'https://quotes.toscrape.com', 
#     },
# )

# print('Response Body: ', response.content)
        
