import requests as req
pr_list=req.get("https://api.github.com/repos/kubernetes/kubernetes/pulls").json()
creators={}

for pr in pr_list:
    if pr["user"]["login"] in creators:
        creators[pr["user"]["login"]]+=1
    else:
        creators[pr["user"]["login"]]=1

for ele in creators:
    print(f"{ele} has created {creators[ele]} PRs")