# cluster-ensembles

A Python package for cluster ensembles. Cluster ensembles generate a single consensus clustering label by using base labels obtained from multiple clustering algorithms. The consensus clustering label stably achieves a high clustering performance. 

<p align="center">
  <img width="600" src="https://user-images.githubusercontent.com/60049342/115107122-deb7b880-9fa3-11eb-98d6-9d1d25bf3ae8.png">
</p>

Installation
------------

```
pip install git+https://github.com/tsano430/cluster-ensembles.git
```

Usage
-----

`CE.cluster_ensembles` is used as follows.

```python
>>> import numpy as np

>>> import cluster_ensembles as CE

>>> label1 = np.array([1, 1, 1, 2, 2, 3, 3])

>>> label2 = np.array([2, 2, 2, 3, 3, 1, 1])

>>> label3 = np.array([4, 4, 2, 2, 3, 3, 3])

>>> label4 = np.array([1, 2, np.nan, 1, 2, np.nan, np.nan]) # `np.nan`: missing value

>>> labels = np.array([label1, label2, label3, label4])

>>> label_ce = CE.cluster_ensembles(labels)

>>> print(label_ce)
[1 1 1 2 2 0 0]
```

#### Parameters

- `labels`: *numpy.ndarray*
  
  Labels generated by multiple clustering algorithms such as K-Means. 
  
  **Note:** Assume that the length of each label is the same. 

- `nclass`: *int, default=None*
  
  Number of classes in a consensus clustering label. 
  If `nclass=None`, set the maximum number of classes in each label except missing values. 
  In other words, set `nclass=3` automatically in the above.

- `solver`: *{'cspa', 'hgpa', 'mcla', 'hbgf', 'nmf', 'all'}, default='hbgf'*
    
    'cspa': Cluster-based Similarity Partitioning Algorithm [1].

    'hgpa': HyperGraph Partitioning Algorithm [1].

    'mcla': Meta-CLustering Algorithm [1].
    
    'hbgf': Hybrid Bipartite Graph Formulation [2].

    'nmf': NMF-based consensus clustering [3].

    'all': The consensus clustering label with the largest objective function value [1] is returned among the results of all solvers. 
    
    <p align="center">
      <img width="600" src="https://user-images.githubusercontent.com/60049342/116185712-20dbb980-a75d-11eb-87cb-ae0e68179674.png">
    </p>

    **Note:** Please use 'hbgf' for large-scale `labels`.

- `random_state`: *int, default=None*
  
  Used for 'hgpa', 'mcla', and 'nmf'. Please pass an integer for reproducible results.

- `verbose`: *bool, default=False*
  
  Whether to be verbose.

#### Return

- `label_ce`: *numpy.ndarray*
  
  A consensus clustering label generated by cluster ensembles. 
    

References
----------

[1] A. Strehl and J. Ghosh, 
"Cluster ensembles -- a knowledge reuse framework for combining multiple partitions,"
Journal of Machine Learning Research, vol. 3, pp. 583-617, 2002.

[2] X. Z. Fern and C. E. Brodley, 
"Solving cluster ensemble problems by bipartite graph partitioning,"
In Proceedings of the Twenty-First International Conference on Machine Learning, p. 36, 2004.

[3] T. Li, C. Ding, and M. I. Jordan, 
"Solving consensus and semi-supervised clustering problems using nonnegative matrix factorization," 
In Proceedings of the Seventh IEEE International Conference on Data Mining, pp. 577-582, 2007.

[4] J. Ghosh and A. Acharya, 
"Cluster ensembles," 
Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery, vol. 1, no. 4, pp. 305-315, 2011. 