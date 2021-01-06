import asyncio
from pyppeteer import launch

class urlChecker:
    def __init__(self, url, name, x = 0, y = 0, width = 1080, height = 2000):
        self.name = name
        self.url = url
        self.loop = asyncio.get_event_loop()
        self.browser = None
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def setUpBrowser(self):
        self.loop.run_until_complete(self.__async_browser())

    def getPicture(self,fileName):
        return self.loop.run_until_complete(self.__async__check_url(fileName))

    async def __async_browser(self):
        self.browser = await launch({'headless': True})
        return self

    async def __async__check_url(self,fileName):
        page = await self.browser.newPage()
        await page.setViewport({'width': 1080, 'height': 2000 })
        await page.goto(self.url)
        await page.screenshot({'path': fileName,'clip': { 'x': self.x, 'y': self.y, 'width': self.width, 'height': self.height } })
        # await page.screenshot({'path': fileName,'clip': { 'x': 0, 'y': 800, 'width': 1080, 'height': 600 } })
        await page.close()
        await asyncio.sleep(1)