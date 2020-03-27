def make_time_series_lowess(x_list, y_list):
    """
    x_list:  dateime object
    y_list:  actual values
    
    This function takes as input x_values in a date format and y values and returns values based on a lowess smoother function in statsmodels.
    """
    from datetime import timezone
    import statsmodels.api as sm

    lowess = sm.nonparametric.lowess

    x_list = list(difference_subset.columns)
    x_list = [dt.datetime.strptime(item, '%m/%d/%y') for item in x_list]
    x_list = [item.replace(tzinfo=timezone.utc).timestamp() for item in x_list]

    y_list = list(difference_subset.iloc[0:,].values[0])

    # lowess will return our "smoothed" data with a y value for at every x-value
    lowess = sm.nonparametric.lowess(y_list, x_list, frac=.3)

    # unpack the lowess smoothed points to their values
    #x_lowess = list(zip(*lowess))[0]
    y_lowess = list(zip(*lowess))[1]

    # convert to a list
    #x_lowess = [item for item in lowess_x]
    y_lowess = [item for item in lowess_y]

    # convert the size of the lowess list to the list's original size
    #x_lowess.insert(0,x_list[0])
    y_lowess.insert(0,y_list[0])

    # convert the list from unix time to a regular time stamp
    #x_list = [(dt.datetime.fromtimestamp(unix_time)).strftime('%m/%d/%y') for unix_time in x_list]
    #x_lowess =  [(dt.datetime.fromtimestamp(unix_time)).strftime('%m/%d/%y') for unix_time in x_lowess]

    return y_lowess