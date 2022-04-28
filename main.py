from kivymd.app import MDApp
from kivy.lang import Builder
import webbrowser
from kivy.uix.screenmanager import Screen, ScreenManager

navigation_helper = """
ScreenManager:
    GetStartedScreen:
    
<GetStartedScreen>:
    name: 'screen1'
    BoxLayout:
        orientation: 'vertical'
        ScrollView:
        Image:
            source: 'logo.jpg'
        MDLabel:
            text: 'Gwitara App is a tool for self-registration of members of the Agikuyu Community wherever they are. It is voluntary and free. The information you give shall be treated as highly confidential and shall only be used for purposes of information sharing among the Agikuyu people and establishing our numerical strength as a community.'
            halign:'center'
            font_style: 'Caption'
        Widget:
            size_hint_y: None
            height:10
            
        MDRectangleFlatButton:
            text:'Register Now'
            pos_hint:{"center_x":0.5}
            on_press: root.manager.current = 'screen2'
            
        Widget:
            size_hint_y: None
            height:30
        
        MDRectangleFlatButton:
            text:'Register Later'
            pos_hint:{"center_x":0.5}
            on_press: app.stop()
        Widget:
            size_hint_y: None
            height:36
        MDBottomAppBar:
            MDToolbar:
                mode: 'free-end'
                type: 'bottom'
                icon: 'pen'
                on_action_button: nav_drawer.set_state('toggle')
                MDLabel:
                    id: footer_text
                    text: "Powered by: Pigeon Data Handlers In Collaboration with Kikuyu Council of Elders"
                    font_size: 12
                    halign: 'center'
                    color: (1, 1, 1, 1)
                    size_hint_y: None
                    height: self.texture_size[1]
                    padding_y:5    
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Gwitara'
                        left_action_items: [["menu", lambda x: nav_drawer.set_state('toggle')]]
                        elevation: 10
                    Widget: 
                    
    MDNavigationDrawer:
        id: nav_drawer
        BoxLayout:
            orientation: 'vertical'
            spacing: '8dp'
            padding: '8dp'
            Image:
                source: 'logo.png'
            MDLabel:
                text: 'Gwitara App .'
                font_style: 'Subtitle1'
                size_hint_y: None
                height: self.texture_size[1]
            ScrollView: 
                MDList: 
                    MDRectangleFlatButton:
                        spacing: '8dp'
                        padding: '8dp'
                        text:' Register Now'
                        pos_hint:{"center_x":0.5}
                        on_press: root.manager.current = 'screen1'
                           
                    MDRectangleFlatButton:
                        spacing: '8dp'
                        padding: '8dp'
                        text:' Visit Website'
                        pos_hint:{"center_x":0.5}
                        on_press: app.any_Function()
                    
                    MDRectangleFlatButton:
                        
                        text:'Exit App'
                        pos_hint:{"center_x":0.5}
                        on_press: app.stop() 
            
            MDLabel:
                text: 'Powered by: Pigeon Data Handlers In Collaboration with Kikuyu Council of Elders '
                font_style: 'Caption'
                size_hint_y: None
                height: self.texture_size[1]
            
                
            
            MDLabel:
                text: 'Version 1.0; Copyright ©'
                font_style: 'Caption'
                size_hint_y: None
                height: self.texture_size[1]
            
            MDLabel:
                text: 'Pigeon Data Handlers 2022'
                font_style: 'Caption'
                size_hint_y: None
                height: self.texture_size[1]
    

"""

class GetStartedScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(GetStartedScreen(name='screen1'))



class Gwitara(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = 'Brown'
        screen = Builder.load_string(navigation_helper)
        return  screen 
   
        
    def any_Function(instance):

        webbrowser.open('http://www.yamumbi.com') 

Gwitara().run()

