import warnings
from sklearn import datasets, model_selection, svm, metrics

warnings.filterwarnings('ignore')
# Ignore the warning when you running

mnist = datasets.fetch_mldata('MNIST original', data_home='./')
# Because of the Internet inside of CHINA can't fetch `mldata`，so we need to download `mnist-original.mat` at `./mldata`，and `chmod 777` it

mnist_data = mnist.data / 255 # The data store by 8-bit, so that divide it by 255
mnist_label = mnist.target # Label is a list of number in range 0-9


def run_sklearn(mnist_data, mnist_label, clf_module, train_size, test_size):
	# doc: `run_sklearn` means to run the different classification on different training&testing datasets size

	# arg: mnist_data   Note: The MNIST image data from MNIST origin file.
	# arg: mnist_label  Note: The MNIST labels from MNIST origin file.
	# arg: clf_module   Note: The classification class from SVM module.
	# arg: train_size   Note: The expect training dataset size.
	# arg: test_size    Note: The expect testing dataset size.

    # return: None

	print("|-------------------------------------|") # Pre print
	print("| Now Train Size: {}, Test Size: {}".format(train_size, test_size)) # Print the training size and testing size
	print("| Use {}".format(clf_module.__name__)) # Print the class name
	clf = clf_module() # Instantiation
	data_train, data_test, label_train, label_test = model_selection.train_test_split(mnist_data, mnist_label, test_size=test_size, train_size=train_size)
	# Split the MNIST dataset by training&testing size
	clf.fit(data_train, label_train) # Training
	pre = clf.predict(data_test) # Testing

	ac_score = metrics.accuracy_score(label_test, pre) # Get the accuracy rate
	print("| Accuracy Rate: {}".format(ac_score)) # Print it
	print("|-------------------------------------|")


def run():
	# doc: Just run

	run_sklearn(mnist_data, mnist_label, svm.SVC, 500, 100)
	run_sklearn(mnist_data, mnist_label, svm.NuSVC, 500, 100)
	run_sklearn(mnist_data, mnist_label, svm.LinearSVC, 500, 100)
	run_sklearn(mnist_data, mnist_label, svm.SVC, 5000, 1000)
#	run_sklearn(mnist_data, mnist_label, svm.NuSVC, 5000, 1000)
#	run_sklearn(mnist_data, mnist_label, svm.LinearSVC, 5000, 1000)

	run_sklearn(mnist_data, mnist_label, svm.SVC, 67000, 2000)


if __name__ == "__main__":
	# The main function

	run()