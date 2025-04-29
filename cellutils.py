# Function
def scale_counts(expmat):
    '''
    These are called docstrings and are placed between three single quotes.
    Here, you can put your guide on how to use a function.
    It can be called by using help(scale_counts)

    This function scales the expression matrix.

    Parameters
    ----------
    expmat : np.ndarray
        Expression matrix in cell x gene format with count data for expression.

    Returns
    -------
    np.ndarray
        Expression matrix standardised based on the matrix sum.
    '''
    return expmat / expmat.sum(axis=1, keepdims=True)

# Class
class Cell:
    def __init__(self, id, expression):
        '''
        Parameters
        ----------
        id : str
            Identifier for the cell.
        expression : dict
            Dictionary of {gene_name: expression_value}.
        '''
        self.id = id
        self.expression = expression
        
    def get_expression(self, gene):
        '''Return the expression level of a single gene.'''
        return self.expression.get(gene, np.nan)  # returns np.nan if gene missing

    def plot_expression(self, gene1, gene2):
        '''Placeholder for a plotting function comparing two genes.'''
        pass  # you can implement later

    def remove_zero_expression(self, gene):
        '''Placeholder for a function that removes genes with zero expression.'''
        pass

    def get_max_expressin(self, gene):
        '''Placeholder for a function that tells you gene(s) with highest expression.'''
        pass