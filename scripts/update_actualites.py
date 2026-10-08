#!/usr/bin/env python3
"""Récupère l'actualité récente des mathématiques (flux RSS de Google Actualités)
et l'écrit dans _data/actualites_maths.json. En cas d'échec, l'ancien fichier est conservé."""
import json
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

REQUETE = '(mathématiques OR mathématicien OR "médaille Fields" OR "prix Abel") when:14d'
NB_ARTICLES = 6
SORTIE = Path(__file__).resolve().parent.parent / "_data" / "actualites_maths.json"


def recuperer():
    url = "https://news.google.com/rss/search?" + urllib.parse.urlencode(
        {"q": REQUETE, "hl": "fr", "gl": "FR", "ceid": "FR:fr"}
    )
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        racine = ET.fromstring(r.read())

    articles, titres_vus = [], set()
    for item in racine.iter("item"):
        titre = (item.findtext("title") or "").strip()
        lien = (item.findtext("link") or "").strip()
        source = (item.findtext("source") or "").strip()
        if source and titre.endswith(" - " + source):
            titre = titre[: -len(source) - 3].strip()
        if not titre or not lien or titre in titres_vus:
            continue
        titres_vus.add(titre)
        try:
            date = parsedate_to_datetime(item.findtext("pubDate")).astimezone(timezone.utc)
        except (TypeError, ValueError):
            date = datetime.now(timezone.utc)
        articles.append({"titre": titre, "lien": lien, "source": source, "date": date.isoformat()})

    articles.sort(key=lambda a: a["date"], reverse=True)
    return articles[:NB_ARTICLES]


def main():
    try:
        articles = recuperer()
    except Exception as e:  # réseau, XML invalide…
        print(f"Échec de la récupération : {e}", file=sys.stderr)
        return 1
    if not articles:
        print("Aucun article trouvé : fichier conservé.", file=sys.stderr)
        return 1
    SORTIE.write_text(
        json.dumps({"maj": datetime.now(timezone.utc).isoformat(), "articles": articles},
                   ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"{len(articles)} articles écrits dans {SORTIE}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
