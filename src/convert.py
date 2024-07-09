import asyncio
from playwright.async_api import async_playwright

async def html_to_pdf(url, pdf_file_path, print_options=None):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        # Navigate to the local server URL
        await page.goto(url, wait_until='networkidle')

        # Set default print options if none are provided
        if print_options is None:
            print_options = {
                "format": "A4",
                "print_background": True
            }
        # Convert to PDF with specified print options
        await page.pdf(path=pdf_file_path, **print_options)

        await browser.close()

# PDF print options
print_options = {
    "format": "A4",            # Paper format: 'Letter', 'Legal', 'Tabloid', 'Ledger', 'A0' to 'A5'
    "print_background": True,  # Print background graphics
    "margin": {                # Margins in inches
        "top": "0.2in",
        "right": "0.2in",
        "bottom": "0.2in",
        "left": "0.2in"
    },
    "landscape": False,        # Set to True for landscape mode
    "display_header_footer": False, # Set to True to display header and footer
    "header_template": '',     # HTML template for the print header
    "footer_template": '',     # HTML template for the print footer
    "scale": 1.0               # Scale of the webpage rendering
}

# URL to the HTML file served by the local server
url = 'http://localhost:5999/src/reportV2.html'
pdf_file_path = '/home/sarthak/projects/src/output.pdf'

# Run the conversion
asyncio.run(html_to_pdf(url, pdf_file_path, print_options))
