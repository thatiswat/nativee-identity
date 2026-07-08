# Nativee Identity

The centralized authentication and identity platform powering the Nativee ecosystem.

Nativee Identity is responsible for authentication, authorization, session management, and RS256 JWT issuance for every Nativee application and service.

It serves as the single source of truth for user identity, allowing the API, AI Engine, Web, Mobile, and future services to remain stateless and independently scalable.

---

# Overview

```text
                     Nativee Platform

              Mobile • Web • SDKs • CLI
                        │
                        ▼
                 Nativee Identity
        Authentication • Sessions • JWT
                        │
                 RS256 Access Token
                        │
          ┌─────────────┴─────────────┐
          ▼                           ▼
     Nativee API               Nativee Engine
 Business Platform             AI Runtime
```

---

# Responsibilities

Nativee Identity owns

- User Registration
- User Authentication
- Password Security
- Session Management
- Refresh Tokens
- JWT Generation
- JWT Verification
- Identity Claims
- Email Verification (Upcoming)
- Password Reset (Upcoming)
- OAuth Providers (Upcoming)
- Multi-Factor Authentication (Upcoming)

Nativee Identity never owns

- Projects
- API Keys
- Usage
- Analytics
- Billing
- AI Execution

Those responsibilities belong to Nativee API and Nativee Engine.

---

# Features

## Authentication

- Register
- Login
- Logout
- Refresh Tokens
- Current User
- Password Hashing (bcrypt)

---

## Security

- RS256 JWT
- RSA Public / Private Keys
- Refresh Token Rotation
- Session Tracking
- JWT Claims Validation
- Token Expiration
- Issuer Validation
- Audience Validation

---

## Identity

- Public User IDs
- Device Sessions
- Identity Claims
- Independent Authentication Service

---

## Database

- PostgreSQL
- SQLAlchemy
- Alembic Migrations

---

# Tech Stack

- Python 3.12+
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
nativee-identity/

├── app/
│
├── api/
│
├── core/
│
├── database/
│
├── dependencies/
│
├── middleware/
│
├── models/
│
├── repositories/
│
├── schemas/
│
├── services/
│
├── utils/
│
└── keys/
│
├── alembic/
│
├── main.py
│
└── requirements.txt
```

---

# Authentication Flow

```text
User

↓

Register

↓

Identity Database

↓

Login

↓

Create Session

↓

Generate RS256 JWT

↓

Return Access Token

↓

Nativee API

↓

Verify JWT

↓

Platform Access
```

---

# JWT Structure

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
  "iss": "https://identity.nativee.in",
  "aud": "nativee"
}
```

---

# Authentication Lifecycle

```text
Register

↓

Login

↓

Access Token (15 min)

↓

Refresh Token (30 days)

↓

Refresh

↓

New Access Token

↓

Logout

↓

Session Revoked
```

---

# Database

## Current Tables

- users
- auth_sessions

---

## Planned Tables

- email_verifications
- password_resets
- oauth_accounts
- user_devices
- mfa_recovery_codes

---

# Environment Variables

```env
DATABASE_URL=

IDENTITY_ISSUER=

IDENTITY_AUDIENCE=nativee

IDENTITY_ALGORITHM=RS256

ACCESS_TOKEN_EXPIRE_MINUTES=15

REFRESH_TOKEN_EXPIRE_DAYS=30

JWT_PRIVATE_KEY=

JWT_PUBLIC_KEY=
```

---

# Local Development

## Install

```bash
pip install -r requirements.txt
```

---

## Run Database Migrations

```bash
alembic upgrade head
```

---

## Start Server

```bash
uvicorn main:app --reload
```

---

# API Documentation

Swagger

```
http://127.0.0.1:8000/docs
```

---

# API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/auth/register` | Register a new user |
| POST | `/auth/login` | Authenticate user |
| POST | `/auth/refresh` | Refresh access token |
| POST | `/auth/logout` | Revoke current session |
| GET | `/auth/me` | Current authenticated user |

---

# Platform Relationships

```text
                 Nativee Platform

           Nativee Identity
                  │
            RS256 JWT
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
   Nativee API        Nativee Engine
```

Nativee Identity authenticates users.

Nativee API manages business resources.

Nativee Engine executes AI workloads.

---

# Current Status

## Completed

- User Registration
- User Login
- RS256 JWT
- Refresh Tokens
- Session Management
- Railway Deployment
- Independent PostgreSQL Database
- Nativee API Integration

---

## In Progress

- Automatic Business User Provisioning
- Email Verification
- Password Reset

---

## Planned

### Identity

- Google OAuth
- GitHub OAuth
- Microsoft OAuth

### Security

- MFA
- Passkeys
- WebAuthn

### Enterprise

- Organizations
- Roles
- Permissions
- RBAC
- SSO

---

# Design Principles

Nativee Identity follows four core principles.

- Authentication is centralized.
- Identity is independent of business data.
- Every service verifies, but never issues, JWTs.
- Authentication scales independently from application services.

---

# License

**Proprietary Software**

Copyright © Nativee Technologies.

All rights reserved.