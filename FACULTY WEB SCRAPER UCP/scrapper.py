import requests
from bs4 import BeautifulSoup
import pandas as pd

KEYWORDS = [
    'Professor',
    'Associate Professor',
    'Assistant Professor',
]

def fetch_page_content(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')

def extract_faculty_positions(soup):
    return soup.find_all('h4', class_='small-text')

def is_relevant_position(role):
    return any(keyword in role for keyword in KEYWORDS)

def extract_faculty_info(position_tag):
    name_tag = position_tag.find_previous('h3', class_='item-title').find('a')
    if not name_tag:
        return None, None, None, None
    
    name = name_tag.get_text(strip=True) or None
    profile_link = name_tag['href']
    
    profile_soup = fetch_page_content(profile_link)
    email = extract_email(profile_soup)
    research_interest = extract_research_interest(profile_soup)
    
    return name, profile_link, email, research_interest

def extract_email(soup):
    contact_info = soup.find('div', class_='extra-info')
    return contact_info.find('i', class_='email').next_sibling.strip() if contact_info else None

def extract_research_interest(soup):
    research_section = soup.find('h4', string='Research Interest')
    if research_section:
        research_detail = research_section.find_next('td')
        return research_detail.get_text(strip=True) if research_detail else None
    return None

def collect_faculty_data(faculty_url):
    soup = fetch_page_content(faculty_url)
    faculty_positions = extract_faculty_positions(soup)
    
    faculty_data = {
        'Name': [],
        'Designation': [],
        'Email': [],
        'Research Interest': []
    }

    for position in faculty_positions:
        role = position.get_text(strip=True) or None
        if is_relevant_position(role):
            name, profile_link, email, research_interest = extract_faculty_info(position)
            if name:
                faculty_data['Name'].append(name)
                faculty_data['Designation'].append(role)
                faculty_data['Email'].append(email)
                faculty_data['Research Interest'].append(research_interest)
    
    return faculty_data

def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

if __name__ == "__main__":
    faculty_url = 'https://ucp.edu.pk/faculty-of-information-technology-and-computer-science/faculty-members/'
    faculty_data = collect_faculty_data(faculty_url)
    save_to_csv(faculty_data, 'faculty_info.csv')
