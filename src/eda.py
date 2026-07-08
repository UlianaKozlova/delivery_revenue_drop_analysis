import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_monthly_revenue(monthly_revenue):
    plt.figure(figsize=(12,6))
    plt.plot(monthly_revenue['year_month'].astype(str), monthly_revenue['paid_amount'], marker='o')
    plt.title('Динамика оборота')
    plt.xlabel('Месяц')
    plt.ylabel('Оборот')
    plt.grid(True)
    plt.show()

def plot_metrics(monthly_metrics):
    fig, axes = plt.subplots(2, 2, figsize=(16, 10))
    metrics = ['orders_count', 'unique_clients', 'avg_order_value', 'orders_per_client']
    titles = ['Количество заказов', 'Уникальные клиенты', 'Средний чек', 'Заказов на клиента']
    for ax, metric, title in zip(axes.flat, metrics, titles):
        ax.plot(monthly_metrics['year_month'].astype(str), monthly_metrics[metric], marker='o')
        ax.set_title(title)
    plt.tight_layout()
    plt.show()

def plot_conversions(funnel_metrics):
    conv_cols = ['visit_to_search', 'search_to_card', 'card_to_cart', 'cart_to_purchase', 'visit_to_purchase']
    plt.figure(figsize=(14,6))
    for col in conv_cols:
        plt.plot(funnel_metrics['month'].astype(str), funnel_metrics[col], marker='o', label=col)
    plt.title('Конверсии воронки')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_platform_revenue(platform_metrics):
    platform_metrics['month_str'] = platform_metrics['month'].astype(str)
    plt.figure(figsize=(14,6))
    sns.lineplot(data=platform_metrics, x='month_str', y='revenue', hue='platform', marker='o')
    plt.title('Оборот по платформам')
    plt.grid(True)
    plt.show()

def plot_marketing_volume(marketing_metrics):
    plt.figure(figsize=(12,5))
    plt.plot(marketing_metrics['month'].astype(str), marketing_metrics['communications_sent'], marker='o')
    plt.title('Количество маркетинговых коммуникаций')
    plt.grid(True)
    plt.show()
