import requests
import os
from dotenv import load_dotenv

load_dotenv()


NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("DATABASE_ID")
HEADERS = {
    "Authorization" : f"Bearer {NOTION_TOKEN}",
    "Content-Type" : "application/json",
    "Notion-Version" : "2022-06-28"
}

def search_for_pageID(txt_name,txt_autor):
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    
    payload = {
        "filter" : {
            "and" : [
                {"property": "Livro", "title": {"equals":txt_name}},
                {"property":"Autor","rich_text": {"equals": txt_autor}}
            ]
        }
    }
    
    try:
        response = requests.post(url, json=payload, headers=HEADERS)
        dados = response.json()
 

        if "results" in dados and dados["results"]:
            return dados["results"][0]["id"]
    except Exception as e:
        print(f"Erro na busca: {e}")
        
    return None

def update_Notion_grades(page_id,notas_dict):
    
    url = f"https://api.notion.com/v1/pages/{page_id}"
    
    payload = {
        "properties":{
            "Nota(Número)": {"number" : notas_dict["final"]},
            "Escrita": {"number": notas_dict["escrita"]},
            "Fluidez" : {"number": notas_dict["fluidez"]},
            "Plot/Clareza": {"number": notas_dict["plot"]}
        }
    }
    res = requests.patch(url, json=payload, headers=HEADERS)
    return res.status_code == 200