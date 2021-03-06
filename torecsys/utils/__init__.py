r"""torecsys.utils is a sub module of utils
"""
import torch
from typing import Callable, Union

def get_reduction(method: Union[Callable[[torch.Tensor], torch.Tensor], str]) \
    -> Callable[[torch.Tensor], torch.Tensor]:
    r"""[summary]
    Args:
        method Union[Callable[[torch.Tensor], torch.Tensor], str]: method of reduction.
    
    Raises:
        AssertionError: when method is not found.
        TypeError: when type of method is not allowed.
    
    Returns:
        Callable[torch.Tensor], torch.Tensor]: Method of reduction.
    """
    if isinstance(method, str):
        reduction_method = getattr(torch, method, None)
        if reduction_method is None:
            raise AssertionError(f"{method} not found.")
    elif callable(method):
        reduction_method = method
    else:
        raise TypeError(f"{type(method).__name__} not allowed.")
    
    return reduction_method
    