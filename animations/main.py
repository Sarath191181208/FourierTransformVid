
from manim import *
import numpy as np
from math import log10, cos, sin
from scipy.integrate import quad


class IntroText(Scene):
    def construct(self):
        txt = Text(f"What is a Sound ?", font_size=44)
        self.play(Write(txt), run_time=3)
        self.wait(2)
        return super().construct()


class IntroSound(Scene):
    def intro(self):
        sound_text = Text("Mouth :", font_size=30)
        # move sound_text to top left
        sound_text.to_edge(UP*0.8+LEFT*0.9)
        self.play(Write(sound_text), run_time=2)
        # Creating and palying the arcs
        arc = Arc(radius=0.7, start_angle=PI/3, angle=-2*PI/3)
        arc.next_to(sound_text, DOWN, buff=0.5)
        arc.shift(RIGHT*1)
        arcs = [arc]
        for _ in range(6):
            arc2 = Arc(radius=0.7, start_angle=PI/3, angle=-2*PI/3)
            arc2.next_to(arcs[-1], RIGHT, buff=0.5)
            arcs.append(arc2)
        for idx, arc in enumerate(arcs):
            self.play(Create(arc), run_time=(1/log10(idx+2)))
        # self.play(Create(arc), Create(arc2), run_time=3)

        self.wait(2)

    def draw_graph(self):
        axes = Axes(
            x_range=[-1, 22, 2],
            y_range=[-1.5, 1.5, 2],
            x_length=10,
            y_length=3,
            axis_config={'include_numbers': True, 'numbers_to_exclude': [0]},
            x_axis_config={'color': ORANGE},
            y_axis_config={'color': ORANGE},
        ).add_coordinates()
        axes.to_edge(DOWN)
        self.add(axes)
        self.play(DrawBorderThenFill(axes))

        graph = axes.plot(lambda x: np.sin(x),
                          x_range=[0, 20], color=YELLOW)
        self.add(graph)
        self.play(Create(graph), run_time=5)

        self.wait(5)

    def construct(self):
        self.intro()

        arrow = Arrow(np.array([0, 0.6, 0]), np.array([0, -0.6, 0]), buff=0.1)
        self.play(Create(arrow), run_time=2)
        self.wait(2)

        self.draw_graph()

        return super().construct()


class Sound_2(Scene):
    def sound(self):
        sound_text = Text("Mouth :", font_size=30)
        # move sound_text to top left
        sound_text.to_edge(UP*0.8+LEFT*0.9)
        self.play(Write(sound_text), run_time=2)
        # Creating and palying the arcs
        arc = Arc(radius=0.7, start_angle=PI/3, angle=-2*PI/3)
        arc.next_to(sound_text, DOWN, buff=0.5)
        arc.shift(RIGHT*1)
        arcs = [arc]
        for _ in range(6):
            arc2 = Arc(radius=0.7, start_angle=PI/3, angle=-2*PI/3)
            arc2.next_to(arcs[-1], RIGHT, buff=0.5)
            arcs.append(arc2)
        for idx, arc in enumerate(arcs):
            self.play(Create(arc), run_time=(1/log10(idx+2)))
        # self.play(Create(arc), Create(arc2), run_time=3)

        self.wait(2)

    def noise(self):
        sound_text = Text(": Noise", font_size=30)
        # move sound_text to top left
        sound_text.to_edge(UP*0.8+RIGHT)
        self.play(Write(sound_text), run_time=2)
        # Creating and palying the arcs
        arc = Arc(radius=0.7, start_angle=2*PI/3, angle=2*PI/3)
        arc.next_to(sound_text, DOWN, buff=0.5)
        arc.shift(LEFT*1)
        arcs = [arc]
        for _ in range(6):
            arc2 = Arc(radius=0.7, start_angle=2*PI/3, angle=2*PI/3)
            arc2.next_to(arcs[-1], LEFT, buff=0.5)
            arcs.append(arc2)
        for idx, arc in enumerate(arcs):
            self.play(Create(arc), run_time=(1/log10(idx+2)))
        # self.play(Create(arc), Create(arc2), run_time=3)

        self.wait(2)

    def draw_graph(self):
        axes = Axes(
            x_range=[-1, 22, 2],
            y_range=[-3.1415, 3.1415, 2],
            x_length=10,
            y_length=3,
            axis_config={'include_numbers': True, 'numbers_to_exclude': [0]},
            x_axis_config={'color': ORANGE},
            y_axis_config={'color': ORANGE},
        ).add_coordinates()
        axes.to_edge(DOWN)
        self.add(axes)
        self.play(DrawBorderThenFill(axes))

        graph = axes.plot(lambda x: np.sin(x)+np.sin(3*x)-np.cos(x)+np.sin(5*x),
                          x_range=[0, 20], color=YELLOW)
        self.add(graph)
        self.play(Create(graph), run_time=5)

        self.wait(5)

    def construct(self):
        self.sound()
        self.noise()

        arrow = Arrow(np.array([0, 0.6, 0]), np.array([0, -0.6, 0]), buff=0.1)
        self.play(Create(arrow), run_time=2)
        self.wait(2)

        self.draw_graph()
        return super().construct()


