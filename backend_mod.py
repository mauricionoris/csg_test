import pickle as pk 
from  intr_github import call_github_api

GITHUB_PERSISTED_FILE = './data/github_users.pickle'

#g_github_users = {
#            "users": [
#                    {"username": "github_username1", "repositories": [
#                        { "name" :"rep_name_1", "html_url":"html_url_1", "description":"ds_1",  "language":"lang_1"}, 
#                        { "name" :"rep_name_2", "html_url":"html_url_2", "description":"ds_2",  "language":"lang_2"}
#                        ]
#                    },
#                ]
#            }

def get_github_users():
    github_users_list = {}
    try:
        with open(GITHUB_PERSISTED_FILE, 'rb') as handle:
            github_users_list = pk.load(handle) # loads the persisted data from the file
    except:
       github_users_list = {"users": []} # it returns an empty structure to allow the first import call
    return github_users_list

def upsert_github_users(github_user):
    usr_idx = -1
    rep_list = call_github_api(github_user)
    github_user_obj = {"username": github_user, "status": "",  "repositories": rep_list }
    gh_list = get_github_users() # gets the file 

    for i, u in enumerate(gh_list['users']):
        if u['username'] == github_user:
            usr_idx = i
            break

    if usr_idx == -1:
        gh_list['users'].append(github_user_obj) # new user
    else:
        gh_list['users'][usr_idx]= github_user_obj # update an existent user

    with open(GITHUB_PERSISTED_FILE, 'wb') as handle:
        pk.dump(gh_list, handle, protocol=pk.HIGHEST_PROTOCOL) # update the persisted file

    return usr_idx # return this id to display in the screen if it is an insert (-1) or an update (> -1)

