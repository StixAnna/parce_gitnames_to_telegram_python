# %%
import os
from dotenv import load_dotenv
import requests
import time
import pandas as pd

# %%
def parse_JSON(response_json: list) -> list:
    commiters_list = [commit['login'] for commit in response_json]
    return list(set(commiters_list))
# %%
def get_commiters(reposit: str, git_stoken) -> list:
    req_dtr =f"https://api.github.com/repos/{reposit}/contributors"
    headers = {
        'User-Agent': 'requests',
        "Accept": "application/vnd.github+json",
        'X-GitHub-Api-Version': '2022-11-28',
        'Authorization': f"{git_stoken}",    # гитхаб токен для авторизации
    }
    try:
        response = requests.get(req_dtr, headers=headers)
    except requests.exceptions.RequestException as e:
        print("Error occured: ", e)
        print("Couldn't get data from Git")
        return []
    else:
        if response.status_code != 200:
            print("Couldn't get data from GIT")
            print(f"Response code: {response.status_code}")
            if "Retry-After" in response.headers:
                     time.sleep(response.headers['Retry-After'])
            return []
        try:
            response_json = response.json()
        except:
            print("Couldn't convert response to JSON")
            return []
        else:
            try:
                commiters_list = parse_JSON(response_json)
            except Exception as e:
                print("Error occured: ", e)
                print("Couldn't parse")
                print(response_json)
            else:
                if "Retry-After" in response.headers:
                     time.sleep(response.headers['Retry-After'])
                return commiters_list

# %%
if __name__ == '__main__':
    rdfileName = "repositries_part_func.xlsx"
    filter = rdfileName.split(".")[0][-3:]
    reposit_list=pd.read_excel(rdfileName, 
                 index_col=None,dtype={'rep': str}
                 )["rep"].tolist()
    git_stoken = os.getenv('GIT_STOKEN')
    for reposit in reposit_list:
        print(f"++++++++++++++++++++++{reposit}+++++++++++++++++++++")        
        lt_write = get_commiters(reposit, git_stoken)
        with open(f"out_{filter}.csv", "a") as txt_file:
            # txt_file.write(f"{reposit}\n")
            txt_file.write(", ".join(lt_write) + "\n")
        time.sleep(30)
    print(f"++++++++++++++++++++++{reposit}endl+++++++++++++++++++++")        


