from sklearn.neighbors import KNeighborsClassifier as Sk_KNeighborsClassifier
from training.model import Model
import type_enforced
import numpy


@type_enforced.Enforcer(enabled=True, strict=True, clean_traceback=True)
class KNeighborsClassifier(Model):
    @type_enforced.Enforcer(enabled=True, strict=True, clean_traceback=True)
    def __init__(
        self: KNeighborsClassifier,
        n_neighbors: int = 2,
        weights: str = "uniform",
        algorithm: str = "auto",
        leaf_size: int = 30,
        p: int = 2,
        metric: str = "minkowski",
        metric_params: dict | None = None,
        n_jobs: int | None = None,
    ):
        """Initialize the model with the values provided in kwargs
        Defaults should be defined so that if no kwargs are provided, the model functions correctly
        """
        self._model: Sk_KNeighborsClassifier = Sk_KNeighborsClassifier(
            n_neighbors=n_neighbors,
            weights=weights,
            algorithm=algorithm,
            leaf_size=leaf_size,
            p=p,
            metric=metric,
            metric_params=metric_params,
            n_jobs=n_jobs,
        )

    @type_enforced.Enforcer(enabled=True, strict=True, clean_traceback=True)
    def predict(
        self, source: numpy.ndarray, target: numpy.ndarray = numpy.empty(0)
    ) -> list[float]:
        """Predicts the clustering of source, returning the predictions.
        The model will train itself it is has not been prior to this method executing.
        """
        return list(map(lambda x: 0.0 + x, self._model.predict(source)))
