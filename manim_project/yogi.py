from manim import *

class SystemDesign(Scene):
    def construct(self):
        # Creating nodes (Rectangle) with labels (Text)
        node_1 = self.create_node("1 Structure is Important", LEFT)
        node_1_1 = self.create_node("1.1 [4] Architecture Review", LEFT + 2 * DOWN)
        node_1_1_1 = self.create_node("1.1.1 Infra Arch", LEFT + 3 * DOWN)
        node_1_1_1_1 = self.create_node("1.1.1.1 Eh ini nanti kita handle datanya ...", LEFT + 4 * DOWN)
        node_1_1_2 = self.create_node("1.1.2 Sec Arch", LEFT + 3 * DOWN)
        node_1_1_2_1 = self.create_node("1.1.2.1 Loh kok ini MD5 gampang banget ...", LEFT + 4 * DOWN)

        node_1_2 = self.create_node("1.2 [5] Api Specification", RIGHT + 2 * DOWN)
        node_1_2_1 = self.create_node("1.2.1 Real Example : dari 1 screen tadi { correct }", RIGHT + 3 * DOWN)
        node_1_2_1_1 = self.create_node("1.2.1.1 Butuh berapa API ? Misalkan butuh 2 API ...", RIGHT + 4 * DOWN)

        # Connecting nodes with arrows
        self.play(
            Write(node_1),
            Write(node_1_1),
            Write(node_1_2)
        )

        self.play(
            self.create_arrow(node_1, node_1_1),
            self.create_arrow(node_1, node_1_2),
        )

        self.play(
            Write(node_1_1_1),
            Write(node_1_1_2)
        )

        self.play(
            self.create_arrow(node_1_1, node_1_1_1),
            self.create_arrow(node_1_1, node_1_1_2),
        )

        self.play(
            Write(node_1_1_1_1)
        )

        self.play(
            self.create_arrow(node_1_1_1, node_1_1_1_1)
        )

        self.play(
            Write(node_1_2_1),
            Write(node_1_2_1_1)
        )

        self.play(
            self.create_arrow(node_1_2, node_1_2_1),
            self.create_arrow(node_1_2_1, node_1_2_1_1),
        )

        # Add some final touches, like setting the background color to white for modern UI
        self.camera.background_color = WHITE

    def create_node(self, text, position):
        """Helper function to create nodes with a rectangle and text"""
        rect = Rectangle(width=6, height=1.5, color=BLUE, fill_opacity=0.5)
        label = Text(text).scale(0.5).move_to(rect.get_center())
        node = VGroup(rect, label)
        node.move_to(position)
        return node

    def create_arrow(self, start_node, end_node):
        """Helper function to create arrows between nodes"""
        start = start_node.get_center()
        end = end_node.get_center()
        arrow = Arrow(start=start, end=end, color=BLACK)
        return arrow

# Run the scene with the following command:
# manim -ql yogi.py SystemDesign
