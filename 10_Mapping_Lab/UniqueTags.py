# Implement unique_tags(tags). Clean each tag by stripping spaces and converting to lowercase. Ignore empty tags. Return a sorted list of unique cleaned tags.
def unique_tags(tags):
    cleaned_tags = set()
    
    for tag in tags:
        # Strip whitespace and convert to lowercase
        cleaned = tag.strip().lower()
        
        # Only add non-empty strings
        if cleaned:
            cleaned_tags.add(cleaned)
            
    # Return as a sorted list
    return sorted(cleaned_tags)