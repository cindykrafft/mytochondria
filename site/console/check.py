import os
import asyncio, sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/opt/pw-browsers/chromium"); pg=await b.new_page(); errs=[]
        pg.on("pageerror", lambda e: errs.append(str(e)))
        html=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"out","filing-console.html")).read()
        await pg.set_content("<!doctype html><html><head><meta charset=utf-8></head><body>"+html+"</body></html>")
        await pg.wait_for_timeout(500)
        n=await pg.evaluate("document.querySelectorAll('.card').length")
        tiers=await pg.evaluate("[...document.querySelectorAll('.eyebrow.tier')].map(e=>e.textContent)")
        held=await pg.evaluate("document.querySelectorAll('details.tier-held').length")
        print("cards",n,"held-sections",held); print(tiers); print("errors",errs)
        await b.close()
asyncio.run(main())
