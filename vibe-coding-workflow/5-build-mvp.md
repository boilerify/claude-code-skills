# Part V - Build with AI Agent

### 5️⃣ Build with AI Agent 💻

<details>
<summary><b>Let AI build your MVP</b> • 1-3 hrs • Creates working application</summary>

#### Setup by Tool Type

<details>
<summary><b>Terminal Agents (Claude Code, Gemini CLI)</b></summary>

```bash
# Claude Code
npm install -g @anthropic-ai/claude-code
cd your-project
claude init
# Add CLAUDE.md to project root
claude "Read CLAUDE.md and NOTES.md, then build the MVP"

# Gemini CLI
npm install -g @google-gemini/cli
gemini login
# Add GEMINI.md to project root
gemini "Read GEMINI.md and NOTES.md, then implement"
```

</details>

<details>
<summary><b>IDE Tools (Cursor, Windsurf)</b></summary>

1. Open your project folder in the IDE
2. Add configuration file:
   - Cursor: `.cursorrules` or `.cursor/rules.mdc`
   - Windsurf: `.windsurfrules`
3. Start with: _"Read NOTES.md and build the MVP step by step"_

</details>

<details>
<summary><b>No-Code Platforms (Bolt.new, Lovable)</b></summary>

1. Go to platform website
2. Paste your PRD content
3. Say: _"Build this MVP following the specifications"_
4. Deploy instantly with one click

</details>

#### Essential Prompts for Building

**Starting prompts by experience level:**
| Level | First Prompt |
|-------|--------------|
| **Beginner** | _"I'm new to coding. Read NOTES.md and guide me step-by-step to build this MVP. Explain what you're doing."_ |
| **Intermediate** | _"Read NOTES.md and the docs folder. Build the core features first, test, then add polish."_ |
| **Developer** | _"Review NOTES.md and architecture. Implement Phase 1 with proper patterns and test coverage."_ |

**Follow-up prompts for all levels:**

- _"Show me the current progress vs requirements"_
- _"Test [feature] and fix any issues"_
- _"Add error handling and edge cases"_
- _"Generate README with setup instructions"_
- _"Prepare for deployment to [platform]"_

</details>

---
