def linear_search(items, keyword, key=lambda x: x):
    """O(n) search: checks each item until all matches are collected."""
    keyword = keyword.lower()
    return [
        item for item in items
        if keyword in str(key(item)).lower()
    ]


def sort_by_salary(items, descending=False):
    """Python's Timsort is O(n log n) on typical inputs."""
    return sorted(items, key=lambda item: item["salary"], reverse=descending)
