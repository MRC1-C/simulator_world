import torch
def train(model,loss_fn, optimizer, data_train=[], data_test=[],device='cpu'):
    size = len(data_train.dataset)
    model.train()
    for batch, (X, y) in enumerate(data_train):
        X,y = X.to(device), y.to(device)
        pred = model(X)
        loss = loss_fn(pred, y)
        # Backpropagation
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if batch % 10 == 0:
            loss_, current = loss.item(), batch * len(X)
            print(f"loss: {loss_:>7f}  [{current:>5d}/{size:>5d}]")
    return loss.item()