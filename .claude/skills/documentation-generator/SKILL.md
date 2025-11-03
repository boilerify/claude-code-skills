---
name: documentation-generator
description: Generate comprehensive documentation from code, create README files, API documentation, and technical specifications. Use when generating documentation, creating READMEs, writing API docs, or documenting codebases.
---

# Documentation Generator

A comprehensive skill for generating various types of documentation from codebases, APIs, and technical specifications.

## Quick Start

### Generate README from project structure

```bash
# Analyze project structure and generate README
python scripts/generate_readme.py --project-path . --output README.md
```

### Create API Documentation

```bash
# Generate API docs from code comments
python scripts/extract_api_docs.py --source-dir src --output docs/api.md
```

## Documentation Types

### 1. README Generation

- Project overview and setup instructions
- Installation and usage guides
- Configuration options and examples

### 2. API Documentation

- REST API endpoints with examples
- GraphQL schema documentation
- WebSocket API documentation

### 3. Code Documentation

- Function and class documentation
- Module-level documentation
- Architecture documentation

### 3. Technical Specifications

- System architecture diagrams
- Database schema documentation
- API endpoint specifications

## Usage Examples

### Generate Project Documentation

```
Generate a comprehensive README for this project
```

### Create API Reference

```
Document all API endpoints in this codebase
```

### Generate Technical Specs

```
Create technical documentation for this application
```

## Templates

### README Template Structure

````markdown
# Project Name

## Overview

Brief description of the project and its purpose.

## Features

- **Auto-generated READMEs**: From project structure and package.json
- **API Documentation**: From route handlers and API endpoints
- **Code Documentation**: From function comments and docstrings

## Best Practices

### Documentation Standards

- Use consistent formatting and structure
- Include code examples for all major features
- Provide installation and setup instructions
- Document configuration options
- Include troubleshooting guides

## Scripts

### `scripts/generate_readme.py`

Analyzes project structure and generates comprehensive README files.

### `scripts/extract_api_docs.py`

Extracts API documentation from code comments and annotations.

## Requirements

### Python Packages

```bash
pip install markdown pygments
```
````

## Related Skills

- **Code Reviewer** - Analyze code quality and best practices
- **API Developer** - Build and test REST APIs
- **Database Manager** - Document database schemas and queries

## Version History

- v1.0.0 (2025-11-03): Initial release
