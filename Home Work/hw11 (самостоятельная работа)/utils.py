import json

with open('candidates.json', 'r', encoding='utf-8') as file:
    content_json = json.load(file)


def load_candidates_from_json():
    """возвращает список всех кандидатов с указанием определенных критериев (uid, имя, картинка)"""
    user_qualities = []
    for item in content_json:
        user_qualities.append([item['id'], item['name'], item['picture']])
    return user_qualities


def get_candidate(uid):
    """возвращает одного кандидата по его id (uid)"""
    candidate = []
    for item in content_json:
        if uid == item['id']:
            candidate.extend(
                [item['name'], item['picture'], item['position'], item['gender'], item['age'], item['skills']])
    return candidate


def get_candidates_by_name(candidate_name):
    """возвращает список всех кандидатов по заданному имени"""
    candidate = []
    candidate_name = candidate_name.lower().strip()
    for item in content_json:
        if candidate_name in item['name'].lower():
            candidate.append(
                [item['id'], item['name'], item['picture'], item['position'], item['gender'], item['age'], item['skills']])
    return candidate


def get_candidates_by_skill(skill_name, count_limit):
    """возвращает список всех кандидатов по скилам"""
    candidate = []
    counter = 0
    for item in content_json:
        if skill_name in item['skills'].lower().split(', '):
            candidate.append(
                [item['id'], item['name'], item['picture'], item['position'], item['gender'], item['age'], item['skills']])
            counter += 1
        if counter >= count_limit:
            break
    return candidate
