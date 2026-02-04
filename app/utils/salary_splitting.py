# def salary_splitting(salary):
#     """
#     Splits a salary string into min_salary and max_salary.
#     - Single values go into min_salary, max_salary = None
#     - Ranges are split on '～'
#     - Handles commas and '円'
#     """
#     if salary is None:
#         return (None, None)

#     # Convert to string and clean
#     salary = str(salary).replace(" ", "").replace("円", "").replace(",", "")

#     # Check for range
#     if '～' in salary:
#         parts = salary.split('～')

#         # If both values exist → proper range
#         if parts[0] and len(parts) > 1 and parts[1]:
#             try:
#                 min_salary = int(parts[0])
#             except:
#                 min_salary = None
#             try:
#                 max_salary = int(parts[1])
#             except:
#                 max_salary = None
#             return (min_salary, max_salary)

#         # Otherwise → treat as single value (min only)
#         try:
#             min_salary = int(parts[0] or parts[1])
#             return (min_salary, None)
#         except:
#             return (None, None)

#     # Single number → only min_salary
#     try:
#         min_salary = int(salary)
#         return (min_salary, None)
#     except:
#         return (None, None)




# -----------------------Salary Splitting for Both english and japanese text---------------------------

import re

def salary_splitting(salary):
    """
    General salary splitter.

    Returns:
        (min_salary, max_salary)

    Handles:
        - 300,000 to 450,000
        - 300,000～450,000
        - 280,000~
        - From 290,000 yen
        - 300,000 and up
        - 285,000 yen
        - 250000
        - None
    """

    if salary is None:
        return (None, None)

    # Convert to string & normalize
    salary_str = str(salary).lower()

    # Remove currency & unnecessary words
    salary_str = (
        salary_str
        .replace("yen", "")
        .replace("円", "")
        .replace(",", "")
        .strip()
    )

    # Extract all numbers
    numbers = re.findall(r"\d+", salary_str)
    numbers = [int(n) for n in numbers]

    if not numbers:
        return (None, None)

    # Detect range keywords
    range_keywords = ["to", "～", "~", "-", "–", "—"]

    # CASE 1 → Proper range
    if any(k in salary_str for k in range_keywords) and len(numbers) >= 2:
        return (numbers[0], numbers[1])

    # CASE 2 → From / and up / trailing ~
    if (
        "from" in salary_str
        or "and up" in salary_str
        or salary_str.endswith("~")
        or salary_str.endswith("～")
    ):
        return (numbers[0], None)

    # CASE 3 → Single value
    return (numbers[0], None)