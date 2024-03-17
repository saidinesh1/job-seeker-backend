# services/skills_extractor_service.py
import pandas as pd
import string
from constants.skills_map import skills_map

class SkillsExtractorService:
    @staticmethod
    def write_extracted_skills_to_txt(file_path):
        df = pd.read_csv(file_path)
        skills_df = df['Example']
        skills_df = skills_df.dropna()
        skills_df = skills_df.drop_duplicates()
        skills = skills_df.to_list()
        skill_map = {}

        for skill in skills:
            s = skill.split()
            s_list = []

            for word in s:
                word_list = []
                for char in word:
                    if char not in string.punctuation:
                        word_list.append(char)
                s_list.append(''.join(word_list).lower())

            skill_map[''.join(s_list)] = skill

        py_file_path = r"F:\job-seeker-backend\constants\skills_map.py"

        with open(py_file_path, 'w') as file:
          file.write('skills_map = {\n')
          for key, value in skill_map.items():
              file.write(f"    '{key}': '{value}',\n")
          file.write('}\n')

        return "Skills written into constants dir."

    @staticmethod
    def get_extracted_skills():
        return skills_map

SkillsExtractorService.write_extracted_skills_to_txt(r"F:\job-seeker-backend\Dataset\technology_skills.csv")