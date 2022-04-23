import json

with open('candidates.json', 'r', encoding='utf-8') as file:
    candidates = json.load(file)


def get_all_candidates():
    """получаем список всех кандидатов, и выводим информацию в нужном нам формате"""
    page_content = ''
    for candidate in candidates:
        page_content += 'Имя кандидата: ' + candidate['name'] + '\n'
        page_content += 'Позиция: ' + candidate['position'] + '\n'
        page_content += 'Навыки: ' + candidate['skills'] + '\n\n'
    return '<pre>' + page_content + '</pre>'


def get_candidate_for_uid(uid):
    """получаем данные конкретного кандидата"""
    page_content = ''
    for candidate in candidates:
        if candidate['id'] == uid:
            link_pictirs = candidate['picture']
            page_content += f'<img src = {link_pictirs}>'
            page_content += '<pre>'
            page_content += 'Имя кандидата: ' + candidate['name'] + '\n'
            page_content += 'Позиция: ' + candidate['position'] + '\n'
            page_content += 'Навыки: ' + candidate['skills'] + '\n\n'
            page_content += '</pre>'
    return page_content


def get_candidates_for_skill(skill):
    """получаем данные кандидатов с нужными нам скилами"""
    page_content = ''
    for candidate in candidates:
        if skill in candidate['skills'].lower().split(', '):
            page_content += '<pre>'
            page_content += 'Имя кандидата: ' + candidate['name'] + '\n'
            page_content += 'Позиция: ' + candidate['position'] + '\n'
            page_content += 'Навыки: ' + candidate['skills'] + '\n\n'
            page_content += '</pre>'
    return page_content
