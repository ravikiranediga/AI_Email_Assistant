from collections import Counter

from database.db import get_all_emails


def get_dashboard_stats():

    emails = get_all_emails()

    total_emails = len(emails)

    tones = [row[2] for row in emails]

    tone_counts = dict(
        Counter(tones)
    )

    most_used_tone = "N/A"

    if tone_counts:

        most_used_tone = max(
            tone_counts,
            key=tone_counts.get
        )

    return {
        "total_emails": total_emails,
        "tone_counts": tone_counts,
        "most_used_tone": most_used_tone,
        "recent_emails": emails[:5]
    }