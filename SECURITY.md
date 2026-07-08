# 🔒 Security Policy

Thank you for helping keep Nativee secure.

The security of our users, developers, and platform is our highest priority. We appreciate responsible disclosure of any vulnerabilities you discover.

---

# Supported Versions

The following versions currently receive security updates.

| Version | Supported |
|----------|-----------|
| 1.x | ✅ |
| < 1.0 | ❌ |

---

# Reporting a Vulnerability

If you believe you have discovered a security vulnerability, **please do not create a public GitHub issue.**

Instead, report it privately.

Email

```
security@nativee.in
```

Please include:

- Description of the vulnerability
- Steps to reproduce
- Affected endpoint(s)
- Expected behavior
- Actual behavior
- Proof of Concept (if available)
- Potential impact

We will acknowledge your report as quickly as possible and work with you to validate and resolve the issue.

---

# Response Process

After receiving a report, we follow the process below.

### 1. Acknowledgement

We aim to acknowledge reports within **72 hours**.

---

### 2. Investigation

Our engineering team will

- Verify the issue
- Assess impact
- Determine severity
- Develop a remediation plan

---

### 3. Resolution

If confirmed, we will

- Develop a fix
- Test internally
- Deploy security updates
- Publish release notes when appropriate

---

# Scope

This security policy applies to all Nativee services including

- Nativee Identity
- Nativee API
- Nativee Engine
- Nativee Web
- Nativee Mobile

---

# Authentication Security

Nativee Identity implements multiple security controls.

## Password Security

- bcrypt password hashing
- Passwords are never stored in plain text
- Password verification occurs only within Nativee Identity

---

## JWT Security

- RS256 asymmetric signing
- RSA Public / Private Keys
- Issuer validation
- Audience validation
- Token expiration
- Refresh token rotation

Only Nativee Identity possesses the private signing key.

Other platform services verify tokens using the public key.

---

## Session Security

- Refresh token sessions
- Session expiration
- Session revocation
- Device session tracking (planned)

---

# Responsible Disclosure

Please allow us reasonable time to investigate and resolve reported vulnerabilities before publicly disclosing them.

Coordinated disclosure helps protect our users and developers.

---

# Out of Scope

The following are generally considered out of scope unless they demonstrate a meaningful security impact.

- Missing security headers
- Version disclosure
- Self-XSS
- Clickjacking without exploitability
- Social engineering
- Denial-of-Service testing
- Brute-force testing
- Automated vulnerability scanner output without proof of exploitability

---

# Best Practices for Contributors

Contributors should

- Never commit secrets or credentials
- Never commit private RSA keys
- Never commit `.env` files
- Keep dependencies updated
- Follow secure coding practices
- Validate all user input
- Use parameterized database queries
- Follow the Principle of Least Privilege

---

# Security Roadmap

Future security improvements include

- Email Verification
- Password Reset
- Google OAuth
- GitHub OAuth
- Multi-Factor Authentication (MFA)
- Passkeys
- WebAuthn
- Enterprise SSO
- Device Trust
- Audit Logs
- Security Event Monitoring

---

# Contact

For security-related questions or vulnerability reports:

```
security@nativee.in
```

---

Thank you for helping keep the Nativee Platform secure.