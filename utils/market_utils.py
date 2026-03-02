from datetime import datetime
import pytz

def is_market_open():
    """
    Rough check for Korean market hours.
    09:00 - 15:30 KST
    """
    korea = pytz.timezone("Asia/Seoul")
    now = datetime.now(korea)

    if now.weekday() >= 5:
        return False

    if 9 <= now.hour < 15:
        return True

    return False