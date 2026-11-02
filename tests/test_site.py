"""Build the site and check the pages we agreed on."""

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_published_pages_match_the_agreed_site(tmp_path: Path) -> None:
    output = tmp_path / "output"
    subprocess.run(
        [
            "pelican",
            "content",
            "-o",
            str(output),
            "-s",
            "publishconf.py",
        ],
        cwd=ROOT,
        check=True,
    )

    home = (output / "index.html").read_text(encoding="utf-8")
    about = (output / "about.html").read_text(encoding="utf-8")
    podcast = (output / "podcast.html").read_text(encoding="utf-8")
    writing = (output / "writing.html").read_text(encoding="utf-8")
    article = (output / "containers-and-how-to-use-them.html").read_text(encoding="utf-8")

    assert "thoughts, hobbies, and other interests" in home
    assert "create an issue" not in home
    assert "Built with" not in home
    assert "Disqus" not in home
    assert "Archives" not in home
    assert not (output / "archives.html").exists()

    assert "https://alpaca.markets/" in about
    assert "https://www.firstcircle.ph/" in about
    assert "https://www.ateneo.edu/" in about
    assert "Alpaca Markets" in about
    assert "Ateneo de Manila University" in about
    assert 'id="theme"' in about
    assert "create an issue" not in about
    assert "Built with" not in about

    assert "Data Dunce-02.jpg" in podcast
    assert "https://open.spotify.com/show/3sq29pUzAEdEywYJtJrx4Z" in podcast
    assert "https://podcasts.apple.com/us/podcast/data-dunce/id1556366523" in podcast

    assert "Containers and how to use them" in writing
    assert "My journey into data" in writing

    assert "It worked on my machine" in article
    assert "vm_vs_docker.png" in article

    for page in (home, about, writing, article):
        assert "google-analytics.com" not in page
        assert "analytics.js" not in page
        assert 'property="og:image" content="https://www.kemppo.com/images/profile.jpg"' in page
        assert 'name="twitter:card" content="summary_large_image"' in page
        assert 'href="https://www.kemppo.com/feeds/all.atom.xml"' in page

    assert 'property="og:title" content="Kemp Po"' in home
    assert "thoughts, hobbies, and other interests" in home
    assert 'property="og:title" content="Containers and how to use them · Kemp Po"' in article
    assert (output / "feeds" / "all.atom.xml").is_file()

    sitemap = (output / "sitemap.xml").read_text(encoding="utf-8")
    for loc in (
        "https://www.kemppo.com/",
        "https://www.kemppo.com/writing.html",
        "https://www.kemppo.com/about.html",
        "https://www.kemppo.com/podcast.html",
        "https://www.kemppo.com/containers-and-how-to-use-them.html",
        "https://www.kemppo.com/my-journey-data.html",
    ):
        assert loc in sitemap
    assert "archives.html" not in sitemap

    robots = (output / "robots.txt").read_text(encoding="utf-8")
    assert "Sitemap: https://www.kemppo.com/sitemap.xml" in robots
