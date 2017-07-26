import numpy as np

def featureFormat( dictionary, features):


    return_list = []

    keys = dictionary.keys()

    for key in keys:

        tmp_list = []
        for feature in features:
            try:
                dictionary[key][feature]
            except KeyError:
                print ("error: key ", feature, " not present")
                return
            value = dictionary[key][feature]

            tmp_list.append(float(value) )

        return_list.append( np.array(tmp_list) )

    return np.array(return_list)


def targetFeatureSplit( data ):

    target = []
    features = []
    for item in data:
        target.append( item[0] )
        features.append( item[1:] )

    return target, features
