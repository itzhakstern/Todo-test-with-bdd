from  behave import when, then
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
WAITING_TIME = 1

@when(u'I delete the task "Wake up"')
def step_impl(context):
    action = ActionChains(context.driver)
    element_to_edit = context.driver.find_element_by_css_selector('label[ng-dblclick="editTodo(todo)"]')
    action.double_click(element_to_edit).perform()
    edition_task = context.driver.find_element_by_css_selector('input[todo-focus="todo == editedTodo"]')
    edition_task.send_keys(Keys.CONTROL, 'a')
    time.sleep(1)
    edition_task.send_keys(Keys.BACKSPACE + '\n')
    context.driver.implicitly_wait(WAITING_TIME)


@then(u'the task list will be empty')
def step_impl(context):
    msg_task = context.driver.find_element_by_css_selector('input[ng-model="newTodo"]').text
    assert msg_task == '', 'test3_delete_a_task is fail'
    print('test3_delete_a_task is passed successfully')