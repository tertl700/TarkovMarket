from pyppeteer import launch


async def init():
    global browser
    browser = await launch(
        handleSIGINT=False,
        handleSIGTERM=False,
        handleSIGHUP=False,
    )
    pages = await browser.pages()
    global page
    page = pages[0]
    await page.goto("https://tarkov-market.com/")
