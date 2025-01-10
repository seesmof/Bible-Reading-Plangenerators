'''
Add Bible reading tasks into Todoist.
'''

TODOIST_API_KEY='e3b0b2ed0642281f8f775fc954ef1567ea84537c'

from todoist_api_python.api import TodoistAPI

def todoist_add_daily_reading(
    given_day: int = None
):
    todoist=TodoistAPI(TODOIST_API_KEY)
    tasks=todoist.get_tasks()

    def check_available_tasks(
        task_name:str,
        parent:int=None,
    ):
        return [
            t for t in tasks 
            if task_name in t.content 
            and (t.parent_id==parent if parent else True)
        ]
    
    def add_unique_task(
        task_name:str,
        parent:int=None,
        due:str=None,
    ):
        duplicates=check_available_tasks(task_name,parent)
        new_task=todoist.add_task(task_name,parent_id=parent,due_string=due) if not duplicates else duplicates[0]
        return new_task
    
    with open(data_file_path,'r') as f:
        data=json.load(f)
    day=data['day'] if not given_day else given_day

    main_task_name=f'Біблія {day}'
    parent_id=add_unique_task(main_task_name,due='today').id

    reading_list=get_reading_for_day(day)
    for Book_number,chapter_number in reading_list:
        add_unique_task(get_formatted_link(Book_number,chapter_number),parent_id)

    if not given_day:
        data['day']+=1
        with open(data_file_path,'w') as f:
            json.dump(data,f)