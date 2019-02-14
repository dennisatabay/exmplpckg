""" The function get_parameter() is supposed to return parameters saved
in a csv file /settings/settings_file.csv within this package

"""
import pandas as pd
import pkg_resources


def get_parameter(parameter):
    """ Read settings csv file in /settings/settings_file.csv in this package
    
    Parameters
    ----------
    parameter : str
        parameter to read
        
    Returns
    -------
    float
        value of the parameter
    str
        comment for the parameter
    """
    
    # get module name
    resource_package = __name__
    
    print(resource_package)
    
    # path to file within package
    resource_path = 'settings/settings_file.csv'
    
    csv_file = pkg_resources.resource_stream(resource_package, resource_path)
    
    df = pd.read_csv(csv_file, sep=',', index_col=[0])
        
    value = df.loc[parameter,'value']
    comment = df.loc[parameter,'comment']
    
    return value, comment