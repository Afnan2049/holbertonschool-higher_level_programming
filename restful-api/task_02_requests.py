import requests
import csv

def fetch_and_print_posts():
    """Fetches posts from JSONPlaceholder and prints titles."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get('title'))

def fetch_and_save_posts():
    """Fetches posts and saves id, title, and body to a CSV file."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    if response.status_code == 200:
        posts = response.json()
        
        # Structure the data: filtering only the required keys
        data_to_save = [
            {'id': post['id'], 'title': post['title'], 'body': post['body']}
            for post in posts
        ]
        
        # Define CSV column headers
        fieldnames = ['id', 'title', 'body']
        
        # Write to CSV
        with open('posts.csv', mode='w', encoding='utf-8', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data_to_save)
