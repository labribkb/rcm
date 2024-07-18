# RCM

Implementation of RCM: Relative Confusion Matrix

Illustration of the tool to display a RCM from two confusion matrices. 
![image](./RCM.png)


# Description

This code provides an implementation of the RCM to compare two classification models (A and B) on the class-performance level. 
In particular, the visualization highlights the differences between two models. 

The design is inspired from standard confusion matrices: 
- Rows denote ground truth labels.
- Columns denote prediction labels.
- Each cell encodes the difference cell-by-cell between two standard confusion matrices. 
- A $+$ symbol means model B performs better than model A in that cell. 
- A $-$ symbol means model A performs better than model B in that cell. 
- The absence of symbols indicates A and B classify the same number of samples in that cell. 
- A gradient of colors encodes the amount of difference between A and B in that cell.
- Hovering the cells will indicate the exact difference in the number of samples between the two models, alongside the percentage of samples it represents compared to the number of samples of that class (w.r.t. to the ground truths).  

The tool is composed of several sliders to control the rendering of the visualization. In particular, the sliders respectively control: 
1. The size of the RCM.
2. The font size of the RCM headers.
3. The font size of the symbols in the matrix.
4. The percentage of symbols displayed in the matrix.

The last slider enables the user to hide some symbols to highlight the cells with the greatest differences between the two models. 

## The repository is composed of: 

- A python library `rcm` that generates the representation of an RCM
- A test script `test.py` that illustrates its use case with two random matrices

# Usage

Here is the minimal template:

```python
import rcm

# create the confusion matrices
conf_a = [...]
conf_b = [...]
labels = [...]


r = rcm.build_rcm(conf_a, conf_b, labels)
r.show(with_sliders=False)
```

> ⚠️ **_NOTE:_** This code has not been tested with more than 30 classes. 

> ⚠️ **_NOTE:_** When generating random matrices using the generator [matrix_generator.ipynb](matrix_generator.ipynb), an error can be thrown sometimes: "ValueError: low >= high". If that error happens, generating another matrix a couple of times should solve the problem. 


# Reference

If you use this code, please cite either one of these two works: 

```
@inproceedings{pomme2022relative,
  title={Relative confusion matrix: efficient comparison of decision models},
  author={Pomm{\'e}, Luc-Etienne and Bourqui, Romain and Giot, Romain and Auber, David},
  booktitle={2022 26th International Conference Information Visualisation (IV)},
  pages={98--103},
  year={2022},
  organization={IEEE}
}

```

```
@incollection{pomme2024relative,
  title={Relative Confusion Matrix: An Efficient Visualization for the Comparison of Classification Models},
  author={Pomm{\'e}, Luc Etienne and Bourqui, Romain and Giot, Romain and Auber, David},
  booktitle={Artificial Intelligence and Visualization: Advancing Visual Knowledge Discovery},
  pages={223--243},
  year={2024},
  publisher={Springer}
}

```