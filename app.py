from fastapi import Body, FastAPI
import requests
from datetime import datetime, timedelta
from req_body import Item
import send_email

app = FastAPI()


def github_pull(repo_api_url):
    #access_token = "xxxxx" can be used in case of a private repo you have access for
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)
    # headers = {"Authorization": f"Bearer {access_token}"} will be used with the token
    response = requests.get(repo_api_url) #headers can also be passed here if needed
    pull_requests = response.json()
    pull_requests_last_week = []
    for pr in pull_requests:
        if start_date <= datetime.strptime(pr["created_at"], "%Y-%m-%dT%H:%M:%SZ") <= end_date:
            summary = {"name":pr["user"]["login"],"title":pr["title"],"pull_number":pr["number"],"created_at_date":pr["created_at"], "request_state": pr["state"], "is_draft": pr["draft"]}
            pull_requests_last_week.append(summary)
        else:
            break   #by default, github api returns sort based on created date, hence i can break out of the look once date doesn't fall in range 
    return pull_requests_last_week

@app.post("/getpulls")
def get_pulls(item: Item):
    pull_summary = github_pull(item.repo)
    email = send_email.send_email(item.email, pull_summary)
    return pull_summary