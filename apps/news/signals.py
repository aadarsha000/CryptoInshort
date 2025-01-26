from django.db.models.signals import post_save
from django.dispatch import receiver

from openai import OpenAI

from .models import CryptoNews
from config.settings import OPENAI_API_KEY


@receiver(post_save, sender=CryptoNews)
def summarize_crypto_news(sender, instance, created, **kwargs):
    if created:
        client = OpenAI(api_key=OPENAI_API_KEY)
        prompt = f"Summarize the following article in 60 words: {instance.title}"
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )
        print(completion.choices[0].message.content)
        summary = completion.choices[0].message.content
        instance.summary = summary
        instance.save()
