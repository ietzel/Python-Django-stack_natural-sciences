import bs4

#"Driver"
#"Flier"
#"Slitherer"
#"Hopper"
#"Crawler"
#"Runner"

with open("index.html") as inf:
    txt = inf.read()
    soup = bs4.BeautifulSoup(txt)

new_para = soup.new_tag("paragraph", text="Driver, Flier, Slitherer, Hopper, Crawler, and Runner meet up for the cave exploration mission. The first one drives the other 5 to the cavity, and hoists them down. They find traces of water, and a big place for settlement. Findings reported...")
soup.head.append(new_para)

with open("index.html", "w") as outf:
    outf.write(str(soup))
