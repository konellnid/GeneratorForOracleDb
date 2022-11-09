from datetime import datetime


def format_date_for_oracle(date: datetime.date):
    return f"TO_DATE('{date.isoformat()}', 'yyyy-mm-dd')"
