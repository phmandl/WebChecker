import asyncio
from pyppeteer import launch


async def main():
    browser = await launch({'headless': True})
    page = await browser.newPage()
    await page.setViewport({'width': 1080, 'height': 2000 })
    await page.goto('https://webshop.asus.com/de/komponenten/grafikkarten/rtx-30-serie/2955/asus-tuf-rtx3070-o8g-gaming')
    await page.screenshot({'path': 'example.jpeg','clip': { 'x': 0, 'y': 800, 'width': 1080, 'height': 600 } })
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())