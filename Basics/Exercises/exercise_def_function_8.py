def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


info_ntesla = build_profile('nikola', 'tesla', born=1856, died=1943,
                            discipline='electrical engineering')

print(info_ntesla)
