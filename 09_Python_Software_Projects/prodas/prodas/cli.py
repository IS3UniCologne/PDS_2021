import click
from . import model


@click.command()
@click.option("--train/--no-train", default=False, help="Train the model")
def main(train):
    if train:
        model.create_model()
    else:
        print("Don't do anything.")


if __name__ == "__main__":
    main()

