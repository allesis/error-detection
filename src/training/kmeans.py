from sklearn.cluster import KMeans
import type_enforced


@type_enforced.Enforcer(enabled=True, strict=True, clean_traceback=True)
class KMeans:
    @type_enforced.Enforcer(enabled=True, strict=True, clean_traceback=True)
    def __init__(**kwargs):
        """Initialize the model with the values provided in kwargs
        Defaults should be defined so that if no kwargs are provided, the model functions correctly
        """
        pass

    @type_enforced.Enforcer(enabled=True, strict=True, clean_traceback=True)
    def train(source: list[float], target: list[float]):
        """Train the model to predict source -> target"""
        pass

    @type_enforced.Enforcer(enabled=True, strict=True, clean_traceback=True)
    def evaluate(source: list[float], target: list[float]) -> float:
        """Evaluate the model's ability to predict source -> target.
        The model will train itself it is has not been prior to this method executing.
        Returns the accuracy as a float
        """
        pass

    @type_enforced.Enforcer(enabled=True, strict=True, clean_traceback=True)
    def predict(source: list[float]) -> list[float]:
        """Predicts the values of source, returning the predictions.
        The model will train itself it is has not been prior to this method executing.
        """
        pass
