from datetime import datetime


def generate_rss(audio_url, title="My Podcast", description="Auto-generated podcast"):
    now = datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")
    rss = f"""
    <rss version="2.0">
      <channel>
        <title>{title}</title>
        <link>{audio_url}</link>
        <description>{description}</description>
        <item>
          <title>{title} - Episode 1</title>
          <enclosure url="{audio_url}" type="audio/mpeg"/>
          <pubDate>{now}</pubDate>
          <guid>{audio_url}</guid>
        </item>
      </channel>
    </rss>
    """
    with open("podcast_feed.xml", "w") as file:
        file.write(rss.strip())
