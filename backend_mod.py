import pickle as pk 
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
            github_users_list = pk.load(handle)
    except:
       github_users_list = {"users": []}


    return github_users_list

def upsert_github_users(github_user):
    usr_idx = -1

    github_user_obj = {"username": github_user, "status": "",  "repositories": [] }
    gh_list = get_github_users()

    for i, u in enumerate(gh_list['users']):
        if u['username'] == github_user:
            usr_idx = i
            break

    if usr_idx == -1:
        gh_list['users'].append(github_user_obj)
    else:
        gh_list['users'][usr_idx]= github_user_obj


    with open(GITHUB_PERSISTED_FILE, 'wb') as handle:
        pk.dump(gh_list, handle, protocol=pk.HIGHEST_PROTOCOL)

    return usr_idx

def call_github_api():

    return {}
