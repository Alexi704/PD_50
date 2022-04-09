import json

class CandidateManager:

    def __init__(self, path):
        self.path = path

    def load_candidates_from_json(self):
        """" возвращает список всех кандидатов """
        with open(self.path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def get_candidate_by_id(self, candidate_id):
        """" возвращает одного кандидата по его id """
        candidates = self.load_candidates_from_json()
        for candidate in candidates:
            if candidate['id'] == candidate_id:
                return candidate

    def get_candidates_by_name(self, candidate_name):
        """" возвращает кандидатов по имени """
        candidates = self.load_candidates_from_json()
        candidate_matches = []
        candidate_name_lower = candidate_name.lower()
        for candidate in candidates:
            if candidate_name_lower in candidate['name'].lower():
                candidate_matches.append(candidate)
        return candidate_matches

    def get_candidates_by_skill(self, skill_name):
        """" возвращает кандидатов по навыку """
        candidates = self.load_candidates_from_json()
        candidate_matches = []
        skill_name_lower = skill_name.lower()
        for candidate in candidates:
            skill_set = candidate['skills'].strip().lower().split(', ')
            if skill_name_lower in skill_set:
                candidate_matches.append(candidate)
        return candidate_matches
