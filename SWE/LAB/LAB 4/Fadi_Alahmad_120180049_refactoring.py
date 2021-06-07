import unittest
import os
import config
import pandas as pd
import pickle
import sys
import traceback
import time


# Generic Function to print exception messages for all functions.
def print_exception_message(message_orientation="horizontal"):
    """
    print full exception message
   :param message_orientation: horizontal or vertical
   :return None
    """
    try:
        exc_type, exc_value, exc_tb = sys.exc_info()
        file_name, line_number, procedure_name, line_code = traceback.extract_tb(exc_tb)[-1]
        time_stamp = " [Time Stamp]: " + str(time.strftime("%Y-%m-%d %I:%M:%S %p"))
        file_name = " [File Name]: " + str(file_name)
        procedure_name = " [Procedure Name]: " + str(procedure_name)
        error_message = " [Error Message]: " + str(exc_value)
        error_type = " [Error Type]: " + str(exc_type)
        line_number = " [Line Number]: " + str(line_number)
        line_code = " [Line Code]: " + str(line_code)
        if message_orientation == "horizontal":
            print("An error occurred:{};{};{};{};{};{};{}".format(time_stamp, file_name, procedure_name,
                                                                  error_message, error_type, line_number, line_code))
        elif message_orientation == "vertical":
            print("An error occurred:\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(time_stamp, file_name,
                                                                          procedure_name, error_message, error_type,
                                                                          line_number, line_code))
        else:
            pass
    except:
        exception_message = sys.exc_info()[0]
        print("An error occurred. {}".format(exception_message))


def tune_hyperparameter_model(ml_model, X_train, y_train, hyper_parameter_candidates, scoring_parameter, cv_fold,
                              search_cv_type="grid"):
    """
    apply grid search cv and randomized search cv algorithms to
    find optimal hyperparameters model
    :param ml_model: defined machine learning model
    :param X_train: feature training data
    :param y_train: target (label) training data
    :param hyper_parameter_candidates: dictionary of
     hyperparameter candidates
    :param scoring_parameter: parameter that controls what metric
     to apply to the evaluated model
    :param cv_fold: number of cv divided folds
    :param search_cv_type: type of search cv (gridsearchcv or
     randomizedsearchcv)
    :return classifier_model: defined classifier model
    """
    try:
        if (search_cv_type == config.GRID_SEARCH_CV):
            classifier_model = GridSearchCV(estimator=ml_model,
                                            param_grid=hyper_parameter_candidates,
                                            scoring=scoring_parameter, cv=cv_fold)
        elif (search_cv_type == config.RANDOMIZED_SEARCH_CV):
            classifier_model = RandomizedSearchCV(estimator=ml_model,
                                                  param_distributions=hyper_parameter_candidates,
                                                  scoring=scoring_parameter, cv=cv_fold)
        classifier_model.fit(X_train, y_train)
    except:
        print_exception_message()
    return classifier_model


# svc model
ml_model = SVC()
hyper_parameter_candidates = {"C": [1e-4, 1e-2, 1, 1e2, 1e4],
                              "gamma": [1e-3, 1e-2, 1, 1e2, 1e3],
                              "class_weight": [None, "balanced"],
                              "kernel": ["linear", "poly", "rbf", "sigmoid"]}
scoring_parameter = "accuracy"
cv_fold = KFold(n_splits=5, shuffle=True, random_state=1)
classifier_model = tune_hyperparameter_model(ml_model, X_train,
                                             y_train, hyper_parameter_candidates, scoring_parameter,
                                             cv_fold)

# ann model
ml_model = MLPClassifier()
hyper_parameter_candidates = {"hidden_layer_sizes": [(20), (50),
                                                     (100)], "max_iter": [500, 800, 1000],
                              "activation": ["identity", "logistic", "tanh", "relu"],
                              "solver": ["lbfgs", "sgd", "adam"]}
scoring_parameter = "accuracy"
cv_fold = KFold(n_splits=5, shuffle=True, random_state=1)
classifier_model = tune_hyperparameter_model(ml_model, X_train,
                                             y_train, hyper_parameter_candidates, scoring_parameter,
                                             cv_fold)


class ANNTest(unittest.TestCase):
    """
    ann unit test class
    """

    def testAccuracyScore(self):
        """
        accuracy classification score unit test
        """
        #        get data folder path
        data_folder_path = config.DATA_FOLDER_PATH
        #         define fashion mnist test pandas dataframe
        fashion_mnist_test = config.FASHION_MNIST_TEST
        df_fashion_mnist_test = pd.read_csv(os.path.join(data_folder_path,
                                                         fashion_mnist_test), header=None)
        #         get number of columns
        df_fashion_mnist_test_columns = df_fashion_mnist_test.shape[1]
        #         select y test label
        target_column_number = config.TARGET_COLUMN_NUMBER
        y_test = df_fashion_mnist_test.iloc[:, 0:target_column_number]
        #         flat y test label
        y_test_flattened = y_test.values.ravel()
        #         select X test features
        X_test = df_fashion_mnist_test.iloc[:, target_column_number: df_fashion_mnist_test_columns]
        #         normalize X test features with min-max scaling
        X_test = (X_test.astype("float32") - config.XMIN) / (config.XMAX - config.XMIN)
        #         open and close fashion mnist model pkl file
        mlp_classifier_model_pkl = open(config.FASHION_MNIST_MODEL_FILE, "rb")
        mlp_classifier_model_file = pickle.load(mlp_classifier_model_pkl)
        mlp_classifier_model_pkl.close()
        #         get y predict test
        y_predict_test = mlp_classifier_model_file.predict(X_test)
        #         calculate accuracy classification score
        accuracy_score_value = calculate_accuracy_score(y_test_flattened,
                                                        y_predict_test)
        #         test for accuracy score value greater than or equal to threshold accuracy score
        self.assertGreaterEqual(accuracy_score_value,
                                config.THRESHOLD_ACCURACY_SCORE, "Test Accuracy Score Failed.")


if __name__ == "__main__":
    unittest.main()
