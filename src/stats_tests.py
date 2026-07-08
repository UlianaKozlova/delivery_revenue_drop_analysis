from scipy import stats
from statsmodels.stats.proportion import proportions_ztest
import pandas as pd

def t_test_avg_check(march_orders, april_orders):
    stat, pvalue = stats.ttest_ind(march_orders, april_orders, equal_var=False)
    print(f'T-test среднего чека: p-value = {pvalue:.6f}')
    return pvalue

def z_test_conversion(funnel, group_col='experiment_group', target='purchase'):
    """
    Сравнение конверсии между test и control группами.
    """
    test = funnel[funnel[group_col] == 'test']
    control = funnel[funnel[group_col] == 'control']
    n_test = len(test)
    n_control = len(control)
    conv_test = test[target].mean()
    conv_control = control[target].mean()
    count = [conv_test * n_test, conv_control * n_control]
    nobs = [n_test, n_control]
    z_stat, p_value = proportions_ztest(count, nobs, alternative='two-sided')
    print(f'Z-тест (Test vs Control): z={z_stat:.4f}, p={p_value:.6f}')
    return p_value

def compare_time_periods(marketing, orders):
    """
    Сравнивает конверсию заказов среди клиентов, получивших сообщения в разное время.
    """
    # Предполагаем, что в marketing есть колонка send_hour
    def time_period(hour):
        if 6 <= hour < 12:
            return 'morning'
        elif 12 <= hour < 18:
            return 'afternoon'
        else:
            return 'evening'
    marketing['time_category'] = marketing['send_hour'].apply(time_period)
    # Объединяем с заказами по client_id
    merged = marketing.merge(orders[['client_id', 'order_id']], on='client_id', how='left')
    conv_by_time = merged.groupby('time_category').apply(lambda x: x['order_id'].notna().mean())
    print('Конверсия по времени отправки:\n', conv_by_time)
    # Можно добавить попарный Z-тест
    return conv_by_time
