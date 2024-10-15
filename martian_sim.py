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

new_para = soup.new_tag("paragraph", text="soup.head.append(new_para)

with open("index.html", "w") as outf:
    outf.write(str(soup))
