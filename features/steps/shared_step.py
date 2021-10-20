from behave import given, when
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

WAITING_TIME = 1
MSG1 = "Wake up"

@given(u'I am in the todos page')
def step_impl(context):
    context.driver.get("https://todomvc.com/examples/angularjs/#/")
    context.driver.implicitly_wait(WAITING_TIME)

@given(u'there is a task "Wake up" in the list')
def step_impl(context):
    context.driver.find_element_by_css_selector('input[ng-model="newTodo"]').send_keys(f"{MSG1}\n")
    context.driver.implicitly_wait(WAITING_TIME)

@when(u'I make the task "Wake up" completed')
def step_impl(context):
    context.driver.find_element_by_css_selector('input[ng-model="todo.completed"]').click()
    context.driver.implicitly_wait(WAITING_TIME)

