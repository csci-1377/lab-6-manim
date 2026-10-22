from manim import *

class LabEx(MovingCameraScene):
    def construct(self):
        label = Text("Pythagorean Theorem", font_size=30, color = WHITE).to_edge(UP)
        """
        Options:
        Can either shift the text using .shift() on the Text()
        OR
        Can place it at the top of the page (easier) using to_edge
        """
        self.play(FadeIn(label))

        # To create basic triangle:
        w_triangle = Triangle(color = WHITE)

        # To create right angle triangle need to connect three lines:
        l1 = ORIGIN           
        l2 = RIGHT * 2          
        l3 = UP * 1.2           
        side_a = Line(l1, l2, color=BLUE).shift(LEFT *1)
        side_b = Line(l3, l1, color=GREEN).shift(LEFT * 1)
        side_c = Line(l2, l3, color=RED).shift(LEFT * 1)
        self.play(Create(side_a), Create(side_b), Create(side_c))

        # To write formula of pythagorean theorem:
        # USING LATEX:

        # General equation would look like:
        pyth_eq = MathTex("a^2 + b^2 = c^2").shift(DOWN *1)

        # Equation that has colors:
        pyth_col = MathTex("a", "^2 + ", "b", "^2 = ", "c", "^2").shift(DOWN *1)
        pyth_col[0].set_color(BLUE)
        pyth_col[2].set_color(GREEN)
        pyth_col[4].set_color(RED)

        self.play(Write(pyth_col))


        # MOVE camera to the right
        self.play(
            self.camera.frame.animate.shift(RIGHT * 4),
            run_time=2
        )
        # If want to move camera to a specific thing instead of just the frame: 
        self.camera.frame.animate.move_to(label) 
        #use move_to not shift and then set it on the specific object
    

        # Create graph:
        axes = Axes(
            x_range=[0, 7], 
            y_range=[0, 7],
            # If wanted to include increments: y_range=[0, 1, 0.2], # y range 0~1, in 0.2 increments
            x_length=5,
            y_length=5,
            tips=True,
            axis_config={"tip_length": 0.1,"tip_width": 0.2,}, 
            x_axis_config={"include_numbers": True},
            y_axis_config={"include_numbers": True}
        ).shift(RIGHT * 7)  # Need to fit new camera scene

        self.play(FadeIn(axes)) 

        #Remove triangle:
        self.play(FadeOut(side_a, side_b, side_c))
        self.wait()

        # Add triangle to graph
        h = 1
        line = axes.plot(
            lambda x: 1, 
            x_range=[1, 4],  # Limits the line to a specific domain
            color=BLUE
        )

        # Needs to be PARAMETRIC for vertical line
        line2 = axes.plot_parametric_curve(
            lambda t: np.array([1, t]),  # x is locked at -2, y changes with t
            t_range=[1, 5],              # The y-axis boundaries for the line
            color=GREEN
        )

        line3 = axes.plot(
            lambda x: (-4/3) * x + 19/3, 
            x_range=[1, 4],  # Limits the line to a specific domain
            color=RED
        )

        self.play(Create(line), run_time=2) # Create draws in length of run_time
        self.play(Create(line2), run_time=2)
        self.play(Create(line3), run_time=2)

        # add labels to lines:
        label = axes.get_graph_label(line, label="3", x_val=2.5, direction=DOWN, color = BLUE)
        label2 = axes.get_graph_label(line2,label = "4", x_val=2 ,direction =  UL, color = GREEN )
        label3 = axes.get_graph_label(line3, label = "c", x_val = 2.5,direction = UR, color = RED )

        self.play(FadeIn(label, label2, label3))

        # putting text next to something else: use next_to(DIRECTION):
        new_eq = MathTex("3", "^2 + ", "4", "^2 = ", "c", "^2")
        new_eq[0].set_color(BLUE)
        new_eq[2].set_color(GREEN)
        new_eq[4].set_color(RED)
        new_eq.next_to(pyth_col, DOWN, buff = 0.3)
        self.play(Write(new_eq))

        # Adding arrows:
        arrow = Arrow(
            start=label.get_left(), 
            end=new_eq[0].get_top(), # Points directly to the bottom of c^2
            buff=0.1,
            color = BLUE,
            stroke_width = 3,
        )

        arrow2 = Arrow(start = label2.get_left(),
            end = new_eq[2].get_top(),
            buff = 0.1,
            color = GREEN,
            stroke_width=3
        )

        arrow3= Arrow(start = label3.get_left(), end = new_eq[4].get_top(), buff = 0.1, color = RED, stroke_width=3)

        self.play(GrowArrow(arrow))
        self.wait()
        self.remove(arrow)
        self.play(GrowArrow(arrow2))
        self.wait()
        self.remove(arrow2)
        self.play(GrowArrow(arrow3))
        self.wait()
        self.remove(arrow3)


        last_eq = MathTex("c", " = 5")
        last_eq[0].set_color(RED)
        last_eq.next_to(new_eq, DOWN, buff=0.3)
        self.play(Write(last_eq))
        self.wait()

        # Adding an image:
        end_im = ImageMobject("end_image.jpg").shift(RIGHT * 4)
        self.remove(label, pyth_col, axes, line, line2, line3, label, label2, label3, new_eq, last_eq)
        self.add(end_im)
        self.wait()

  









        




