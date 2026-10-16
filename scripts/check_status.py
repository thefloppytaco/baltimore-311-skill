#!/usr/bin/env python3
"""Check Baltimore City 311 request status via the city's public ArcGIS feed.

Usage: check_status.py <SR-number> [<SR-number> ...]
Example: check_status.py 26-00965493

No API key or login needed. The feed refreshes daily, so a request filed
today usually appears tomorrow.
"""
import datetime
import json
import sys
import urllib.parse
import urllib.request

BASE = ("https://services1.arcgis.com/UWYHeuuJISiGmgXx/arcgis/rest/services/"
        "311_Customer_Service_Requests_current/FeatureServer/0/query")
FIELDS = ("ServiceRequestNum,SRType,SRStatus,CreatedDate,StatusDate,DueDate,"
          "CloseDate,Agency,LastActivity,Outcome,Address,ZipCode")


def norm(sr):
    s = sr.strip().upper().replace(" ", "")
    if len(s) == 10 and s[:2].isdigit() and s[2] != "-":
        s = s[:2] + "-" + s[2:]
    return s


def fetch(sr):
    params = {"where": "ServiceRequestNum='%s'" % sr,
              "outFields": FIELDS, "f": "json"}
    url = BASE + "?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url, timeout=30) as resp:
        data = json.load(resp)
    feats = data.get("features") or []
    return feats[0]["attributes"] if feats else None


def fmt(ms):
    if not ms:
        return "-"
    return datetime.datetime.fromtimestamp(ms / 1000).strftime("%b %d, %Y")


def main():
    if len(sys.argv) < 2:
        print("usage: check_status.py <SR-number> [<SR-number> ...]",
              file=sys.stderr)
        return 2
    for raw in sys.argv[1:]:
        sr = norm(raw)
        try:
            a = fetch(sr)
        except Exception as exc:  # noqa: BLE001 - report, don't crash
            print("%s: ERROR %s" % (sr, exc))
            continue
        if not a:
            print("%s: not in the public feed yet (it updates daily)" % sr)
            continue
        print("%s | %s | %s" % (a["ServiceRequestNum"], a["SRStatus"],
                                a["SRType"]))
        print("  Address: %s %s" % (a["Address"], a["ZipCode"] or ""))
        print("  Agency: %s | Filed: %s | Due: %s"
              % ((a["Agency"] or "").strip(), fmt(a["CreatedDate"]),
                 fmt(a["DueDate"])))
        if a.get("LastActivity"):
            print("  Last activity: %s" % a["LastActivity"])
        if a.get("Outcome"):
            print("  Outcome: %s" % a["Outcome"])
        if a.get("CloseDate"):
            print("  Closed: %s" % fmt(a["CloseDate"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
