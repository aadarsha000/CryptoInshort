from django.db.models.signals import post_save
from django.dispatch import receiver

from openai import OpenAI

from .models import CryptoNews
from config.settings import OPENAI_API_KEY
from .services.extract_news_from_url import (
    extract_news_from_url_using_newspaper3k,
    extract_news_from_url_using_playwright,
)


@receiver(post_save, sender=CryptoNews)
def summarize_crypto_news(sender, instance, created, **kwargs):
    if created:
        client = OpenAI(api_key=OPENAI_API_KEY)
        content = extract_news_from_url_using_newspaper3k(instance.source_url)
        if content:
            print("__________________3k___________________")
            prompt = f"Summarize the following article in 60 words: {content}"
            completion = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
            )
            summary = completion.choices[0].message.content
            instance.summary = summary
            instance.save()
        else:
            print("__________________playwright___________________")
            content = extract_news_from_url_using_playwright(instance.source_url)
            print(content)
            if content:
                print("__________________playwright___________________")
                prompt = f"""
                Extract only the main news content from the following text and ignore unrelated sections like navigation menus, ads, or footers. Summarize the extracted content in 60 words.
                Here is the text:
                {content}
                """
                completion = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {
                            "role": "user",
                            "content": prompt,
                        }
                    ],
                )
                summary = completion.choices[0].message.content
                instance.summary = summary
                instance.save()
