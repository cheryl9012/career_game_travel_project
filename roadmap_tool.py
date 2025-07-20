from agents import function_tool

@function_tool
def get_career_roadmap(field:str) -> str:
    maps = {
        "software engineer": "Learn Python , DSA , Web Dev , Github , Projects",
        "data science": "Master Python , Panadas, ML, and real-world datasets.",
        "graphic designer":"Learn Figma , UI/UX , Portfolio.",
        "ai" : "Study Python , Deep learning, Transformers , and AI tools"
   }
    return maps.get(field.lower(), "No roadmap found for that field")