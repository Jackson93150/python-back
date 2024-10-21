from rest_framework.throttling import UserRateThrottle

class AuthenticationThrottle(UserRateThrottle):
    scope = 'user'