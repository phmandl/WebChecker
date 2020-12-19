import asyncio
from pyppeteer import launch

class urlChecker:
    def __init__(self, url):
        self.url = url
        self.loop = asyncio.get_event_loop()
        self.browser = None

    def setUpBrowser(self):
        self.loop.run_until_complete(self.__async_browser())

    def check(self):
        return self.loop.run_until_complete(self.__async__check_url())

    async def __async_browser(self):
        self.browser = await launch({'headless': True})
        return self

    async def __async__check_url(self):
        page = await self.browser.newPage()
        await page.setViewport({'width': 1080, 'height': 2000 })
        await page.goto(self.url)
        await page.screenshot({'path': 'example.jpeg','clip': { 'x': 0, 'y': 800, 'width': 1080, 'height': 600 } })
        await page.close()
        await asyncio.sleep(2)


check = urlChecker('https://webshop.asus.com/de/komponenten/grafikkarten/rtx-30-serie/2955/asus-tuf-rtx3070-o8g-gaming')
check.setUpBrowser()

while True:
    check.check()
    print('next Page \n')