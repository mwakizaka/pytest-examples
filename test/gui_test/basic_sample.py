from selene.tools import s, ss, visit
from selene import tools
from selenium import webdriver
from selene.elements import texts, text
from selene.conditions import hidden, empty, css_class, size
from time import sleep


def test_selene_demo():
    tools.set_driver(webdriver.Chrome("drivers/mac/64/chromedriver"))

    visit('http://todomvc4tasj.herokuapp.com')

    tasks = ss("#todo-list>li")
    active_tasks = tasks.filter(css_class("active"))

    for task_text in ["1", "2", "3"]:
        s("#new-todo").set_value(task_text)
        sleep(1)
        s("#new-todo").press_enter()
        sleep(1)

    tasks.should_have(texts("1", "2", "3")).should_have(css_class("active"))
    s("#todo-count").should_have(text("3"))

    tasks[2].element(".toggle").click()

    active_tasks.should_have(texts("1", "2"))
    active_tasks.should_have(size(2))

    tasks.filter(css_class("completed")).should_have(texts("3"))

    s("a[href='#/active']").click()
    tasks[:2].should_have(texts("1", "2"))
    tasks[2].should_be(hidden)

    s("#toggle-all").click()
    s("#clear-completed").click()
    tasks.should_be(empty)