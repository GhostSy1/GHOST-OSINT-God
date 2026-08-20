import aiohttp
import asyncio
class SocialIntelligence:
    def __init__(self, username):
        self.username = username
        self.platforms = {
            "GitHub": "https://github.com/{}",
            "Twitter": "https://twitter.com/{}",
            "Instagram": "https://www.instagram.com/{}",
            "Facebook": "https://www.facebook.com/{}",
            "LinkedIn": "https://www.linkedin.com/in/{}",
            "Reddit": "https://www.reddit.com/user/{}",
            "Pinterest": "https://www.pinterest.com/{}",
            "Tumblr": "https://{}.tumblr.com",
            "YouTube": "https://www.youtube.com/@{}",
            "TikTok": "https://www.tiktok.com/@{}"
        }
    async def check_platform(self, session, name, url_template):
        url = url_template.format(self.username)
        try:
            async with session.get(url, timeout=5) as response:
                if response.status == 200:
                    return name, url
        except Exception:
            pass
        return name, None
    async def run(self):
        async with aiohttp.ClientSession() as session:
            tasks = [self.check_platform(session, name, url) for name, url in self.platforms.items()]
            results = await asyncio.gather(*tasks)
            return {name: url for name, url in results if url}
