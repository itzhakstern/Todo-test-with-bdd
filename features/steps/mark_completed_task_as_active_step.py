from behave import when, then
TASK = 'Wake up'

@when(u'I make the task "Wake up" active')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/ng-view/section/footer/ul/li[2]/a').click()
    check_task = context.driver.find_element_by_xpath('/html/body/ng-view/section/section/ul/li/div/label')
    assert check_task.text == TASK, 'test5_Mark_completed_task_as_active is fail'
    print('test5_Mark_completed_task_as_active is passed successfully')


@then('"Wake up" task mot in IsCompleted list')
def step_impl(context):
    check_task = context.driver.find_element_by_xpath('/html/body/ng-view/section/section/ul/li/div/label')
    assert check_task.text == TASK, 'test5_Mark_completed_task_as_active is fail'
    print('test5_Mark_completed_task_as_active is passed successfully')