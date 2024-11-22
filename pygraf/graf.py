import matplotlib.pyplot as plt


class Graf:
    categories = []
    values = []
    color_val = "#000000"

    def init(self, categories, values, color_val):
        self.categories = categories
        self.values = values
        self.color_val = color_val

    def draw_graph(self):
        # Sorting the data for largest values at the top
        sorted_data = sorted(zip(self.values, self.categories), reverse=True)
        sorted_values, sorted_categories = zip(*sorted_data)

        # Plotting
        plt.figure(figsize=(16, 12))
        bars = plt.barh(
            sorted_categories[::-1], sorted_values[::-1], color=self.color_val
        )  # Set alpha to 1.0 for no transparency

        plt.xticks(
            range(0, max(sorted_values) + 10, 10),
            [f"{x}%" for x in range(0, max(sorted_values) + 10, 10)],
            fontweight="bold",
            fontsize=16,
        )

        plt.gca().set_yticks(
            range(len(sorted_categories))
        )  # Set y-ticks to match categories
        plt.gca().set_yticklabels(
            sorted_categories[::-1], fontweight="bold", fontsize=16
        )

        # Adding values on the bars
        for bar in bars:
            plt.text(
                bar.get_width() + 1,
                bar.get_y() + bar.get_height() / 2,
                f"{bar.get_width()}%",
                va="center",
                fontweight="bold",
                fontsize=14,
            )

        plt.box(False)

    def show_graph(self):
        self.draw_graph()
        plt.show()

    def save_graph_to_file(self, fileName):
        if fileName is None or fileName == "":
            return
        self.draw_graph()
        plt.savefig(fileName, dpi=300)

    def save_graph_as_tight_layout(self, fileName):
        if fileName is None or fileName == "":
            return
        self.draw_graph()
        plt.tight_layout()
        plt.savefig(fileName, dpi=300)
