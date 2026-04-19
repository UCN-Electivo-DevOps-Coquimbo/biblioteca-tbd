# Active User Session

This folder provides a simple active-user session using the Singleton pattern.

## What it does

- Keeps only one user session instance while the app is running.
- Lets any module read the logged-in user with `UserSession()`.
- Supports session reset with `logout()`.

## Files

- `singleton.py`: Base Singleton behavior.
- `user_session.py`: User session data (`id`, `name`, `email`, `password`, `rol`).

## How it is implemented

1. `UserSession` inherits from `Singleton`.
2. `Singleton.__new__()` returns the same instance for the class.
3. `UserSession.__init__()` runs only once (using `initialized`).
4. `UserSession.logout()` clears data and allows a fresh session.

## How to use

### 1) Create session after login

```python
from singletons.user_session import UserSession

# Optional: clear previous session
session = UserSession()
session.logout()

# Create active session
session = UserSession(
    id=user["id"],
    name=user["name"],
    email=user["email"],
    password=user["password"],
    rol=user["rol"],
)
```

### 2) Read active user anywhere

```python
from singletons.user_session import UserSession

active_user = UserSession()
print(active_user.email)
print(active_user.rol)
```

### 3) Logout

```python
from singletons.user_session import UserSession

UserSession().logout()
```

## Notes

- Designed for a single-process console app.
- Not intended for concurrent multi-user server sessions.
- Avoid printing or exposing passwords in logs.
