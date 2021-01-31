import asyncio
import os
from pyppeteer import launch

class webPagePicChecker:
    def __init__(self, url, name, area):
        self.name = name
        self.url = url
        self.loop = asyncio.get_event_loop()
        self.browser = None
        self.height = []
        self.width = []
        self.x = []
        self.y = []
        self.pages = []

        for idx,dat in enumerate(area):
            self.height.append(dat["height"])
            self.width.append(dat["width"])
            self.x.append(dat["x"])
            self.y.append(dat["y"])

    def setUpBrowser(self):
        self.loop.run_until_complete(self.__async_browser())

    async def __async_browser(self):
        self.browser = await launch({'headless': True})
        for idx,url in enumerate(self.url):
            page = await self.browser.newPage()
            await page.setViewport({'width': 1080, 'height': 2000 })
            await page.goto(url)
            self.pages.append(page)   
        return self

    def getPicture(self,fileName):
        return self.loop.run_until_complete(self.__async__check_page(fileName))

    async def __async__check_page(self,folder):
        for idx,name in enumerate(self.name):
            page = self.pages[idx]
            x = self.x[idx]
            y = self.y[idx]
            width = self.width[idx]
            height = self.height[idx]
            fileName = folder + '\\' + name + '.png'

            await page.screenshot({'path': fileName,'clip': { 'x': x, 'y': y, 'width': width, 'height': height } })
            await asyncio.sleep(1)