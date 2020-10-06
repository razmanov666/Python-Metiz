def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for k, v in user_info.items():
        profile[k] = v
    return profile

# user_profile = build_profile('albert', 'einstein', location = 'princepton', 
#                              field = 'physics', nation = 'Germany')
# print(user_profile)                             