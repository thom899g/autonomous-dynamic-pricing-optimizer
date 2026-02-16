import pandas as pd
from sklearn.linear_model import LinearRegression
from typing import Dict, Optional
import logging

logger = logging.getLogger(__name__)

class PricingModel:
    def __init__(self):
        self.model = LinearRegression()

    def train_model(self, data: pd.DataFrame) -> bool:
        try:
            if "price" not in data or "demand" not in data:
                logger.error("Missing required columns for training")
                return False
            X = data[["price"]]
            y = data["demand"]
            self.model.fit(X, y)
            logger.info("Model trained successfully")
            return True
        except Exception as e:
            logger.error(f"Training failed: {str(e)}")
            return False

    def predict_price(self, cost: float, margin: float) -> Optional[float]:
        try:
            predicted_demand = self.model.predict([[cost + margin]])
            # Ethical check: Ensure price doesn't exploit elasticity
            if predicted_demand > 1000:  # Assuming 1000 is a high threshold
                logger.warning("High demand may lead to price gouging")
            return cost + margin
        except Exception as e:
            logger.error(f"Prediction failed: {str(e)}")
            return None

    def get_coefficients(self) -> Dict[str, float]:
        try:
            coefficients = {
                "intercept": self.model.intercept_,
                "slope": self.model.coef_[0]
            }
            return coefficients
        except Exception as e:
            logger.error(f"Failed to retrieve coefficients: {str(e)}")
            return None

if __name__ == "__main__":
    model = PricingModel()
    data = pd.DataFrame({
        'price': [10, 20, 30],
        'demand': [100, 200, 300]
    })
    model.train_model(data)
    print(model.predict_price(5, 5))