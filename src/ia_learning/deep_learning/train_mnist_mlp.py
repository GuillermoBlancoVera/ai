"""Train a small neural network on MNIST with PyTorch."""

from pathlib import Path

import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms


class MLP(nn.Module):
    """A tiny multilayer perceptron for 28x28 grayscale images."""

    def __init__(self) -> None:
        super().__init__()
        self.network = nn.Sequential(
            nn.Flatten(),
            nn.Linear(28 * 28, 128),
            nn.ReLU(),
            nn.Linear(128, 10),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.network(x)


def train_one_epoch(
    model: nn.Module,
    loader: DataLoader,
    loss_fn: nn.Module,
    optimizer: torch.optim.Optimizer,
    device: torch.device,
) -> float:
    model.train()
    total_loss = 0.0

    for images, labels in loader:
        images = images.to(device)
        labels = labels.to(device)

        predictions = model(images)
        loss = loss_fn(predictions, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    return total_loss / len(loader)


def evaluate(model: nn.Module, loader: DataLoader, device: torch.device) -> float:
    model.eval()
    correct = 0
    total = 0

    with torch.no_grad():
        for images, labels in loader:
            images = images.to(device)
            labels = labels.to(device)
            predictions = model(images).argmax(dim=1)
            correct += (predictions == labels).sum().item()
            total += labels.size(0)

    return correct / total


def main() -> None:
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    data_dir = Path("data/raw")

    transform = transforms.ToTensor()
    train_dataset = datasets.MNIST(data_dir, train=True, download=True, transform=transform)
    test_dataset = datasets.MNIST(data_dir, train=False, download=True, transform=transform)

    train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=256)

    model = MLP().to(device)
    loss_fn = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    print(f"Deep learning: MNIST MLP on {device}")
    for epoch in range(1, 4):
        loss = train_one_epoch(model, train_loader, loss_fn, optimizer, device)
        accuracy = evaluate(model, test_loader, device)
        print(f"Epoch {epoch}: loss={loss:.4f}, test_accuracy={accuracy:.3f}")

    Path("models").mkdir(exist_ok=True)
    torch.save(model.state_dict(), "models/mnist_mlp.pt")
    print("Saved model to models/mnist_mlp.pt")


if __name__ == "__main__":
    main()
