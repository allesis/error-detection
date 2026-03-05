import type_enforced
import numpy
import matplotlib.pyplot as plt


@type_enforced.Enforcer(enabled=True, strict=True, clean_traceback=True)
def plot_results(
    data: numpy.ndarray,
    prediction: list[float],
):
    """Plots the value of data onto a 2D space using PCA
    """
    #filter rows of original data
    filtered_label0 = data[prediction == 0.0]
     
    print(prediction)
    filtered_label1 = data[prediction == 1.0]
    print(filtered_label0)
    print(filtered_label1)
     
    print(data)
    #Plotting the results
    plt.scatter(filtered_label0[:,0] , filtered_label0[:,1] , color = 'red')
    plt.scatter(filtered_label1[:,0] , filtered_label1[:,1] , color = 'blue')
    plt.xlim(-1000, 1000)
    plt.ylim(-5000000, 5000000)
    plt.show()
         
