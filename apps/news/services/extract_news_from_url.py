import asyncio
from playwright.async_api import async_playwright
from newspaper import Article


def extract_news_from_url_using_playwright(url):
    async def main():
        async with async_playwright() as p:
            browser = await p.firefox.launch(headless=True)
            page = await browser.new_page()
            await page.goto(url=url)
            await page.wait_for_load_state("domcontentloaded")
            text_content = await page.evaluate("document.body.innerText")
            await browser.close()
            return text_content

    return asyncio.run(main())


def extract_news_from_url_using_newspaper3k(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except Exception as e:
        return None
