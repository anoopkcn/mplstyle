# mplstyle
matplotlib plot styles

## installation
**Activate your python environment then do:**
```bash
git clone https://github.com/anoopkcn/mplstyle.git 
cd mplstyle
pip install -e .
```
Where `-e` argument make sure that when you make a change in the package it is reflected in the import without needing to install it again. 

## Usage
Import library 
```python
from mplstyle import styles
```
Create an object. Note that when you create the object with a specific style template name, this template is applied instead of the matplotlib default

```python
st=styles.Style('academic')
```
Where `academic` is a `mplstyle` template.  To revert back to default `matplotlib` template simply create the object without any arguments

```python
st=styles.Style()
```

Example code:
```python
st=styles.Style('academic')

x = np.linspace(-np.pi, np.pi, 100)

fig = plt.figure(figsize=(10, 4))

with mpl.rc_context({'axes.grid':True}):
    ax1 = fig.add_subplot(1, 2, 1)
    ax1.plot(x, np.sin(x))

with mpl.rc_context():
    ax2 = fig.add_subplot(1, 2, 2)
    ax2.plot(x, np.cos(x),color='tab:green')

with mpl.rc_context():
    panel = ax2.inset_axes([0.35,0.2,0.3,0.3])
    panel.plot(x, np.sin(x), color="tab:orange")
```
Output:
![threepanel_since]('examples/three_panel.svg')