from  behave import then
WAITING_TIME = 1
TASK = 'Wake up'

@then(u'the task "Wake up" will appear as completed')
def step_impl(context):
    context.driver.find_element_by_css_selector('input[ng-model="todo.completed"]').click()
    context.driver.implicitly_wait(WAITING_TIME)
    context.driver.find_element_by_xpath('/html/body/ng-view/section/footer/ul/li[2]/a').click()
    check_task = context.driver.find_element_by_xpath('/html/body/ng-view/section/section/ul/li/div/label')
    assert check_task.text == TASK, 'test5_Mark_completed_task_as_active is fail'
    print('test5_Mark_completed_task_as_active is passed successfully')
