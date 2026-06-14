# 🔒 SAST Demo: Python Security Analysis

[![Security](https://img.shields.io/badge/Focus-Application%20Security-red?style=flat-square)](https://github.com/sairam-bathini/sast-demo-python)
[![Language](https://img.shields.io/badge/Language-Python-blue?style=flat-square)](https://www.python.org/)
[![Tool](https://img.shields.io/badge/Tool-SonarQube-brightgreen?style=flat-square)](https://www.sonarqube.org/)

## 📋 Problem Statement

Modern applications contain security vulnerabilities that go undetected during development. SAST (Static Application Security Testing) tools identify vulnerabilities early in the SDLC without requiring running code. This project demonstrates how to leverage SonarQube to detect and analyze Python code vulnerabilities.

## 🎯 What It Does

This repository provides:
- **Intentionally vulnerable Python code** with common security flaws
- **SonarQube integration** for static code analysis
- **Security findings demonstration** showing real vulnerabilities
- **Best practices guide** for secure Python development
- **CI/CD integration examples** for automated security scanning

### Key Vulnerabilities Detected:
- ✅ SQL Injection vulnerabilities
- ✅ Cross-Site Scripting (XSS) flaws
- ✅ Hardcoded credentials and secrets
- ✅ Path traversal issues
- ✅ Command injection risks
- ✅ Weak cryptography usage
- ✅ Insecure deserialization
- ✅ Input validation failures

## 🛠️ Tech Stack

| Component | Purpose |
|-----------|---------|
| **Python 3.8+** | Application language |
| **SonarQube** | Static code analysis & security scanning |
| **Docker** | Containerized deployment |
| **Pytest** | Unit testing framework |
| **Bandit** | Python-specific security linting |
| **Flask** | Web framework (if applicable) |

## 🚀 How to Run

### Option 1: Local Setup

```bash
# 1. Clone repository
git clone https://github.com/sairam-bathini/sast-demo-python.git
cd sast-demo-python

# 2. Install dependencies
pip install -r requirements.txt
pip install bandit pytest

# 3. Run Bandit SAST scan
bandit -r . -f json -o bandit-report.json

# 4. View findings
python view_findings.py

# 5. Run unit tests
pytest tests/ -v
```

### Option 2: Docker + SonarQube

```bash
# 1. Start SonarQube container
docker run -d --name sonarqube -p 9000:9000 sonarqube:latest

# 2. Wait for startup (2-3 minutes)
sleep 60

# 3. Create project and get token from http://localhost:9000

# 4. Run SonarScanner
docker run --rm \
  -e SONAR_HOST_URL=http://sonarqube:9000 \
  -e SONAR_LOGIN=your_token \
  -v $PWD:/usr/src/python-app \
  sonarsource/sonar-scanner-cli

# 5. View results at http://localhost:9000
```

### Option 3: GitHub Actions

```yaml
# .github/workflows/sast.yml
name: SAST Security Scan
on: [push, pull_request]
jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run Bandit
        run: |
          pip install bandit
          bandit -r . -f json -o bandit-report.json
      - name: Upload findings
        uses: actions/upload-artifact@v2
        with:
          name: security-report
          path: bandit-report.json
```

## 📊 Sample Findings

### Critical Issue Example: SQL Injection

```python
# ❌ VULNERABLE CODE
@app.route('/user/<user_id>')
def get_user(user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"  # Direct concatenation
    return execute_query(query)

# ✅ SECURE CODE
@app.route('/user/<user_id>')
def get_user(user_id):
    query = "SELECT * FROM users WHERE id = %s"  # Parameterized query
    return execute_query(query, (user_id,))
```

**Impact:** Attacker can extract/modify database contents  
**CVSS Score:** 9.8 (Critical)  
**Remediation:** Use parameterized queries and ORM frameworks

### High Issue Example: Hardcoded Credentials

```python
# ❌ VULNERABLE
database_url = "postgresql://admin:P@ssw0rd123@localhost/mydb"

# ✅ SECURE
database_url = os.getenv('DATABASE_URL', 'postgresql://localhost/mydb')
```

**Impact:** Exposure of database credentials  
**CVSS Score:** 7.5 (High)  
**Remediation:** Use environment variables and secrets management

## 📈 Security Dashboard

```
SonarQube Metrics:
┌─────────────────────────────────────┐
│ Lines of Code:        1,250          │
│ Bugs:                 8              │
│ Vulnerabilities:      12             │
│ Code Smells:          25             │
│ Duplications:         3.2%           │
│ Security Hotspots:    5              │
│ Coverage:             65%            │
│ Grade:                D (Poor)       │
└─────────────────────────────────────┘
```

## 🔐 Security Impact

| Vulnerability Type | Count | CVSS Avg | Business Impact |
|-------------------|-------|----------|-----------------|
| SQL Injection | 3 | 9.8 | Data breach, regulatory fines |
| XSS (Reflected) | 2 | 6.1 | Account takeover, malware |
| Hardcoded Secrets | 2 | 7.5 | Unauthorized access |
| Weak Crypto | 1 | 7.2 | Encryption bypass |
| Command Injection | 1 | 8.8 | Remote code execution |
| Path Traversal | 2 | 5.3 | Unauthorized file access |
| Input Validation | 1 | 6.5 | Application crash, DoS |

### Security Remediation Priority:

🔴 **CRITICAL** (Fix within 24 hours)
- SQL Injection, Command Injection, RCE

🟠 **HIGH** (Fix within 1 week)
- Hardcoded secrets, Weak authentication

🟡 **MEDIUM** (Fix within 1 month)
- Input validation, Weak encryption

🟢 **LOW** (Fix within release cycle)
- Code quality, Documentation

## 📚 Learning Resources

- [OWASP Top 10 2021](https://owasp.org/www-project-top-ten/)
- [SonarQube Python Rules](https://rules.sonarsource.com/python)
- [Bandit Documentation](https://bandit.readthedocs.io/)
- [OWASP Secure Coding Practices](https://cheatsheetseries.owasp.org/)

## 🏆 Best Practices Applied

✅ Parameterized SQL queries  
✅ Input validation and sanitization  
✅ Secure cryptographic functions  
✅ Secrets management  
✅ Error handling without info disclosure  
✅ Security headers implementation  
✅ Dependency vulnerability scanning  
✅ Secure deserialization  
✅ Rate limiting and DoS protection  
✅ Security logging  

## 🤝 Contributing

Found a vulnerability or improvement? [Submit an issue](https://github.com/sairam-bathini/sast-demo-python/issues)

## 📞 Support

- **Questions?** Create an [issue](https://github.com/sairam-bathini/sast-demo-python/issues)
- **Security Concern?** Email responsibly
- **Feedback?** Discussions are welcome

## 📄 License

MIT License - Educational purposes only

---

**Last Updated:** 2026-06-14 | **Maintained by:** [@sairam-bathini](https://github.com/sairam-bathini)
