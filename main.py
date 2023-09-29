from data_cleaner import DataCleaner
from data_preprocessor import DataPreprocessor
from model_trainer import ModelTrainer
from model_evaluator import ModelEvaluator
from chatbot import Chatbot
from data_anonymizer import DataAnonymizer
from data_consent_manager import DataConsentManager
from data_erasure_manager import DataErasureManager

def main():
    # Instantiate the classes
    data_cleaner = DataCleaner()
    data_preprocessor = DataPreprocessor()
    model_trainer = ModelTrainer()
    model_evaluator = ModelEvaluator()
    chatbot = Chatbot()
    data_anonymizer = DataAnonymizer()
    data_consent_manager = DataConsentManager()
    data_erasure_manager = DataErasureManager()

    # Clean the data
    cleaned_data = data_cleaner.clean_data()

    # Anonymize personal data
    anonymized_data = data_anonymizer.anonymize_personal_data(cleaned_data)

    # Obtain necessary consents for data usage
    consented_data = data_consent_manager.obtain_consent(anonymized_data)

    # Preprocess the data for the chosen AI model
    preprocessed_data = data_preprocessor.preprocess_data(consented_data)

    # Train the model
    model = model_trainer.train_model(preprocessed_data)

    # Validate the model
    validated_model = model_trainer.validate_model(model)

    # Evaluate the model
    model_evaluator.evaluate_model(validated_model)

    # Deploy the chatbot
    chatbot.deploy(validated_model)

if __name__ == "__main__":
    main()
