import type_enforced
import numpy as np
import matplotlib

matplotlib.use("SVG")
import matplotlib.pyplot as plt


@type_enforced.Enforcer(enabled=True, strict=True, clean_traceback=True)
def plot_results(
    data: np.ndarray,
    prediction: np.ndarray,
    name: str = "plot.svg",
):
    filtered_label0 = data[prediction == np.float64(0.0)]

    filtered_label1 = data[prediction == np.float64(1.0)]

    plt.scatter(filtered_label0[:, 0], filtered_label0[:, 1], color="red")
    plt.scatter(filtered_label1[:, 0], filtered_label1[:, 1], color="blue")
    plt.savefig(name)
