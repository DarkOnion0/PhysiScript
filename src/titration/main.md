## Code

```code
import numpy as np
```

```{include=src/titration/main.py .code}

```

## Example

```code
titragePH(
    title="Titrage ph-Métrique",
    x=["$V \ (mL)$", np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 19, 19.3, 19.5, 20, 21, 23])],
    y=["$pH$", np.array([10.9, 10.2, 9.8, 9.6, 9.5, 9.3, 9.1, 8.9, 8.6, 8.1, 7.2, 4.0, 3.1, 2.6, 2.3, 2.0])],
    showVeLine=True,
)
```

```code
titrageConductimetrique(
    title="Titrage conductimétrique",
    x=["$V \ (mL)$", np.array([0,0.5,1,1.5,2.2,2.6,3,3.6,4.1,4.5,5,5.6,6,6.6,7,7.4,7.8,8,8.2,8.5,8.8,9,9.6,10.1,10.4,10.6,10.8,11,11.5,12])],
    y=["$\sigma \ (mS \cdot m^{-1})$", np.array([11.18,10.71,10.33,9.92,9.35,9.03,8.72,8.21,7.92,7.62,7.27,6.87,6.63,6.25,5.99,5.77,5.55,5.45,5.38,5.31,5.26,5.25,5.27,5.51,5.98,6.29,6.55,6.91,7.67,8.41])],
    split = 21,
    showVeLine=True,
)
```

## Usage

```code
print("Hello World!")
```
