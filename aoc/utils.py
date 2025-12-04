from typing import TypeVar
import numpy as np
from numpy.typing import NDArray

T = TypeVar("T", bound=np.generic)


def get_neighbors(arr: NDArray[T], r: int, c: int, include_self=False) -> NDArray[T]:
    # Determine slice bounds, staying inside array limits
    r_min = max(0, r - 1)
    r_max = min(arr.shape[0], r + 2)
    c_min = max(0, c - 1)
    c_max = min(arr.shape[1], c + 2)

    # Extract the region
    region = arr[r_min:r_max, c_min:c_max]

    if include_self:
        return region
    else:
        # Remove center element
        neighbors = region.copy().reshape(-1)
        neighbors = np.delete(neighbors, (r - r_min) * region.shape[1] + (c - c_min))
        return neighbors
