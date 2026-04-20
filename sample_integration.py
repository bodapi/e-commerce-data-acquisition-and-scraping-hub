"""
BODAPI GLOBAL HUB - MULTI-PLATFORM API SAMPLE
=============================================
This is the master integration script for Bodapi. 
One API key, global access to E-commerce data.

Supported Platforms: Amazon, Shopee, Lazada, Walmart, Wayfair, etc.
Documentation: https://bodapi.com
"""

import requests

class BodapiClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.bodapi.com/v1"

    def get_market_data(self, platform, region, item_id):
        """
        Generic function to fetch data from any supported platform.
        """
        endpoint = f"{self.base_url}/{platform}/{region}/product/{item_id}"
        print(f"[BODAPI] Requesting {platform.upper()} data for ID: {item_id}...")
        
        # In actual use, this would return a JSON response
        return {"status": "success", "platform": platform, "item_id": item_id}

if __name__ == "__main__":
    # Initialize the Bodapi Client
    client = BodapiClient(api_key="YOUR_MASTER_API_KEY")

    # Example: Fetching Amazon US Data
    amazon_data = client.get_market_data("amazon", "us", "B08N5K3T9")
    
    # Example: Fetching Shopee PH Data
    shopee_data = client.get_market_data("shopee", "ph", "234567890")

    print("--- Integration Test Complete ---")
    print("Ready to serve high-volume data requests.")
