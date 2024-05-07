import requests

url = "https://jsonplaceholder.typicode.com/"

def get_filtered_titles():
    response = requests.get(url+"/posts")
    if response.status_code == 200:
        posts = response.json()
        filtered_titles = [post['title'] for post in posts if len(post['title'].split()) <= 6]
        return filtered_titles
    else:
        print("Failed to fetch data:", response.status_code)

def get_filtered_body():
    response = requests.get(url+"/posts")
    if response.status_code == 200:
        posts = response.json()
        filtered_posts = [post for post in posts if len(post['body'].split('\n')) <= 3]
        return filtered_posts
    else:
        print("Failed to fetch data:", response.status_code)

def make_post_request():
    data = {
        'title': 'New Post Title',
        'body': 'This is the body of the new post.',
        'userId': 1
    }
    response = requests.post(url+"/posts", json=data)
    print("POST Response:", response.status_code)
    print("Response Data:", response.json())

def make_put_request(post_id):
    updated_data = {
        'id': post_id,
        'title': 'Updated Post Title',
        'body': 'This is the updated body of the post.',
        'userId': 1
    }
    response = requests.put(f"https://jsonplaceholder.typicode.com/posts/{post_id}", json=updated_data)
    print("PUT Response:", response.status_code)
    print("Response Data:", response.json())

def make_delete_request(post_id):
    response = requests.delete(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    print("DELETE Response:", response.status_code)

print(get_filtered_titles())
print(get_filtered_body())
print(make_post_request())
print(make_put_request(78))
print(make_delete_request(78))

