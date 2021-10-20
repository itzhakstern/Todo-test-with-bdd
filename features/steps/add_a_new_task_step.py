from behave import when, then
WAITING_TIME = 1

TASK1 = 'Clean my house'

@when(u'I add new task "Clean my house"')
def step_impl(context):
    context.driver.find_element_by_css_selector('input[ng-model="newTodo"]').send_keys(f"{TASK1}\n")
    context.driver.implicitly_wait(WAITING_TIME)

@then(u'the task "Clean my house" will be added to the list')
def step_impl(context):
    elements = context.driver.find_elements_by_css_selector('label[ng-dblclick="editTodo(todo)"]')
    for elem in elements:
        if elem.text == TASK1:
            print("test1_add_a_new_task is passed successfully")
            return
    print("ERROR - the task not found in the todo list")
