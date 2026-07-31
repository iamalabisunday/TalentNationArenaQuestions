# Implement unique_tags(tags). Clean each tag by stripping spaces and converting to lowercase. Ignore empty tags. Return a sorted list of unique cleaned tags.
def unique_tags(tags):
    cleaned = {
        tag.strip().lower()
        for tag in tags
        if tag.strip()
    }
    return sorted(cleaned)