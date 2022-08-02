import asyncio
from asyncio import sleep

from pyppeteer import launch
from pyppeteer.page import Page

N = 2
width, height = 1280, 1280


async def click_from_rainbow(page: Page, i: int = 0):
    print(f"第{i}次点击")
    badge_to_boringBay = '[title="无聊湾 → https://boringbay.com"]'
    await page.waitForSelector(badge_to_boringBay)
    await sleep(2)
    await page.click(badge_to_boringBay)
    await page.waitFor(2)
    await sleep(5)


async def main():
    args = ['--disable-infobars', f'--window-size={width},{height}', '--no-sandbox']
    browser = await launch(args=args)
    page = await browser.newPage()
    await page.setViewport({'width': width, 'height': height})
    await page.goto('https://pawswrite.xyz/', {'waitUntil': 'load'})
    await sleep(5)
    tasks = []
    for i in range(N):
        tasks.append(click_from_rainbow(page, i + 1))
    await asyncio.gather(*tasks)
    return browser


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    browser = loop.run_until_complete(main())
    loop.run_until_complete(browser.close())
