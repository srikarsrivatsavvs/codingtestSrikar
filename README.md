What does this application do? 
It takes the input of a github public repo url and email id, and it sends out the summary of the PRs present on the repo.

Some application info - 
- It has been built using Python FastAPI framework 
- To run the application, I'm currently using uvicorn: uvicorn app:app --host 0.0.0.0 --port 80 
- Application has been hosted on an EC2 instance to make the api accessible **( currently this won't work, as i've not hosted the application )**
- Amazon SES is being used for sending Emails.

About the API: 
- A simple POST request api has been created, that takes input of a repo url, and email id
- API CURL request example( Go ahead, try it out from your postman! ) : **( currently this won't work, as i've not hosted the application )**
    curl --location 'http://15.206.166.176/getpulls' --header 'Content-Type: application/json' --data-raw '{"repo": "https://api.github.com/repos/sveltejs/svelte/pulls?state=all&per_page=100", "email": "srikar_srivatsav@yahoo.co.in"}'
- Limitations of the current API endpoint: 
    1. Api request isn't being authenticated
    2. Email sent in the request body isn't being validated if it's of the right format or not
    3. Repo url in the request body takes the api.github.com format only. Any other formats are not supported at the moment
    4. Emails can only be sent to my single verified email right now, as SES is in sandbox environment
    5. If the repo has 0 pull requests, api sends out the same template email with no pull request data. This can be handled at a later point

