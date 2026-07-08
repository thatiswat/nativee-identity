# 🏛 Nativee Identity Architecture

> Centralized authentication and identity service for the Nativee Platform.

---

# Overview

Nativee Identity is responsible for authenticating users and issuing secure RS256 JSON Web Tokens (JWTs) that are trusted across the entire Nativee ecosystem.

It is the single source of truth for user identity and authentication.

Business resources such as projects, API keys, analytics, and billing are intentionally excluded from this service and belong to Nativee API.

---

# Platform Architecture

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
      Nativee API              Nativee Engine
   Business Platform            AI Runtime
```

---

# Responsibilities

Nativee Identity owns

- User Registration
- User Login
- Password Security
- Password Hashing
- Session Management
- Refresh Tokens
- JWT Generation
- JWT Verification
- RSA Key Management
- Identity Claims

Nativee Identity never owns

- Projects
- API Keys
- Usage
- Analytics
- Billing
- AI Models
- Translation
- Speech Processing

Those responsibilities belong to Nativee API and Nativee Engine.

---

# Service Architecture

```text
HTTP Request

↓

Middleware

↓

API Routes

↓

Services

↓

Repositories

↓

PostgreSQL
```

Each layer has a single responsibility.

---

# Folder Structure

```text
app/

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

alembic/

main.py
```

---

# Layer Responsibilities

## Middleware

Responsible for

- Logging
- Request IDs
- Error Handling
- CORS
- Request Timing

---

## API Layer

Responsible for

- HTTP Endpoints
- Request Validation
- Response Serialization

The API layer never contains business logic.

---

## Services

Responsible for

- Authentication
- Login
- Registration
- Session Creation
- Refresh Tokens
- Current User

Services never communicate directly with SQL.

---

## Repositories

Responsible only for database operations.

Current repositories

- UserRepository
- AuthSessionRepository

Repositories never contain authentication logic.

---

## Schemas

Responsible for

- Request Models
- Response Models
- Shared JWT Contracts

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

Verify Password

↓

Create Session

↓

Generate Access Token

↓

Generate Refresh Token

↓

Return Tokens
```

---

# JWT Verification Flow

```text
User

↓

JWT

↓

Nativee API

↓

Verify Signature

↓

Verify Issuer

↓

Verify Audience

↓

Extract Claims

↓

Business User Resolution
```

Identity generates tokens.

Other services only verify them.

---

# JWT Structure

Access Tokens are signed using RS256.

```json
{
    "sub": "1",
    "pid": "usr_xxxxxxxxx",
    "email": "john@example.com",
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

# Database Architecture

```text
Identity Database

├── users

└── auth_sessions
```

Future tables

```text
email_verifications

password_resets

oauth_accounts

devices

mfa_recovery_codes
```

---

# Security Model

Passwords

↓

bcrypt

↓

Database

----------------------------

Private RSA Key

↓

JWT Signing

↓

Access Token

↓

Public RSA Key

↓

Verification

Only Nativee Identity possesses the private key.

Every other service uses the public key.

---

# Deployment Architecture

```text
GitHub

↓

Railway Deployment

↓

Nativee Identity

↓

PostgreSQL
```

Independent deployment allows authentication to scale separately from business services.

---

# Design Principles

Nativee Identity follows these engineering principles.

- Single Responsibility
- Stateless Authentication
- RS256 Public-Key Cryptography
- Independent Deployment
- Independent Database
- Layered Architecture
- Repository Pattern
- Service Layer
- Dependency Injection

---

# Future Architecture

Planned capabilities include

- Email Verification
- Password Reset
- OAuth Providers
- Multi-Factor Authentication
- Passkeys
- WebAuthn
- Enterprise SSO
- Organizations
- Role-Based Access Control

---

# Relationship with Other Services

```text
                 Nativee Platform

          ┌──────────────────────┐
          │  Nativee Identity    │
          │ Authentication       │
          └──────────┬───────────┘
                     │
                RS256 JWT
                     │
      ┌──────────────┴──────────────┐
      ▼                             ▼
 Nativee API                 Nativee Engine
 Business Platform            AI Runtime
```

Identity authenticates users.

Nativee API manages business resources.

Nativee Engine executes AI workloads.

Each service owns its own domain and can evolve independently without affecting the others.