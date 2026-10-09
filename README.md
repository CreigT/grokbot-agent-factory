# GrokBot Agent Factory

Paste an AI agent recipe. GrokBot finishes the gaps, builds the files, and pushes a public repo to GitHub.

Sponsored by Creignificent LLC. Owner: CreigT.

## How to run it

1. Copy `RECIPE.template.md`.
2. Fill what you know. Leave the rest blank.
3. Paste the recipe into Grok and say: **finish this recipe, build it, push it to GitHub**.
4. GrokBot returns the repo URL. You edit `config.js` only.

Optional local check before you paste:

```bash
python3 tools/check_recipe.py RECIPE.template.md
```

Open `index.html` in a browser for the same desk with no install.

## What GrokBot will do

- Mark missing fields instead of inventing a product.
- Fill safe defaults: public repo, static HTML, no paid APIs, no secrets in git.
- Build a short README, `config.js`, `index.html`, and `.env.example`.
- Create `https://github.com/CreigT/<agent-name>` and push one commit to `main`.
- Stop on attack, fraud, credential theft, or anything that needs a paid service to run.

## What you edit

`config.js` only. Do not put API keys in the repo.

## Deploy

Import the new repo on Vercel as Other. No build command. Output is the repo root.
