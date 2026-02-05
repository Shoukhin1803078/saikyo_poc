def extract_job_urls_from_output(output):
    """
    Extract unique serial_no from output and return frontend-ready URLs.
    """
    base_url = "https://fudosanworks.com/jobs/details"
    seen = set()
    urls = []

    for item in output:
        serial_no = item.get("serial_no")
        if serial_no and serial_no not in seen:
            seen.add(serial_no)
            urls.append(f"{base_url}/{serial_no}")

    return urls
