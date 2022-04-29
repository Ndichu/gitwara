from kivymd.app import MDApp
from kivy.lang import Builder
import webbrowser
from kivy.uix.screenmanager import Screen, ScreenManager

navigation_helper = """
ScreenManager:
    GetStartedScreen:
    RegisterScreen:
    
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
            font_style: 'Subtitle1'
            
            
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
                        on_press: root.manager.current = 'screen2'
                           
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
<RegisterScreen>:
    name: 'screen2'
    ScrollView:
    
        orientation: 'vertical'
        
        MDCard:
            size_hint: None, None
            size:root.width,root.height
            spacing: 25
            padding: 25
            elevation: 12
            orientation: 'vertical'
            pos_hint: {"center_x": .5, "center_y": .5}
            size_hint_y: None
            text_size: self.width, None
            background_color: (150, 75, 0)
            
            MDLabel:
                id: head_text
                text: "Gwitara"
                font_size: 40
                halign: 'center'
                size_hint_y: None
                height: self.texture_size[1]
                padding_y:15
            
            MDTextFieldRound:
                id: firstname
                hint_text: "First name"
                icon_right: "account"
                size_hint_x: None
                width: 200
                font_size:18
                pos_hint:{"center_x": 0.5}

            MDTextFieldRound:
                id: middlename
                hint_text: "Middle name"
                icon_right: "account"
                size_hint_x: None
                width: 200
                font_size:18
                pos_hint:{"center_x": 0.5}
                
            MDTextFieldRound:
                id: lastname
                hint_text: "Last name"
                icon_right: "account"
                size_hint_x: None
                width: 200
                font_size:18
                pos_hint:{"center_x": 0.5}
            
            MDTextFieldRound:
                id: gender
                hint_text: "Gender: Male or Female"
                icon_right: "user"
                size_hint_x: None
                width: 200
                font_size:18
                pos_hint:{"center_x": 0.5}
                
            MDTextFieldRound:
                id: DOB
                hint_text: "Date of Birth: day/month/year"
                icon_right: "calender"
                size_hint_x: None
                width: 200
                font_size:18
                pos_hint:{"center_x": 0.5}
                
            MDTextFieldRound:
                id: userphone
                hint_text: "Phone number"
                icon_right: "phone"
                size_hint_x: None
                width: 200
                font_size:18
                pos_hint:{"center_x": 0.5}

            MDTextFieldRound:
                id: useremail
                hint_text: "Email"
                icon_right: "email"
                size_hint_x: None
                width: 200
                font_size:18
                pos_hint:{"center_x": 0.5}

            
            MDTextFieldRound:
                id: county
                hint_text: "County"
                icon_right: "map"
                size_hint_x: None
                width: 200
                font_size:18
                pos_hint:{"center_x": 0.5}
            
            MDTextFieldRound:
                id: subcounty
                hint_text: "Sub-County"
                icon_right: "map"
                size_hint_x: None
                width: 200
                font_size:18
                pos_hint:{"center_x": 0.5}


            MDTextFieldRound:
                id: ward
                hint_text: "Ward"
                icon_right: "map"
                size_hint_x: None
                width: 200
                font_size:18
                pos_hint:{"center_x": 0.5}

            
            MDRoundFlatButton:
                text: "SUBMIT"
                font_size:12
                pos_hint:{"center_x":0.5}
                on_press: root.manager.current = 'screen1'
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
class RegisterScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(GetStartedScreen(name='screen1'))
sm.add_widget(RegisterScreen(name='screen2'))



class Gwitara(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = 'Brown'
        screen = Builder.load_string(navigation_helper)
        return  screen 
   
        
    def any_Function(instance):

        webbrowser.open('http://www.yamumbi.com') 

Gwitara().run()

