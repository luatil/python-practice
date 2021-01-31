import pytest
from datetime import datetime
from datetime import timedelta

def get_billing_month_w(dt) -> datetime:
    if(dt.day >= 25):
        if(dt.month == 12):
            dt = datetime(dt.year + 1, 1, 1)
        else:
            dt = datetime(dt.year, dt.month + 1, 1)
    return dt

def get_billing_month_ver2(dt) -> datetime:
    if(dt.day >= 25):
        dt = datetime(dt.year+1, 1, 1) if dt.month == 12 else datetime(dt.year,dt.month+1, 1)
    return dt

def get_billing_month(dt) -> datetime:
    offset = timedelta(days=7)
    dt = dt + offset if dt.day >= 25 else dt
    return dt


def test_date_24_january():
    dt = datetime(2020, 1, 24)
    assert get_billing_month(dt).month == 1
    
def test_date_25_january():
    dt = datetime(2021, 1, 25)
    assert get_billing_month(dt).month == 2
    
def test_date_29_february():
    dt = datetime(2020, 2, 29)
    assert get_billing_month(dt).month == 3
    
def test_date_31_march():
    dt = datetime(2020, 3, 31)
    assert get_billing_month(dt).month == 4      
    
def test_date_31_december():
    dt = datetime(2021, 12, 31)
    assert get_billing_month(dt).month == 1
