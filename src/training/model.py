import type_enforced
import numpy


@type_enforced.Enforcer(enabled=True, strict=True, clean_traceback=True)
class Model:
    @type_enforced.Enforcer(enabled=True, strict=True, clean_traceback=True)
    def train(self, source: list[list[float]], target: list[float] = list()):
        """Train the model to cluster data based on the clustering of source"""
        self._model.fit(source, y=target)

    @type_enforced.Enforcer(enabled=True, strict=True, clean_traceback=True)
    def evaluate(self, source: list[float], target: list[float] = list()) -> float:
        """Evaluate the model's ability to cluster
        The model will train itself it is has not been prior to this method executing.
        Returns the accuracy as a float
        Target is ignored, included for API consistency
        """
        return self._model.score(source, y=target)

    @type_enforced.Enforcer(enabled=True, strict=True, clean_traceback=True)
    def predict(
        self, source: list[list[float]], target: list[float] = list()
    ) -> list[float]:
        """Predicts the clustering of source, returning the predictions.
        The model will train itself it is has not been prior to this method executing.
        """
        return list(map(lambda x: 0.0 + x, self._model.fit_predict(source, y=target)))
