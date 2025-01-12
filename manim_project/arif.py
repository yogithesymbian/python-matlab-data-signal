# manim -pql arif.py SystemDesignDiagram
# manim -ql arif.py SystemDesignDiagram

from manim import *

class SystemDesignDiagram(Scene):
    def construct(self):
        # Create the main central node
        central_node = Text("1 Structure is Important", font_size=24, color=BLUE)
        self.play(Write(central_node))
        self.wait(1)

        # Position the central node in the center
        central_node.move_to(ORIGIN)

        # Left branch nodes
        left_nodes = [
            Text("1.1 [4] Architecture Review", font_size=18, color=YELLOW),
            Text("1.2 [5] Api Specification", font_size=18, color=YELLOW),
            Text("1.3 [6] Development (BE, FE, QA)", font_size=18, color=YELLOW),
            Text("1.4 [7] Non Prod Deployment", font_size=18, color=YELLOW),
            Text("1.5 [1] Business Requirement Document (BRD)", font_size=18, color=YELLOW)
        ]

        # Right branch nodes
        right_nodes = [
            Text("1.6 [2] UI / UX", font_size=18, color=GREEN),
            Text("1.7 [3] Technical Design", font_size=18, color=GREEN),
            Text("1.8 [8] Testing", font_size=18, color=GREEN),
            Text("1.9 [9] Prod Development", font_size=18, color=GREEN),
            Text("1.10 [10] Maintenance / Improvements", font_size=18, color=GREEN)
        ]

        # Add left nodes with connecting arrows
        for i, node in enumerate(left_nodes):
            node.shift(LEFT * 3 + UP * (2 - i))  # Positioning
            arrow = Arrow(central_node.get_left(), node.get_right(), buff=0.1, color=YELLOW)
            self.play(GrowArrow(arrow), Write(node))
            self.wait(0.5)

        # Add right nodes with connecting arrows
        for i, node in enumerate(right_nodes):
            node.shift(RIGHT * 3 + UP * (2 - i))  # Positioning
            arrow = Arrow(central_node.get_right(), node.get_left(), buff=0.1, color=GREEN)
            self.play(GrowArrow(arrow), Write(node))
            self.wait(0.5)

        self.wait(2)
        # End Scene
