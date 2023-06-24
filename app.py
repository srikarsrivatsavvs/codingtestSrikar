from fastapi import FastAPI, HTTPException
from item import Item
from send_email import send_email
from pull_requests import github_pull

app = FastAPI()

@app.post("/getpulls") #Creating a post api method
def get_pulls(item: Item): #Request body 
    try: 
        pull_summary = github_pull(item.repo)
        send_email(item.email, pull_summary)
        return pull_summary
    except: 
        raise HTTPException(status_code=500, detail="Something went wrong. Check the request")