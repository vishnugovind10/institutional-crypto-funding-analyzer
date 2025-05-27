def validate_api_keys(credentials):
    return all(key in credentials for key in ['apiKey', 'secret'])
