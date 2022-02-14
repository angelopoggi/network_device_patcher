import pglet
from pglet import Stack, Textbox, Button, Checkbox, Text
from firewall_cve_webui.lib.netmon_requester import netmon_connect
from firewall_cve_webui.core.button_demo import DemoButon


def main(page):
    page.title = "Firewall CVE Vulnerability List"
    page.horizontal_align = 'center'
    page.update()  # needs to be called every time "page" control is changed

    #Create the Boxes with Router Host name and OS
    routers = netmon_connect("devices?type=firewall")
    for router in routers['devices']:
        button = DemoButon.action()
        page.add(
            Text(
                f'{router["hostname"]} : {router["os"]} : {router["version"]} : {button}',
                block=False,
                align="left",
            ),
        )


    # def add_clicked(e):
    #     tasks_view.controls.append(Checkbox(label=new_task.value))
    #     tasks_view.update()
    #
    # new_task = Textbox(placeholder='Whats needs to be done?', width='100%')
    # tasks_view = Stack()
    #
    # page.add(Stack(width='70%', controls=[
    #     Stack(horizontal=True, on_submit=add_clicked, controls=[
    #         new_task,
    #         Button('Add', on_click=add_clicked)
    #     ]),
    #     tasks_view
    # ]))

if __name__ == "__main__":
    pglet.app("Firewall CVEs", target=main)