# Nativeee Identity

> Centralized authentication and identity service powering the Nativeee platform.

Nativeee Identity is responsible for user authentication, authorization, session management, and JWT issuance across the Nativeee ecosystem.

It acts as the single source of truth for user identity while allowing other services to remain stateless and independently scalable.

---

# Architecture

```text
                Mobile App
                     │
                Web Dashboard
                     │
                     ▼
             Nativeee Identity
                     │
          RS256 Signed JWT Tokens
                     │
      ┌──────────────┴──────────────┐
      ▼                             ▼
 Nativeee API                 Nativeee Engine
```

---

# Responsibilities

- User Registration
- User Login
- JWT Access Tokens
- Refresh Tokens
- Session Management
- Device Sessions
- Email Verification
- Password Reset
- OAuth Providers (Upcoming)
- Multi-Factor Authentication (Upcoming)

---

# Features

## Authentication

- Register
- Login
- Logout
- Refresh Tokens
- Current User
- Password Hashing (bcrypt)

## Security

- RS256 JWT
- RSA Key Pair
- Refresh Token Rotation
- Session Tracking
- Token Expiration
- JWT Claims Validation

## Database

- PostgreSQL
- SQLAlchemy ORM
- Alembic Migrations

---

# Tech Stack

- Python 3.11+
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- python-jose
- Passlib
- Uvicorn

---

# Project Structure

```text
nativeee-identity/

├── app/
│   ├── api/
│   ├── core/
│   ├── database/
│   ├── models/
│   ├── repositories/
│   ├── schemas/
│   ├── services/
│   ├── utils/
│   └── keys/
│
├── alembic/
├── main.py
└── requirements.txt
```

---

# Authentication Flow

```text
Register
    │
    ▼
Identity Database
    │
    ▼
Login
    │
    ▼
Access Token
    │
    ▼
Refresh Token
    │
    ▼
Nativeee API
    │
    ▼
Verified User
    │
    ▼
Platform Access
```

---

# JWT

Access Tokens are signed using **RS256**.

## Example Claims

```json
{
  "sub": "1",
  "pid": "usr_xxxxxxxxx",
  "email": "user@example.com",
  "name": "John Doe",
  "role": "user",
  "sid": "ses_xxxxxxxxx",
  "is_active": true,
  "type": "access",
  "iss": "https://identity.nativeee.in",
  "aud": "nativeee"
}
```

---

# Database

## Core Tables

- users
- sessions

## Future Tables

- email_verifications
- password_resets
- oauth_accounts
- devices
- mfa_recovery_codes

---

# Environment Variables

```env
DATABASE_URL=

IDENTITY_ISSUER=

IDENTITY_AUDIENCE=nativeee

IDENTITY_ALGORITHM=RS256

ACCESS_TOKEN_EXPIRE_MINUTES=15

REFRESH_TOKEN_EXPIRE_DAYS=30

JWT_PRIVATE_KEY=

JWT_PUBLIC_KEY=
```

---

# Local Development

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Migrations

```bash
alembic upgrade head
```

## Start the Server

```bash
uvicorn main:app --reload
```

---

# Swagger

```
http://localhost:8000/docs
```

---

# API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/auth/register` | Register a user |
| POST | `/auth/login` | Login |
| POST | `/auth/refresh` | Refresh access token |
| POST | `/auth/logout` | Logout |
| GET | `/auth/me` | Current authenticated user |

---

# Roadmap

## Version 1

- ✅ Registration
- ✅ Login
- ✅ RS256 JWT
- ✅ Refresh Tokens
- ✅ Session Management

## Version 2

- Email Verification
- Password Reset
- Google OAuth
- GitHub OAuth

## Version 3

- Organizations
- Roles
- Permissions
- RBAC

## Version 4

- MFA
- Passkeys
- WebAuthn

---

# License

Copyright © Nativeee.

All rights reserved.