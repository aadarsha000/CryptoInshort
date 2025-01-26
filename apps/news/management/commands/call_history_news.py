import requests
from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError
from datetime import datetime
from config.settings import CRYPTO_NEWS_API_URL, CRYPTO_NEWS_API_KEY
from apps.news.models import CryptoNews, CryptoTricker


class Command(BaseCommand):
    help = "Call the Crypto News API and save the news to the database"

    def parse_date(self, date_str):
        """
        Parse the date string from the API response into a datetime object.
        """
        try:
            # Parse the date string in the format "Sat, 25 Jan 2025 23:45:33 -0500"
            return datetime.strptime(date_str, "%a, %d %b %Y %H:%M:%S %z")
        except ValueError as e:
            self.stdout.write(self.style.ERROR(f"Error parsing date: {e}"))
            return None

    def call_crypto_news_api(self, base_url, params):
        """
        Call the Crypto News API and save articles to the database.
        """
        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            data = response.json()
            print(data)

            articles = data.get("data", [])
            if not articles:
                self.stdout.write(self.style.WARNING("No articles found."))
                return

            for article in articles:
                if not CryptoNews.objects.filter(
                    unique_id=article["news_url"]
                ).exists():
                    # Convert sentiment to lowercase to match SENTIMENT_CHOICES
                    sentiment = article.get("sentiment", "").lower()
                    if sentiment not in dict(CryptoNews.SENTIMENT_CHOICES.choices):
                        sentiment = (
                            "neutral"  # Default to neutral if sentiment is invalid
                        )

                    # Parse the published_at date
                    published_at = self.parse_date(article["date"])
                    if not published_at:
                        continue  # Skip this article if the date is invalid

                    crypto_news = CryptoNews.objects.create(
                        unique_id=article["news_url"],
                        title=article["title"],
                        content=article.get(
                            "text", ""
                        ),  # Use .get() to avoid KeyError if "text" is missing
                        summary=article.get(
                            "summary", ""
                        ),  # Use .get() to avoid KeyError if "summary" is missing
                        source_url=article[
                            "news_url"
                        ],  # Assuming "news_url" is the source URL
                        source_name=article.get(
                            "source_name", ""
                        ),  # Use .get() to avoid KeyError if "source_name" is missing
                        image_url=article.get(
                            "image_url", ""
                        ),  # Use .get() to avoid KeyError if "image_url" is missing
                        published_at=published_at,  # Use the parsed datetime object
                        sentiment=sentiment,  # Use the validated sentiment
                    )
                    tickers = article.get("tickers", [])
                    for ticker in tickers:
                        ticker_obj, _ = CryptoTricker.objects.get_or_create(
                            ticker=ticker
                        )
                        crypto_news.tickers.add(ticker_obj)

            self.stdout.write(
                self.style.SUCCESS(f"Successfully processed {len(articles)} articles.")
            )

        except requests.exceptions.RequestException as e:
            self.stdout.write(self.style.ERROR(f"Error calling API: {e}"))

    def handle(self, *args, **kwargs):
        """
        Entry point for the management command.
        """
        self.stdout.write(self.style.SUCCESS("Starting to fetch crypto news..."))

        base_url = f"{CRYPTO_NEWS_API_URL}category"
        api_key = CRYPTO_NEWS_API_KEY

        # Parameters for API calls
        general_params = {"section": "general", "items": 3, "page": 1, "token": api_key}
        ticker_params = {
            "section": "alltickers",
            "items": 3,
            "page": 1,
            "token": api_key,
        }

        # Call API for general news
        self.call_crypto_news_api(base_url, general_params)

        # Call API for ticker-related news
        self.call_crypto_news_api(base_url, ticker_params)

        self.stdout.write(self.style.SUCCESS("Finished fetching crypto news."))
