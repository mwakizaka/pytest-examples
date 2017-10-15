from selene.tools import s, ss, visit
from selene.bys import by_link_text
from selene.conditions import visible
from selene.elements import text, texts


def test_somewhere():
    visit("https://todomvc4tasj.herokuapp.com/")
    s("#new-todo").set("a").press_enter()
    s("#new-todo").set("b").press_enter()
    s("#new-todo").set("c").press_enter()
    ss("#todo-list li").should_have(texts("a", "b", "c"))
    ss("#todo-list li").findBy(text("b")).s(".toggle").click()
    s(by_link_text("active")).click()
    tasks = ss("#todo-list li")
    tasks.filterBy(visible).should_have(texts("a", "c"))
