import pandas as pd
import os

DATA_DIR = '../data/' 

def load_orders():
    return pd.read_csv(os.path.join(DATA_DIR, 'grocery_delivery_orders_2025_11_2026_04.csv'))

def load_funnel():
    return pd.read_csv(os.path.join(DATA_DIR, 'grocery_delivery_funnel_2025_11_2026_04.csv'))

def load_marketing():
    return pd.read_csv(os.path.join(DATA_DIR, 'grocery_delivery_marketing_communications_2025_11_2026_04.csv'))

def preprocess(orders, funnel, marketing):
    orders['order_date'] = pd.to_datetime(orders['order_date'])
    funnel['session_date'] = pd.to_datetime(funnel['session_date'])
    marketing['send_date'] = pd.to_datetime(marketing['send_date'])

    orders['year_month'] = orders['order_date'].dt.to_period('M')
    funnel['session_month'] = funnel['session_date'].dt.to_period('M')
    marketing['send_month'] = marketing['send_date'].dt.to_period('M')

    return orders, funnel, marketing
