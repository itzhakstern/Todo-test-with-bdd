from behave import given, when, then
WAITING_TIME = 1
TASK = 'Wake up'

@given(u'there is a completed task "Clean the house" in the list')
def step_impl(context):
    context.driver.find_element_by_css_selector('input[ng-model="newTodo"]').send_keys("Clean the house\n")
    context.driver.implicitly_wait(WAITING_TIME)

@when(u'I click on Clear completed tasks')
def step_impl(context):
    context.driver.find_element_by_xpath("/html/body/ng-view/section/section/ul/li[2]/div/input").click()
    context.driver.implicitly_wait(WAITING_TIME)
    context.driver.find_element_by_class_name("clear-completed").click()
    context.driver.implicitly_wait(WAITING_TIME)


@then('the task "Wake up" is not in Completed list')
def step_impl(context):
    elements = context.driver.find_elements_by_css_selector(
        'li[ng-repeat="todo in todos | filter:statusFilter track by $index"]')
    print("test6_clear_completed_tasks is passed successfully") if len(elements) == 1 and elements[0].text == TASK \
        else print('test6_clear_completed_tasks is fail')