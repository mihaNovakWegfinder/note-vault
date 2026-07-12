#!/usr/bin/env python3
"""Creates a daily note markdown file for the current date."""

from datetime import date, timedelta
import os


def create_daily_note() -> str:
    target_date = date.today()

    yesterday = target_date - timedelta(days=1)
    tomorrow = target_date + timedelta(days=1)

    filename = f"{target_date.strftime('%Y-%m-%d')}.md"

    if os.path.exists(filename):
        print(f"Note already exists: {filename}")
        return filename

    content = f"""# {target_date.strftime('%A, %B %d %Y')}

## 🎯 Currently Working On
-

## 📋 Yesterday ({yesterday.strftime('%A, %B %d')})
-

## 🚀 Tomorrow ({tomorrow.strftime('%A, %B %d')})
-
-

## 💡 Notes & Ideas
-

## ✅ Accomplishments
-
        """

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Created: {filename}")
    return filename


if __name__ == "__main__":
    create_daily_note()
