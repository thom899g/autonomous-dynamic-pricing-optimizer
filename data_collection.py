import requests
import pandas as pd
import logging
from typing import Dict, Optional

logger = logging.getLogger(__name__)

class DataCollector:
    def __init__(self):
        self.market_data_url = "https://api.markets.com/data"
        self.customer_behavior_url = "https://api.behavior.com/segments"
        self.competitor_prices_url = "https://api.price_tracker.com/current"

    def fetch_market_data(self) -> Optional[pd.DataFrame]:
        try:
            response = requests.get(self.market_data_url)
            if not response.ok:
                logger.error(f"Failed to fetch market data: {response.status_code}")
                return None
            data = response.json()
            df = pd.DataFrame(data)
            return df
        except Exception as e:
            logger.error(f"Error in fetch_market_data: {str(e)}")
            return None

    def fetch_customer_behavior(self) -> Optional[pd.DataFrame]:
        try:
            response = requests.get(self.customer_behavior_url)
            if not response.ok:
                logger.error(f"Failed to fetch customer behavior: {response.status_code}")
                return None
            data = response.json()
            df = pd.DataFrame(data)
            return df
        except Exception as e:
            logger.error(f"Error in fetch_customer_behavior: {str(e)}")
            return None

    def fetch_competitor_prices(self) -> Optional[pd.DataFrame]:
        try:
            response = requests.get(self.competitor_prices_url)
            if not response.ok:
                logger.error(f"Failed to fetch competitor prices: {response.status_code}")
                return None
            data = response.json()
            df = pd.DataFrame(data)
            return df
        except Exception as e:
            logger.error(f"Error in fetch_competitor_prices: {str(e)}")
            return None

    def collect_data(self) -> Dict[str, Optional[pd.DataFrame]]:
        try:
            market_data = self.fetch_market_data()
            customer_behavior = self.fetch_customer_behavior()
            competitor_prices = self.fetch_competitor_prices()

            data_dict = {
                "market_data": market_data,
                "customer_behavior": customer_behavior,
                "competitor_prices": competitor_prices
            }

            return data_dict
        except Exception as e:
            logger.error(f"Data collection failed: {str(e)}")
            return None

if __name__ == "__main__":
    collector = DataCollector()
    data = collector.collect_data()