class Beats(Scene):
    def draw_graph(self, ele, freq):
        axes = Axes(
            x_range=[-1, 4, 5],
            y_range=[-1, 1, 2],
            x_length=5,
            y_length=2,
            axis_config={'include_numbers': True,
                         'numbers_to_exclude': [0]},
            x_axis_config={'color': ORANGE},
            y_axis_config={'color': ORANGE},
        ).add_coordinates()
        axes.next_to(ele, RIGHT, buff=0.5)
        # self.add(axes)
        # self.play(DrawBorderThenFill(axes))

        graph = axes.plot(lambda x: np.sin(freq*x),
                          x_range=[0, 3.85], color=YELLOW)
        # self.play(Create(graph), run_time=5)

        # self.wait(5)
        return axes, graph

    def beat_ske(self, name, pos, freq):
        ele = Text(name, font_size=30)
        ele.move_to(pos)
        # self.play(Write(ele), run_time=2)
        axes, graph = self.draw_graph(ele, freq)
        return ele, axes, graph

    def A_beat(self, pos):
        ele, axes, graph = self.beat_ske("A", pos, freq=5.5)
        self.play(Write(ele), run_time=2)
        self.wait(2)
        self.play(DrawBorderThenFill(axes))
        self.play(Create(graph), run_time=5)

    # def B_beat(self):

    def construct(self):
        self.A_beat([-6.5, 2.5, 0])
        eles = [
            # Char | Pos          | Freq
            # A    [-6.5, 2.5, 0], 1.254
            ("B",   [-6.5, 0, 0],   1.12),
            ("C",   [-6.5, -2.5, 0], 2.10),
            ("D",   [0, -2.5, 0],   1.87),
            ("E",   [0, 0, 0],      0.837),
            ("F",   [0, 2.5, 0],    0.739),
        ]

        ele_lst = []
        for char, pos, freq in eles:
            ele_lst.append(self.beat_ske(char, pos, freq))
        vectr_grps = [VGroup(*i) for i in zip(*ele_lst)]

        self.play(*[Write(i) for i in vectr_grps[0]], run_time=5)
        self.wait(5)
        self.play(DrawBorderThenFill(vectr_grps[1]), run_time=3)
        self.play(Create(vectr_grps[2]), run_time=8)
        self.wait(5)
        return super().construct()


class FourierTransformIntro(Scene):

    def draw_graph(self):
        axes = Axes(
            x_range=[-1, 22, 2],
            y_range=[-3.1415, 3.1415, 2],
            x_length=10,
            y_length=2,
            axis_config={'include_numbers': True, 'numbers_to_exclude': [0]},
            x_axis_config={'color': ORANGE},
            y_axis_config={'color': ORANGE},
        ).add_coordinates()
        axes.to_edge(UP)
        self.play(DrawBorderThenFill(axes))

        graph = axes.plot(lambda x: np.sin(x)+np.sin(3*x)-np.cos(x)+np.sin(5*x),
                          x_range=[0, 20], color=YELLOW)
        sin_gph = axes.plot(lambda x: np.sin(x), x_range=[0, 20], color=RED)
        cos_gph = axes.plot(lambda x: -np.cos(x),
                            x_range=[0, 20], color=ORANGE)
        sin3_gph = axes.plot(lambda x: np.sin(
            3*x), x_range=[0, 20], color=GREEN)
        sin5_gph = axes.plot(lambda x: np.sin(
            5*x), x_range=[0, 20], color=BLUE)

        sin_gph.next_to(graph, DOWN, buff=0.5)
        cos_gph.next_to(sin_gph, DOWN, buff=0.5)
        sin3_gph.next_to(cos_gph, DOWN, buff=0.5)
        sin5_gph.next_to(sin3_gph, DOWN, buff=0.5)

        self.play(Create(graph), run_time=5)

        self.play(Create(sin_gph), run_time=5)
        self.play(Create(cos_gph), run_time=3)
        self.play(Create(sin3_gph), run_time=3)
        self.play(Create(sin5_gph), run_time=3)

        self.wait(5)

    def construct(self):
        self.draw_graph()
        return super().construct()


