import imageio.v2 as imageio
import matplotlib.pyplot as plt

import rplanpy


def test_functions(file: str, out_file: str = 'example_graph.png', plot_original: bool = True) -> None:
    data = rplanpy.data.RplanData(file)
    ncols = 3 if plot_original else 2
    fig, ax = plt.subplots(nrows=1, ncols=ncols, figsize=(15, 5))
    if plot_original:
        image = imageio.imread(file)
        ax[0].imshow(image)
        ax[0].axis("off")
        ax[0].set_title("Original image")
    rplanpy.plot.plot_floorplan(data, ax=ax[plot_original+0], title="Rooms and doors")
    ax = rplanpy.plot.plot_floorplan_graph(
        data=data, with_colors=True, edge_label='door', ax=ax[plot_original+1],
        title="Building graph"
    )
    plt.tight_layout()
    plt.savefig(out_file)

    plt.show()


if __name__ == '__main__':
    file = 'example.png'
    test_functions(file, out_file='example_graph.png', plot_original=True)
