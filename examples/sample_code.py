def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    if not numbers:
        raise ValueError("The list cannot be empty")
    return sum(numbers) / len(numbers)