class FourierTransform2(Scene):
    def draw_graph(self):
        axes = Axes(
            x_range=[-1, 22, 2],
            y_range=[-3.1415, 3.1415, 2],
            x_length=10,
            y_length=3,
            axis_config={'include_numbers': True, 'numbers_to_exclude': [0]},
            x_axis_config={'color': ORANGE},
            y_axis_config={'color': ORANGE},
        ).add_coordinates()
        axes.to_edge(DOWN)
        self.play(DrawBorderThenFill(axes))

        graph = axes.plot(lambda x: np.sin(x)+np.sin(3*x)-np.cos(x)+np.sin(5*x),
                          x_range=[0, 20], color=YELLOW)
        self.play(Create(graph), run_time=5)

    def Four_transform(self):
        def integrand(x, t):
            g = sin(x) + sin(3*x) - cos(x) + sin(5*x)
            return g*cos(x*t)

        axes = Axes(
            x_range=[-1, 22, 1],
            y_range=[-10, 10, 5],
            x_length=10,
            y_length=3,
            axis_config={'include_numbers': True,
                         'numbers_to_exclude': [0, -1]},
            x_axis_config={'color': YELLOW},
            y_axis_config={'color': YELLOW},
        ).add_coordinates()
        axes.to_edge(UP)
        self.play(DrawBorderThenFill(axes))
        gph = axes.plot(lambda t: quad(integrand, 0, 10, args=t)[0]*1.5,
                        x_range=[0, 20], color=RED)
        self.play(Create(gph))
        self.wait(5)

    def construct(self):
        self.draw_graph()

        arrow = Arrow(np.array([0, -0.3, 0]), np.array([0, 1, 0]), buff=0.1)
        self.play(Create(arrow), run_time=2)
        txt = Text("Fourier Transform", font="Arial", font_size=30)
        txt.next_to(arrow, RIGHT, buff=0.5)
        self.play(Write(txt), run_time=2)
        self.wait(2)

        self.Four_transform()
        return super().construct()


class FourierFormula(Scene):
    def construct(self):
        txt = Text("Fourier Transform =", font_size=30)
        txt.move_to(np.array([0, 1, 0]))
        self.play(Write(txt), run_time=2)
        self.wait(3)
        formula = Tex(
            r"\[\int_{x_1}^{x_2} g(x) e^{-2\pi i f t} \, dx\]", font_size=54)
        formula.next_to(txt, DOWN, buff=0.5)
        self.play(Write(formula))
        self.wait(5)
        return super().construct()


class Ques(Scene):
    def construct(self):
        txt = Text("How can I use this to draw?", font_size=42)
        # txt.to_edge(UP+LEFT)
        self.play(Write(txt), run_time=5)
        self.wait(2)
        return super().construct()


class Refresher(Scene):
    def construct(self):
        txt = Text("Refresher", font_size=42)
        txt.to_edge(UP)
        self.play(Write(txt), run_time=5)
        self.wait(2)
        txt = Text(
            "Let's revisit what we have seen, I swear we are getting into the drawing!", font_size=30)
        txt.move_to(np.array([0, 2, 0]))
        self.play(Write(txt), run_time=5)
        self.wait(2)

        txt_des = Text("""
        We have seen that how we can change the function from time domain to frequency.
        In simpler terms we have seen how we can seperate the Bigger wave into smaller waves.
        This is a simple yet useful insight we need to draw the surface.
        """, font_size=20)
        self.play(Write(txt_des), run_time=10)

        txt_des.next_to(txt, DOWN, buff=0.5)

        return super().construct()


class Drawing(Scene):
    def draw_heart(self):
        surf = ParametricFunction(
            lambda t: np.array([
                16*sin(t) * 16*sin(t) * 16*sin(t),
                13*cos(t)-5*cos(2*t)-2*cos(3*t)-cos(4*t),
                0]),
            t_range=[0, 20*PI], color=RED)
        axes = ThreeDAxes()
        self.add(surf)
        # self.play(DrawBorderThenFill(axes))
        self.wait()
        # self.play(ShowCreation(surf), run_time=5)

    def construct(self):
        self.draw_heart()
        return super().construct()


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        # circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen
