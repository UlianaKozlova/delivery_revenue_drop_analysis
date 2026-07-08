import pandas as pd

def aggregate_monthly_orders(orders):
    monthly = orders.groupby('year_month').agg({
        'order_id': 'count',
        'client_id': 'nunique',
        'paid_amount': ['sum', 'mean']
    }).reset_index()
    monthly.columns = ['year_month', 'orders_count', 'unique_clients', 'total_revenue', 'avg_order_value']
    monthly['orders_per_client'] = monthly['orders_count'] / monthly['unique_clients']
    return monthly

def aggregate_funnel(funnel):
    funnel_metrics = funnel.groupby('session_month').agg({
        'session_id': 'count',
        'product_search': 'sum',
        'product_card_view': 'sum',
        'add_to_cart': 'sum',
        'cart_visit': 'sum',
        'purchase': 'sum'
    }).reset_index()
    funnel_metrics.columns = ['month', 'sessions', 'searches', 'card_views', 'add_to_cart', 'cart_visits', 'purchases']
    funnel_metrics['visit_to_search'] = funnel_metrics['searches'] / funnel_metrics['sessions']
    funnel_metrics['search_to_card'] = funnel_metrics['card_views'] / funnel_metrics['searches']
    funnel_metrics['card_to_cart'] = funnel_metrics['add_to_cart'] / funnel_metrics['card_views']
    funnel_metrics['cart_to_purchase'] = funnel_metrics['purchases'] / funnel_metrics['cart_visits']
    funnel_metrics['visit_to_purchase'] = funnel_metrics['purchases'] / funnel_metrics['sessions']
    return funnel_metrics

def aggregate_platform_metrics(orders):
    platform = orders.groupby(['year_month', 'platform']).agg({
        'paid_amount': 'sum',
        'order_id': 'count',
        'client_id': 'nunique'
    }).reset_index()
    platform.columns = ['month', 'platform', 'revenue', 'orders', 'clients']
    platform['avg_check'] = platform['revenue'] / platform['orders']
    return platform

def aggregate_marketing(marketing):
    marketing_metrics = marketing.groupby('send_month').agg({
        'communication_id': 'count',
        'client_id': 'nunique'
    }).reset_index()
    marketing_metrics.columns = ['month', 'communications_sent', 'users_reached']
    return marketing_metrics
