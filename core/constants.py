REPOS_URL = 'https://api.github.com/users/{user}/repos?client_id={id}&client_secret={secret}'.format

COUNT_FILES_URL = 'https://api.github.com/search/code?q=repo:{user}/{reponame}+{lang}&client_id={client_id}&client_secret={client_secret}'.format