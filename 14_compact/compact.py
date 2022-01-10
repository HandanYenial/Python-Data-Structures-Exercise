def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    the_list=[]
    for element in lst:
        if element:
            the_list.append(element)
    return the_list