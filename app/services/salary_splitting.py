def salary_splitting(salary):
    """
    Splits a salary string into min_salary and max_salary.
    - Single values go into min_salary, max_salary = None
    - Ranges are split on '～'
    - Handles commas and '円'
    """
    if salary is None:
        return (None, None)

    # Convert to string and clean
    salary = str(salary).replace(" ", "").replace("円", "").replace(",", "")

    # Check for range
    if '～' in salary:
        parts = salary.split('～')

        # If both values exist → proper range
        if parts[0] and len(parts) > 1 and parts[1]:
            try:
                min_salary = int(parts[0])
            except:
                min_salary = None
            try:
                max_salary = int(parts[1])
            except:
                max_salary = None
            return (min_salary, max_salary)

        # Otherwise → treat as single value (min only)
        try:
            min_salary = int(parts[0] or parts[1])
            return (min_salary, None)
        except:
            return (None, None)

    # Single number → only min_salary
    try:
        min_salary = int(salary)
        return (min_salary, None)
    except:
        return (None, None)