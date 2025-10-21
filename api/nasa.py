import os
from dotenv import load_dotenv
import requests
from typing import Optional, Dict

import logging

# Configure basic logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

load_dotenv()

NASA_API_KEY = os.getenv("NASA_API_KEY") or "DEMO_KEY"

def make_api_request(url: str, params: dict, timeout: int = 10) -> Optional[Dict]:
    """
    Make an HTTP GET request to the specified URL with given parameters.
    
    Args:
        url: The API endpoint URL to request
        params: Dictionary of query parameters to include in the request
        timeout: Maximum time in seconds to wait for a response (default: 20)
    
    Returns:
        Optional[Dict]: JSON response as a dictionary if successful, None if an error occurs
    """
    try:
        response = requests.get(url, params=params, timeout=timeout)
        # Check if the response status code indicates success
        response.raise_for_status()
        # Try to parse JSON response
        return response.json()
    # Raise an HTTPError for bad responses (4xx and 5xx)
    except requests.exceptions.Timeout:
        logging.error(f"Request timed out after {timeout} seconds: {url}")
    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err} - URL: {url}")
    except requests.exceptions.RequestException as req_err:
        logging.error(f"Request exception occurred: {req_err}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
    
    return None  # Return None if an error occurs

def get_nasa_apod(api_key=NASA_API_KEY, date: Optional[str] = None) -> Optional[Dict]:
    """
    Retrieve NASA's Astronomy Picture of the Day (APOD).
    
    Fetches the APOD data from NASA's API, which includes an astronomical image or
    photograph along with a brief explanation written by a professional astronomer.
    
    Args:
        api_key: NASA API key for authentication (default: NASA_API_KEY from environment)
        date: Optional date string in YYYY-MM-DD format. If None, returns today's APOD
    
    Returns:
        Optional[Dict]: Dictionary containing APOD data including title, explanation,
                       URL, and other metadata if successful, None if request fails
    
    Example:
       result = get_nasa_apod(date="2024-01-15")
       print(result['title'])
    """

    # Build API URL and parameters
    base_url = "https://api.nasa.gov/planetary/apod"
    params = {
        "api_key": api_key,
    }

    if date:
        params["date"] = date

    logging.info(f"Requesting NASA APOD for date: {date if date else 'today'}...")
    apod_data = make_api_request(base_url, params, timeout=30)
    
    if apod_data is None:
        logging.error("Failed to retrieve NASA APOD data.")
    else:
        logging.info("Successfully retrieved NASA APOD data.")
    
    return apod_data


def search_nasa_images(query: str,
                       size: int = 3) -> Optional[Dict]:
    """
    Search NASA's Image and Video Library for images matching the query.

    Args:
        query (str): Search term to look for in NASA's image library
        size (int, optional): Number of results to return (page size). Defaults to 3.

    Returns:
        Optional[Dict]: Dictionary containing search results with image metadata,
                       URLs, and descriptions. Returns None if request fails.

    Example:
        results = search_nasa_images("Mars rover", size=5)
        for item in results["collection"]["items"]:
        print(item["data"][0]["title"])
    """
    # NASA Image and Video Library API endpoint
    base_url = "https://images-api.nasa.gov/search"

    # Build parameters
    params = {
        "q": query,
        "media_type": "image",
        "page": 1,
        "page_size": size
    }

    return make_api_request(base_url, params, timeout=15)


