# %%
import pandas as pd
def get_compares(git_allusers, falltgramusers):
    git_allusers_tocheck = list(set(git_allusers))
    sovpad=[]
    #print(sorted(git_allusers_tocheck))
    for gituser in git_allusers_tocheck:
        if gituser.lower() in falltgramusers:
           sovpad.append(gituser.lower())
    return sovpad

# %%

rdfileName = "out_users.csv"
alltgramusers = []
with open(rdfileName, 'r') as file:
    file_data = file.read()
    alltgramusers = file_data.split(', ')
    print(len(set(alltgramusers)))

# %%

xls = 'Dorahacks_Hackers.xlsx'
hackers_list = pd.read_excel(xls, 
                 index_col=None,dtype={'name 2 ': str}
                 )["name 2 "].tolist()
print(len(set(hackers_list)))

# %%

sovpad2 = []
for filename in ["out_fif.csv", "out_unc.csv", "out_ton.csv"]:
  print(f"processing for {filename}")
  buff_total = []
  with open(filename, 'r') as file:
      # Читаем файл построчно
      for line in file:
          buff = line.strip().lower().split(", ")
          buff_total.extend(buff)
  print(get_compares(buff_total, alltgramusers))
  print(len(set(buff_total)))
  
print(f"processing for Dorahacks_Hackers")
for hacker in hackers_list:
    if hacker.lower() in alltgramusers:
      sovpad2.append(hacker.lower())
print(sovpad2)

# %%
'acadabus' == 'acadabus'
# %%
