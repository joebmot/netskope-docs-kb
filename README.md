# netskope-docs-kb

Automated daily scrape of [docs.netskope.com](https://docs.netskope.com/en) into a structured GitHub knowledge base for Claude RFP automation and research.

## Structure

```
data/
├── index.json        ← master page index
├── changelog.md      ← what changed in last run
└── topics/           ← one .md file per product
    ├── ztna.md
    ├── casb.md
    ├── dlp.md
    └── ...
```

## Claude Access URLs

```
https://raw.githubusercontent.com/joebmot/netskope-docs-kb/main/data/index.json
https://raw.githubusercontent.com/joebmot/netskope-docs-kb/main/data/changelog.md
https://raw.githubusercontent.com/joebmot/netskope-docs-kb/main/data/topics/ztna.md
```

## Schedule

Runs daily at **6:00 AM UTC** via GitHub Actions. Trigger manually: Actions → Daily Netskope Docs Scrape → Run workflow.
