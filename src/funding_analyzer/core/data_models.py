from dataclasses import dataclass
from datetime import datetime

@dataclass
class FundingRate:
    timestamp: datetime
    exchange: str
    symbol: str
    funding_rate: float
