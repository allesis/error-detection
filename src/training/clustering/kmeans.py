from sklearn.cluster import KMeans as Sk_KMeans
from training.model import Model
import type_enforced


@type_enforced.Enforcer(enabled=True, strict=True, clean_traceback=True)
class KMeans(Model):
    @type_enforced.Enforcer(enabled=True, strict=True, clean_traceback=True)
    def __init__(self: KMeans, n_clusters: int = 2):
        """Initialize the model with the values provided in kwargs
        Defaults should be defined so that if no kwargs are provided, the model functions correctly
        """
        self._model: Sk_KMeans = Sk_KMeans(n_clusters=n_clusters)
