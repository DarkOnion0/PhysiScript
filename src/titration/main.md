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

## Usage

```code
print("Hello World!")
```
