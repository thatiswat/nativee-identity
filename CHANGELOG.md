# 📦 Changelog

All notable changes to Nativee Identity will be documented in this file.

This project follows Semantic Versioning.

---

# v1.0.0 — Nativee Identity Platform

Released: July 2026

> Initial production release of the Nativee Identity service.

This release introduces centralized authentication for the Nativee Platform and establishes Identity as an independent backend service.

---

## 🚀 Added

### Authentication

- User Registration
- User Login
- Logout
- Current User Endpoint
- Refresh Token Authentication
- Session Management

---

### JWT Infrastructure

- RS256 Authentication
- RSA Public / Private Key Support
- Access Tokens
- Refresh Tokens
- JWT Claims
- Issuer Validation
- Audience Validation
- Token Expiration

---

### Security

- Password Hashing (bcrypt)
- Session Tracking
- Refresh Token Rotation
- Identity Claims
- Public User IDs

---

### Database

- PostgreSQL
- SQLAlchemy ORM
- Alembic Migrations

Current Tables

- users
- auth_sessions

---

### Architecture

- Repository Pattern
- Service Layer
- Dependency Injection
- Layered Architecture
- Independent Identity Database

---

### Platform

- Nativee API Integration
- RS256 JWT Verification
- Railway Deployment
- OpenAPI Documentation

---

## 🏗 Architecture

Nativee Identity became the central authentication authority.

```
                Mobile
                   │
                Web App
                   │
                   ▼
          Nativee Identity
                   │
              RS256 JWT
                   │
          ┌────────┴────────┐
          ▼                 ▼
     Nativee API      Nativee Engine
```

---

## 🔄 Breaking Changes

Initial production release.

---

## 📈 Engineering Improvements

- Centralized Authentication
- Independent Deployment
- Independent Database
- Stateless JWT Authentication
- Service-Oriented Architecture

---

## 🚧 Next Milestones

- Automatic Business User Provisioning
- Email Verification
- Password Reset
- OAuth Providers
- Multi-Factor Authentication
- Organizations
- RBAC
- Enterprise Identity

---

# Future Releases

## v1.1

- Email Verification
- Password Reset
- Identity Synchronization

---

## v1.2

- Google OAuth
- GitHub OAuth
- Microsoft OAuth

---

## v1.3

- Organizations
- Roles
- Permissions
- RBAC

---

## v2.0

- Multi-Factor Authentication
- Passkeys
- WebAuthn
- Enterprise SSO
- Audit Logs