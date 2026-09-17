#!/usr/bin/env bash
# inno3d-claude-skills 설치/제거 스크립트
# 저장소의 각 스킬 폴더를 ~/.claude/skills/ 아래로 심볼릭 링크합니다.
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_DIR="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"
UNINSTALL=0
[[ "${1:-}" == "--uninstall" ]] && UNINSTALL=1

mkdir -p "$TARGET_DIR"

count=0
for skill_md in "$REPO_DIR"/*/SKILL.md; do
  [[ -e "$skill_md" ]] || continue
  src="$(dirname "$skill_md")"
  name="$(basename "$src")"
  dest="$TARGET_DIR/$name"

  if (( UNINSTALL )); then
    if [[ -L "$dest" && "$(readlink "$dest")" == "$src" ]]; then
      rm "$dest"
      echo "removed  $name"
      (( ++count ))
    fi
    continue
  fi

  if [[ -L "$dest" ]]; then
    ln -sfn "$src" "$dest"
    echo "relinked $name"
  elif [[ -e "$dest" ]]; then
    echo "SKIP     $name (심볼릭 링크가 아닌 파일/폴더가 이미 있음: $dest)" >&2
    continue
  else
    ln -s "$src" "$dest"
    echo "linked   $name"
  fi
  (( ++count ))
done

if (( UNINSTALL )); then
  echo "제거 완료: ${count}개"
else
  echo "설치 완료: ${count}개 → $TARGET_DIR"
  echo "Claude Code를 재시작하면 스킬이 인식됩니다."
fi
