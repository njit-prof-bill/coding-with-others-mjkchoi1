def longest_substring_k_unique(s: str, k: int) -> int:
    if len(s) == 0 or k == 0:
        return 0
    
    char_count = {}
    left = 0
    max_len = 0
    
    # Iterate over the string using the right pointer
    for right in range(len(s)):
        # Add the current character to the map
        if s[right] in char_count:
            char_count[s[right]] += 1
        else:
            char_count[s[right]] = 1
        
        # If we have more than k unique characters, shrink the window from the left
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        
        # If the number of unique characters is exactly k, calculate the length
        if len(char_count) == k:
            max_len = max(max_len, right - left + 1)
    
    return max_len

