"""
Main exp
"""
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.button import button
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.datatables import MDDataTable


class MainContainer(BoxLayout):
    pass


class ABAccordion(BoxLayout):
    pass


class ABRegistry(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print(self.ids)
        # data_tables = MDDataTable(
        #     use_pagination=True,
        #     check=True,
        #     column_data=[
        #         ("No.", dp(30)),
        #         ("Status", dp(30)),
        #         ("Signal Name", dp(60)),
        #         ("Severity", dp(30)),
        #         ("Stage", dp(30)),
        #         ("Schedule", dp(30)),
        #         ("Team Lead", dp(30)),
        #     ],
        #     row_data=[
        #         (
        #             "1",
        #             ("alert", [255 / 256, 165 / 256, 0, 1], "No Signal"),
        #             "Astrid: NE shared managed",
        #             "Medium",
        #             "Triaged",
        #             "0:33",
        #             "Chase Nguyen",
        #         ),
        #         (
        #             "2",
        #             ("alert-circle", [1, 0, 0, 1], "Offline"),
        #             "Cosmo: prod shared ares",
        #             "Huge",
        #             "Triaged",
        #             "0:39",
        #             "Brie Furman",
        #         ),
        #         (
        #             "3",
        #             (
        #                 "checkbox-marked-circle",
        #                 [39 / 256, 174 / 256, 96 / 256, 1],
        #                 "Online",
        #             ),
        #             "Phoenix: prod shared lyra-lists",
        #             "Minor",
        #             "Not Triaged",
        #             "3:12",
        #             "Jeremy lake",
        #         ),
        #         (
        #             "4",
        #             (
        #                 "checkbox-marked-circle",
        #                 [39 / 256, 174 / 256, 96 / 256, 1],
        #                 "Online",
        #             ),
        #             "Sirius: NW prod shared locations",
        #             "Negligible",
        #             "Triaged",
        #             "13:18",
        #             "Angelica Howards",
        #         ),
        #         (
        #             "5",
        #             (
        #                 "checkbox-marked-circle",
        #                 [39 / 256, 174 / 256, 96 / 256, 1],
        #                 "Online",
        #             ),
        #             "Sirius: prod independent account",
        #             "Negligible",
        #             "Triaged",
        #             "22:06",
        #             "Diane Okuma",
        #         ),
        #     ]
        # )


class ABApp(MDApp):

    def build(self):
        return MainContainer()


if __name__ == '__main__':
    ABApp().run()
