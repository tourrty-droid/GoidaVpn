#!/bin/bash
# Auto-update AutoMixConf every 15 minutes
# Run this with: chmod +x setup-workflow.sh && ./setup-workflow.sh

mkdir -p .github/workflows

cat > .github/workflows/auto-update-automixconf.yml << 'EOF'
name: Auto-update AutoMixConf

on:
  schedule:
    - cron: '*/15 * * * *'
  workflow_dispatch:

jobs:
  update-automixconf:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: pip install PyGithub
      - name: Update AutoMixConf
        run: python auto_mix_configs.py
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          GITHUB_USERNAME: tourrty-droid
          GITHUB_REPO: GoidaVpn
      - name: Commit and push if changed
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add -A
          git diff-index --quiet HEAD || git commit -m "auto: update AutoMixConf" && git push
EOF

echo "✅ Workflow создан! Закоммитьте изменения:"
echo "git add .github/workflows/auto-update-automixconf.yml"
echo "git commit -m 'ci: Add auto-update workflow'"
echo "git push"
