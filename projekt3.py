"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie

author: Matěj Adámek
email: matej.311@seznam.cz
discord: Addy#8986
"""

import pandas as pd
from bs4 import BeautifulSoup
import requests
import argparse

def get_municipality_name(url_municipality):
    raw_html = requests.get(url_municipality)
    soup = BeautifulSoup(raw_html.text, "html.parser")
    municipality = soup.find("div",{"class":"topline"})
    municipality2 = municipality.find_all("h3")[2].text
    municipality_list = list()
    municipality_list.append(municipality2[7:])
    municipality_list2 = list()
    for i in municipality_list:
        municipality_list2.append(i.replace("\n", ""))
    return municipality_list2


def get_municipality_urls(district_url):
    raw_html = requests.get(district_url)
    soup = BeautifulSoup(raw_html.text, "html.parser")
    url_result_set = soup.find_all(href=True)
    url_result_set = url_result_set[6:-2]
    url_result_set_list = list()
    for url in url_result_set:
        if url.text.isdigit():
            url_result_set_list.append(url["href"])
    return url_result_set_list

def get_nuts(district_url):
    raw_html = requests.get(district_url)
    soup = BeautifulSoup(raw_html.text, "html.parser")
    nuts_list = list()
    nuts = soup.find("div",{"class":"topline"})
    nuts2 = nuts.find_all("td",{"class":"cislo"})
    nuts3 = list()
    for i in nuts2:
        i = i.find("a")
        nuts3.append(i.text)
    return nuts3


def get_votes(url):
    raw_html = requests.get(url)
    soup = BeautifulSoup(raw_html.text,"html.parser")
    votes = list()
    for i in soup.find_all("td", headers = "t1sa2 t1sb3"):
        votes.append(i.text)
    for i in soup.find_all("td",headers="t2sa2 t2sb3"):
        if i.text == "-":
            continue
        votes.append(i.text)
    return votes


def get_parties(url_municipality):
    raw_html = requests.get(url_municipality)
    soup = BeautifulSoup(raw_html.text, "html.parser")
    parties = list()
    for i in soup.find_all("td", class_="overflow_name"):
        if i.text == "-":
            continue
        parties.append(i.text)
    return parties

def get_voters_envelopes_valid_votes(url_municipality):
    raw_html = requests.get(url_municipality)
    soup = BeautifulSoup(raw_html.text, "html.parser")
    get_voters_envelopes_valid_votes_list = list()
    registered = soup.find("td", headers="sa2").text
    envelopes = soup.find("td", headers="sa3").text
    valid = soup.find("td", headers="sa6").text
    get_voters_envelopes_valid_votes_list.append(registered)
    get_voters_envelopes_valid_votes_list.append(envelopes)
    get_voters_envelopes_valid_votes_list.append(valid)
    get_voters_envelopes_valid_votes_list = [symbol.replace(r"\xa0", " ") for symbol in get_voters_envelopes_valid_votes_list]
    return get_voters_envelopes_valid_votes_list

def main() -> list:
    try:
        while True:
            parser = argparse.ArgumentParser(description=
                                             "Vložte odkaz na vybraný okres a název csv souboru "
                                             "včetně přípony .csv")
            parser.add_argument('district_url', help="Vložte odkaz na vybraný okres obalený uvozovkami", type=str)
            parser.add_argument('title_csv', help="Vložte jméno csv souboru včetně přípony .csv", type=str)
            args = parser.parse_args()
            if args.district_url[0:52] == "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=" \
                    and args.title_csv[-4:] == ".csv":
                break
            else:
                print("Špatně zadaný odkaz nebo název csv souboru, zkuste vložení provést znovu")
                exit()

        district_url = args.district_url
        title_csv = args.title_csv

        url_municipality = f"https://volby.cz/pls/ps2017nss/{get_municipality_urls(district_url)[0]}"
        nuts = get_nuts(district_url)
        parties = get_parties(url_municipality)
        results = list()
        for url in get_municipality_urls(district_url):
            url_municipality = f"https://volby.cz/pls/ps2017nss/{url}"
            results2 = list()
            results2 = get_municipality_name(url_municipality) +\
                        get_voters_envelopes_valid_votes(url_municipality) + get_votes(url_municipality)
            results.append(results2)
        df = pd.DataFrame(results,columns=(["location", "registered", "envelopes", "valid"] + parties))
        df.insert(0,"code",nuts)
        df.to_csv(title_csv, index=False)
    except IndexError:
        print("Špatně zadaný odkaz, zkuste odkaz vložit znovu")

if __name__ == "__main__":
    main()





