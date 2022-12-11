#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thursday Oct 06 2022

@author: Xing Geng

"""

def top10_value(data,reference_col,sorting_col):
    import pandas as pd
    """
    Given a dataframe, selecting two columns of a reference column and a sorting column, return a dataframe that has     been sorted by the column and given the top 10 values of that column.
    
    Parameters
    ----------
    data : pandas.core.frame.DataFrame
        The dataframe to sample from
    reference_col : str
        The column to give the comparison information
    sorting_col : str
        The column for sorting values
   
        
    Returns
    -------
    pandas.core.frame.DataFrame 
        A dataframe with the group by column and the result of the top values.
        
    Raises
    ------
    TypeError
        If the input argument data is not of type pandas.core.frame.DataFrame
    AssertError
        If the input argument reference_col is not in the data columns
    AssertError
        If the input argument sorting_col is not in the data columns
    
    Examples
    --------
    >>> top10_value(helper_data)

	1937	 0
    2015	 6

    """
    
    # Checks if a dataframe is the type of object being passed into the data argument
    if not isinstance(data, pd.DataFrame): 
        raise TypeError("The data argument is not of type DataFrame")
    
    # Tests that the reference column is in the dataframe
    assert reference_col in data.columns, "The reference column does not exist in the dataframe"
    
    # Tests that the the sorting column is insorting column does not exist in the dataframe"
    
    
   
    # selecting the two columns and convert to a dataframe
    res = pd.DataFrame(data,columns=[reference_col,sorting_col])
    
    # sorting values
    
    res=res.sort_values(sorting_col,ascending=False)
    
    # reset the index
    res = res.reset_index()
    
    # selecting the top10 values
    
    res = res.loc[0:9]
    
    # drop the index
    
    res = res.drop('index',axis=1)
    
    #return the result
    return(res)