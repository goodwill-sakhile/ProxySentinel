import os
# Force Kivy to use software rendering
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.core.text import LabelBase
LabelBase.register(name="Billabong", fn_regular="fonts/Billabong.otf")
LabelBase.register(name="BeautifulPeoplePersonalUse-dE0g", fn_regular="fonts/BeautifulPeoplePersonalUse-dE0g.ttf")
root = Builder.load_string("""
<MainBox>:
    md_bg_color:47/float(255), 79/float(255), 79/float(255), 1
    MDBoxLayout:
        orientation:"vertical"
        MDBoxLayout:
            size_hint_y:None
            height:"110dp"
            orientation:"vertical"
            MDBoxLayout:
                size_hint_y:None
                height:"60dp"
                MDLabel:
                    text: "ProxySentinel"
                    font_size:"30dp"
                    font_name:"Billabong"
                    halign:"center"
                    valign:"middle"
                    color:1, 1, 1, 1
            MDBoxLayout:
                size_hint_y:None
                height:"50dp"
                spacing:20
                Widget:
                MDIconButton:
                    icon:"block-helper"
                    pos_hint:{"center_x":.5, "center_y":.5}
                    user_font_size:"50sp"
                    theme_text_color:"Custom"
                    text_color:1, 1, 1, 1
                    md_bg_color:0, 220/float(255), 154/float(255), 1
                    
                MDIconButton:
                    icon:"av-timer"
                    pos_hint:{"center_x":.5, "center_y":.5}
                    user_font_size:"50sp"
                    theme_text_color:"Custom"
                    text_color:1, 1, 1, 1
                MDIconButton:
                    icon:"history"
                    pos_hint:{"center_x":.5, "center_y":.5}
                    user_font_size:"50sp"
                    theme_text_color:"Custom"
                    text_color:1, 1, 1, 1
                MDIconButton:
                    icon:"onepassword"
                    pos_hint:{"center_x":.5, "center_y":.5}
                    user_font_size:"50sp"
                    theme_text_color:"Custom"
                    text_color:1, 1, 1, 1
                Widget:
        MDBoxLayout:
            ScreenManager
                MDScreen:
                    name:"block_site"
                    MDBoxLayout:
                        Widget:
                        MDBoxLayout:
                            size_hint_x:None
                            width:"400dp"
                            orientation:"vertical"
                            spacing: 10
                            MDBoxLayout:
                                size_hint_y:None
                                height:"100dp"
                            MDBoxLayout:
                                size_hint_y:None
                                height:"50dp"
                                MDLabel:
                                    text:"Enter Search Words"
                                    font_name:"BeautifulPeoplePersonalUse-dE0g"
                                    text_size:self.size
                                    halign:"center"
                                    valign:"middle"
                                    color:1, 1, 1, 1
                            MDTextField:
                                id: name_field
                                helper_text: "This will be used to personalize your profile"
                                helper_text_mode: "on_focus"
                                icon_right: "account"
                                size_hint_x: 1
                                mode: "rectangle"
                                fill_color: 0.1, 0.1, 0.1, 0.05
                                text_color: 1, 1, 1, 1
                                hint_text_color_focus: 1, 0.5, 0, 1
                                #line_color_focus: 0, 154/float(255), 220/float(255), 1
                                line_color_normal:0, 154/float(255), 220/float(255), 1
                                icon_right:"magnify"
                            MDRaisedButton:
                                text: "Search Sites to Block"
                                font_name:"BeautifulPeoplePersonalUse-dE0g"
                                size_hint_x: 1
                                size_hint_y: None
                                height: "50dp"
                                md_bg_color: 0, 220/float(255), 154/float(255), 1  # Orange background
                                text_color: 1, 1, 1, 1     # White text
                                font_size: "18sp"
                                radius: [12, 12, 12, 12]  # Rounded corners
                                elevation: 4
                            Widget:
                        Widget:
""")
class MainBox(MDBoxLayout):
    pass
class WebsiteBlocker(MDApp):
    def build(self):
        root = MainBox()
        return root
if __name__ == "__main__":
    WebsiteBlocker().run()
