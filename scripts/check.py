#!/usr/bin/env python3
"""Checks every Markdown file in the repo before it is published.

Report only: it never rewrites a file. Exit code 1 on any finding.

- No em or en dashes (house style: commas, colons, full stops, "to" for ranges).
- No invisible characters (zero-width, joiners, BOM, soft hyphen, direction marks, tag chars).
- No phrase from the banned list (client names, internal codenames, figures that were
  corrected, places that are not for publication).
- Every relative link and heading fragment resolves.
- Every case file carries the seven sections the README promises, in order.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
MD = sorted(p for p in ROOT.glob('*.md'))
CASES = [p for p in MD if re.match(r'\d\d-', p.name)]

DASHES = {'—': 'em dash', '–': 'en dash'}
INVISIBLE = {
    '​': 'zero-width space', '‌': 'zero-width non-joiner', '‍': 'zero-width joiner',
    '⁠': 'word joiner', '﻿': 'byte-order mark', '­': 'soft hyphen',
    '‎': 'left-to-right mark', '‏': 'right-to-left mark', '‪': 'LRE', '‫': 'RLE',
    '‬': 'PDF', '‭': 'LRO', '‮': 'RLO', '⁦': 'LRI', '⁧': 'RLI',
    '⁨': 'FSI', '⁩': 'PDI',
}
BANNED = [
    # client names never appear beside a figure, or anywhere in this repo
    'chainalysis', 'elliptic', 'crystal blockchain', 'merkle science', 'trm labs', 'podproza',
    # internal codenames and places that stay off the public record
    r'\brex\b', 'revion', 'buntogole', 'twende', 'opsuma', 'lisbon',
    # figures that were corrected and must not come back
    r'£3\s?m', 'around £3', '800 misroutes', '40 in production',
]
SECTIONS = ['## Context', '## The problem', '## What I did', '## Result',
            '## Also in this role', '## Evidence and limits']

findings = []


def note(path, msg):
    findings.append(f'{path.name}: {msg}')


for path in MD:
    text = path.read_text(encoding='utf-8')
    for ch, name in DASHES.items():
        for m in re.finditer(re.escape(ch), text):
            line = text.count('\n', 0, m.start()) + 1
            note(path, f'{name} on line {line}')
    for ch, name in INVISIBLE.items():
        if ch in text:
            note(path, f'invisible character: {name}')
    for c in text:
        if 0xE0000 <= ord(c) <= 0xE007F:
            note(path, 'invisible character: Unicode tag character')
            break
    low = text.lower()
    for pat in BANNED:
        if re.search(pat, low):
            note(path, f'banned phrase: {pat}')
    for m in re.finditer(r'\]\(([^)]+)\)', text):
        target = m.group(1).strip()
        if target.startswith(('http://', 'https://', 'mailto:')):
            continue
        file_part, _, frag = target.partition('#')
        dest = path if not file_part else (path.parent / file_part)
        if not dest.exists():
            note(path, f'link to missing file: {target}')
            continue
        if frag:
            heads = re.findall(r'^#+\s+(.+)$', dest.read_text(encoding='utf-8'), re.M)
            slugs = {re.sub(r'[^a-z0-9 -]', '', h.lower()).strip().replace(' ', '-') for h in heads}
            if frag not in slugs:
                note(path, f'link to missing heading: {target}')

for path in CASES:
    text = path.read_text(encoding='utf-8')
    positions = [text.find(s + '\n') for s in SECTIONS]
    missing = [s for s, p in zip(SECTIONS, positions) if p < 0]
    if missing:
        note(path, 'missing section(s): ' + ', '.join(missing))
    elif positions != sorted(positions):
        note(path, 'sections out of order')
    if not text.startswith('# ' + path.name[:2] + '. '):
        note(path, 'title does not start with the case number')
    if '**Where.**' not in text:
        note(path, 'no "Where." line under the title')

if findings:
    print('\n'.join(findings))
    print(f'{len(findings)} finding(s)')
    sys.exit(1)
print(f'all checks passed ({len(MD)} files, {len(CASES)} cases)')
