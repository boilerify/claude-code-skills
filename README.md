# Claude Code Skills

A comprehensive collection of specialized skills that extend Claude's capabilities for modern software development workflows.

## Overview

This repository contains modular, self-contained skills that transform Claude from a general-purpose agent into a specialized expert equipped with procedural knowledge, workflows, and tool integrations for specific domains and tasks.

## Available Skills

### 📚 Documentation Generator

**Purpose:** Generate comprehensive documentation from code, create README files, API documentation, and technical specifications.

**When to use:**

- Generating project documentation and README files
- Creating API documentation from code comments
- Writing technical specifications and architecture documentation

**Features:**

- Auto-generated READMEs from project structure
- API documentation extraction from route handlers and endpoints
- Code documentation from function comments and docstrings

### Next.js

**Purpose:** Comprehensive Next.js v15+ skill for building modern web applications using the App Router, React Server Components, SSR/SSG/ISR data fetching, API routes, metadata/SEO, and TypeScript.

**When to use:**

- Scaffolding, building, or maintaining Next.js applications
- Implementing App Router patterns and server components
- Building SEO-optimized applications with modern React patterns

**Features:**

- Server Components for zero-bundle size
- File-system based routing with layouts
- Built-in API endpoints with route handlers
- Automatic image optimization with `next/image`

### ️ Skill Creator

**Purpose:** Guide for creating effective skills that extend Claude's capabilities with specialized knowledge, workflows, or tool integrations.

### 👨‍💻 Frontend Developer

**Purpose:** Frontend development specialist for React applications and responsive design.

**When to use:**

- Building UI components and React applications
- Implementing state management and performance optimization
- Creating accessible and responsive web interfaces

## Project Structure

```
.claude/
├── agents/
│    └── frontend-developer.md
├── scripts/
│    └── validate-bash.sh
├── settings.local.json
└── skills/
    ├── documentation-generator/
    │   ├── SKILL.md
    │   ├── references/
    │   │    └── documentation_standards.md
     └── scripts/
        ├── extract_api_docs.py
         └── generate_readme.py
    ├── nextjs/
    │    └── SKILL.md
     └── skill-creator/
        ├── SKILL.md
        ├── LICENSE.txt
         └── scripts/
            ├── init_skill.py
            ├── package_skill.py
             └── quick_validate.py
```

## Quick Start

### Using Documentation Generator

```bash
# Generate README from project structure
python .claude/skills/documentation-generator/scripts/generate_readme.py --project-path . --output README.md
```

### Creating a New Skill

```bash
# Initialize a new skill
python .claude/skills/skill-creator/scripts/init_skill.py <skill-name> --path .claude/skills/
```

## Skill Architecture

Each skill follows a standardized structure:

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter metadata (name, description)
│    └── Markdown instructions
└── Bundled Resources (optional)
    ├── scripts/          - Executable code (Python/Bash/etc.)
├── references/       - Documentation for context
└── assets/           - Files used in output
```

### Progressive Disclosure Design

Skills use a three-level loading system for efficient context management:

1. **Metadata** - Always in context (~100 words)
2. **SKILL.md body** - When skill triggers (<5k words)
3. **Bundled resources** - As needed by Claude

## Usage Examples

### Generate Project Documentation

```
Generate a comprehensive README for this project
```

### Create Next.js Application

```
Scaffold a new Next.js application with authentication
```

### Build Frontend Components

```
Create a responsive dashboard layout with React components
```

## Development

### Skill Creation Process

1. **Understand** - Analyze concrete usage examples
2. **Plan** - Identify reusable resources (scripts, references, assets)
3. **Initialize** - Run `init_skill.py` to create template
4. **Edit** - Customize SKILL.md and bundled resources
5. **Package** - Create distributable zip file
6. **Iterate** - Test and improve based on real usage

### Validation and Packaging

```bash
# Validate a skill
python .claude/skills/skill-creator/scripts/quick_validate.py <skill-path>
```

## Requirements

- Python 3.8+
- Node.js 20+ (for Next.js development)
- Modern package manager (npm, pnpm, or yarn)

## Contributing

To contribute a new skill:

1. Use the Skill Creator skill to initialize a new skill
2. Follow the progressive disclosure design principle
3. Include proper YAML frontmatter with name and description
4. Package using the packaging script

## License

See individual skill directories for specific licensing information.

## Version History

- **v1.0.0** (2025-11-03): Initial release with core skills

## Related Resources

- [Claude Documentation](https://docs.anthropic.com/)
- [Next.js Official Docs](https://nextjs.org/docs)
- [React Documentation](https://react.dev/)
