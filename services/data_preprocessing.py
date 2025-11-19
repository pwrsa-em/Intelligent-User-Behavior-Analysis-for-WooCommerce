import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from models.user_model import UserModel
from models.product_model import ProductModel
from models.event_model import EventModel

class DataPreprocessor:
    def __init__(self):
        self.user_model = UserModel()
        self.product_model = ProductModel()
        self.event_model = EventModel()
        self.scaler = MinMaxScaler()

    def load_raw_data(self):
        users = pd.DataFrame(self.user_model.get_all_users())
        products = pd.DataFrame(self.product_model.get_all_products())
        events = pd.DataFrame(self.event_model.get_all_events())
        return users, products, events

    def clean_data(self, df):
        df = df.copy()
        df.drop_duplicates(inplace=True)
        df.fillna({col: df[col].median() if df[col].dtype != 'object' else 'unknown'
                   for col in df.columns}, inplace=True)
        return df

    def engineer_features(self, events_df):
        df = events_df.copy()
        # تعداد رویدادها برای هر محصول
        product_event_count = df.groupby('product_id').size().reset_index(name='event_count')
        # تعداد خرید و اضافه به سبد
        add_to_cart = df[df['event_type']=='add_to_cart'].groupby('product_id').size().reset_index(name='add_to_cart_count')
        purchases = df[df['event_type']=='purchase'].groupby('product_id').size().reset_index(name='purchase_count')
        # ادغام
        features = product_event_count.merge(add_to_cart, on='product_id', how='left')
        features = features.merge(purchases, on='product_id', how='left')
        features.fillna(0, inplace=True)
        return features

    def scale_features(self, df, columns):
        df = df.copy()
        df[columns] = self.scaler.fit_transform(df[columns])
        return df

    def preprocess_all(self):
        users, products, events = self.load_raw_data()
        users = self.clean_data(users)
        products = self.clean_data(products)
        events = self.clean_data(events)
        features = self.engineer_features(events)
        features = self.scale_features(features, ['event_count', 'add_to_cart_count', 'purchase_count'])
        return {'users': users, 'products': products, 'events': events, 'features': features}