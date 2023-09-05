#!/usr/bin/python3
"""Defines matrix mult using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return multi of two matrices.

    Args:
        m_a:first matrix.
        m_b:second matrix.
    """

    return (np.matmul(m_a, m_b))
