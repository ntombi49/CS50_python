def convert(fraction):
    """Convert a fraction X/Y into a rounded percentage.

    Args:
        fraction (str): a string in "X/Y" format where X and Y are positive integers.

    Returns:
        int: percentage rounded to nearest integer (0-100).

    Raises:
        ValueError: if X or Y is not a positive integer, or X > Y.
        ZeroDivisionError: if Y is 0.
    """
    try:
        x_str, y_str = fraction.split("/")
        x = int(x_str)
        y = int(y_str)
    except ValueError:
        # Raised if conversion to int fails
        raise ValueError("X and Y must be integers.")

    if x < 0 or y <= 0:
        raise ValueError("X must be non-negative and Y must be pos
