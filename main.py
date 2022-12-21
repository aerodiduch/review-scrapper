from app_store_scraper import AppStore
import pandas as pd
import numpy as np
import json


def get_reviews(country, app_name, app_id):
    app = AppStore(
        country, app_name, app_id
    )
    app.review()
    return app.reviews


def export_report(data):
    df = pd.DataFrame(np.array(data),columns=['review'])
    df2 = df.join(pd.DataFrame(df.pop('review').tolist()))
    df2.head()
    df2.to_csv('./data.csv')


if __name__ == '__main__':
    app = get_reviews(country='ar', app_name='', app_id=1234)
    export_report(app)
