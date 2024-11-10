from WineQuality import logger
from WineQuality.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from WineQuality.pipeline.stage02_data_validation import DataValidationTrainingPipeline
from WineQuality.pipeline.stage03_data_transformation import DataTransformationTrainingPipeline
from WineQuality.pipeline.stage04_model_trainer import ModelTrainerTrainingPipeline
from WineQuality.pipeline.stage05_model_evaluation import ModelEvaluationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"stage {STAGE_NAME} started")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f"stage {STAGE_NAME} started")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f"stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f"stage {STAGE_NAME} started")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f"stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Trainer Stage"

try:
    logger.info(f"stage {STAGE_NAME} started")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f"stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation Stage"

try:
    logger.info(f"stage {STAGE_NAME} started")
    model_evaluation = ModelEvaluationTrainingPipeline()
    model_evaluation.main()
    logger.info(f"stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e