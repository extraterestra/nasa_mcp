import json

from mcp.server.fastmcp import FastMCP
from api.nasa import get_nasa_apod, search_nasa_images

mcp = FastMCP()

@mcp.tool("get_apod_data", description="Fetch NASA's Astronomy Picture of the Day (APOD) data for a specific date. Provide the date in 'YYYY-MM-DD' format or leave blank for today's data.")
def get_apod_data(date: str = None):
    result = get_nasa_apod(date)
    if result:
        return json.dumps(result, indent=4)
    else:
        return {"error": "Failed to retrieve APOD data"}

@mcp.tool("search_images_data", description="Search NASA's image library using a query string. Provide a search term (e.g., 'Mars', 'Moon Landing').")
def search_images_data(q: str):
    result = search_nasa_images(q)
    if result:
        return json.dumps(result, indent=4)
    else:
        return {"error": "Failed to search for images"}

if __name__== "__main__":
    mcp.run()