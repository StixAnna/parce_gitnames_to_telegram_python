# %%
import requests
from bs4 import BeautifulSoup
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# %%
def get_html(url):
    r = requests.get(url)
    return r.text
# %%
def Take_rep_list(texttofind, rep_list):
    for i in range(1, 101):
      html = get_html(f"https://github.com/search?q={texttofind}&type=repositories&p={i}")
      soup1 = BeautifulSoup(html, 'lxml')
      rep_list += [i.split('"')[-2] for i in soup1.find('p').text.split(',') if 'hl_name' in i]
    return rep_list

# %%
rep_list = []
texttofind = 'ton'
rep_list = Take_rep_list(texttofind, rep_list)

# %%
len(rep_list)

# %%
pd.DataFrame({'rep': rep_list}).to_excel(f"repositries_{texttofind}.xlsx", index=False)

# %%
rep_list = []
texttofind = 'func'
rep_list = Take_rep_list(texttofind, rep_list)

# %%
len(rep_list)

# %%
pd.DataFrame({'rep': rep_list}).to_excel(f"repositries_{texttofind}.xlsx", index=False)

# %%
rep_list = []
texttofind = 'fift'
rep_list = Take_rep_list(texttofind, rep_list)

# %%
pd.DataFrame({'rep': rep_list}).to_excel(f"repositries_{texttofind}.xlsx", index=False)


