import asyncio
import aiohttp
import feedparser


class HabrReader:
    def __init__(self):
        self.url = "https://habr.com/ru/rss/articles/"

    async def fetch_rss(self, session):
        async with session.get(self.url) as response:
            return await response.text()

    async def parse_feed(self, feed):
        #print(feed)
        title = feed.title
        link = feed.link
        description = feed.description
        published = feed.published
        categories = [item['term'] for item in feed.tags]

        return {
            'title': title,
            'link': link,
            'description': description,
            'published': published,
            'categories': categories,
        }

    async def main(self):
        async with aiohttp.ClientSession() as session:
            xml = await self.fetch_rss(session)
            feeds = feedparser.parse(xml)
            parsed_feeds = await asyncio.gather(*[self.parse_feed(feed) for feed in feeds.entries])
            return parsed_feeds
