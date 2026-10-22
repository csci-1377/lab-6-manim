from manim import *

class helloWorld(Scene):
    def construct(self):
        text = Text("Hello World!")
        self.play(Create(text))
        self.wait()
        
