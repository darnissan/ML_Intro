

import sklearn
def prepare_data(training_data,new_data):
    # 1 - fill the missing value with the median
    # 2 - Normalize the data
    # 3 - create the new feature speicalProperty
    new_data_to_edit = new_data.copy()
    training_data_to_edit = training_data.copy()
    fill_missing_values_with_median(training_data_to_edit,new_data_to_edit)
    normalize_data(training_data_to_edit,new_data_to_edit)
    create_special_property(training_data_to_edit,new_data_to_edit)
    output_path="new_data.csv"
    new_data_to_edit.to_csv(output_path)


    return new_data_to_edit


def fill_missing_values_with_median(training_data,new_data):
    features_with_missing_values = training_data.columns[training_data.isnull().any()]
    for feature in features_with_missing_values:
        median = training_data[feature].median()
        training_data[feature].fillna(median, inplace = True)
        new_data[feature].fillna(median, inplace = True)

def normalize_data(training_data,new_data):

    Parameters_to_min_max = ['PCR_03','PCR_10','sugar_levels']
    Paremeters_to_standard_scaler = ['PCR_01','PCR_02','PCR_04','PCR_05','PCR_06','PCR_07','PCR_08','PCR_09']

    for parameter in Parameters_to_min_max:
        minMaxScaler = sklearn.preprocessing.MinMaxScaler(feature_range=(-1,1))
        minMaxScaler.fit(training_data[[parameter]])
        training_data[parameter] = minMaxScaler.transform(training_data[[parameter]])
        new_data[parameter] = minMaxScaler.transform(new_data[[parameter]])


    for parameter in Paremeters_to_standard_scaler:
        standardScaler = sklearn.preprocessing.StandardScaler()
        standardScaler.fit(training_data[[parameter]])
        training_data[parameter] = standardScaler.transform(training_data[[parameter]])
        new_data[parameter] = standardScaler.transform(new_data[[parameter]])


def create_special_property(training_data,new_data):
    if 'bloodtype' in training_data.columns:
        training_data['specialProperty'] = training_data['bloodtype'].isin(["O+", "B+"])
        new_data['specialProperty'] = new_data['bloodtype'].isin(["O+", "B+"])


