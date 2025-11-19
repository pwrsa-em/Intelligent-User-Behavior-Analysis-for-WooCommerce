from services.data_preprocessing import DataPreprocessor
from views.api_response import success

class MLController:
    def __init__(self):
        self.preprocessor = DataPreprocessor()

    def generate_training_data(self):
        data = self.preprocessor.preprocess_all()
        return success(data)
