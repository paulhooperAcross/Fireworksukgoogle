#!/bin/bash
set -e
BASE="$HOME/.openclaw/workspace/projects/fireworks-night-uk"
PAGES="$BASE/site/pages"
INDEX="$BASE/site/content-index.json"

next=$(python3 - <<PY
import json
p=json.load(open("$INDEX"))['pages']
planned=[(k,v.get('priority',999)) for k,v in p.items() if v.get('status')=='planned']
planned=sorted(planned,key=lambda x:x[1])
print(planned[0][0] if planned else "")
PY
)

[ -z "$next" ] && echo "No planned pages" && exit 0

file="$PAGES/$next.md"
[ -f "$file" ] && echo "Exists $file" && exit 0

title=$(echo "$next" | sed 's/-/ /g' | sed 's/\b\w/\U&/g')

cat > "$file" <<EOF
# $title

Guide to $title.

## Overview
Bonfire Night fireworks events across the UK attract thousands of visitors every year.

## What Happens
Community displays, professional fireworks, food stalls and family entertainment.

## Tips
- Arrive early
- Dress warmly
- Check event safety guidance

---
Draft page for Fireworks Night UK.
EOF

python3 - <<PY
import json
p=json.load(open("$INDEX"))
p['pages']["$next"]['status']='draft'
json.dump(p,open("$INDEX","w"),indent=2)
PY

echo "Generated $next"
