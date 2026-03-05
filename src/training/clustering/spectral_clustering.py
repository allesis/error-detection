from sklearn.cluster import SpectralClustering as Sk_SpectralClustering
from training.model import Model
import type_enforced


@type_enforced.Enforcer(enabled=True, strict=True, clean_traceback=True)
class SpectralClustering(Model):
    @type_enforced.Enforcer(enabled=True, strict=True, clean_traceback=True)
    def __init__(self: SpectralClustering, n_clusters: int = 2):
        """Initialize the model with the values provided in kwargs
        Defaults should be defined so that if no kwargs are provided, the model functions correctly
        """
        self._model: Sk_SpectralClustering = Sk_SpectralClustering(n_clusters=n_clusters)
