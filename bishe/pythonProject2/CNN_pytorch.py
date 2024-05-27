import matplotlib.pylab as plt
from matplotlib import cm
from matplotlib import image
from matplotlib import pyplot
import numpy as np
import pandas as pd
from time import time
from scipy import stats
from sklearn import metrics
import torch
from torch import nn
import torch.nn.functional as F
from torch.autograd import Variable
import torch.utils.data as data_utils
import torch.optim as optim
from torch.nn import Linear, ReLU, CrossEntropyLoss, Sequential, Conv2d, MaxPool2d, Module, Softmax, BatchNorm2d, \
    Dropout2d
from torch.optim import Adam, SGD
from sklearn.metrics import f1_score, precision_score, recall_score
from sklearn.utils import class_weight

print(torch.cuda.is_available())
data1_path = 'MHEALTHDATASET/mHealth_subject1.log'
data2_path = 'MHEALTHDATASET/mHealth_subject2.log'
data3_path = 'MHEALTHDATASET/mHealth_subject3.log'
data4_path = 'MHEALTHDATASET/mHealth_subject4.log'
data5_path = 'MHEALTHDATASET/mHealth_subject5.log'
data6_path = 'MHEALTHDATASET/mHealth_subject6.log'
data7_path = 'MHEALTHDATASET/mHealth_subject7.log'
data8_path = 'MHEALTHDATASET/mHealth_subject8.log'
data9_path = 'MHEALTHDATASET/mHealth_subject9.log'
data10_path = 'MHEALTHDATASET/mHealth_subject10.log'

columns = [
    'acc_chest_x', 'acc_chest_y', 'acc_chest_z',  # 胸部加速度
    'acc_ankle_l_x', 'acc_ankle_l_y', 'acc_ankle_l_z',  # 左脚踝加速度
    'gyro_ankle_l_x', 'gyro_ankle_l_y', 'gyro_ankle_l_z',  # 左脚踝角速度
    'mag_ankle_l_x', 'mag_ankle_l_y', 'mag_ankle_l_z',  # 左脚踝磁力计
    'acc_arm_x', 'acc_arm_y', 'acc_arm_z',
    'gyro_arm_x', 'gyro_arm_y', 'gyro_arm_z',  # 右下臂角速度
    'mag_arm_x', 'mag_arm_y', 'mag_arm_z',  # 右下臂磁力计
    'activity_label'
]

data1 = pd.read_csv(data1_path, delimiter=r'\s+', header=None, names=columns)
data2 = pd.read_csv(data2_path, delimiter=r'\s+', header=None, names=columns)
data3 = pd.read_csv(data3_path, delimiter=r'\s+', header=None, names=columns)
data4 = pd.read_csv(data4_path, delimiter=r'\s+', header=None, names=columns)
data5 = pd.read_csv(data5_path, delimiter=r'\s+', header=None, names=columns)
data6 = pd.read_csv(data6_path, delimiter=r'\s+', header=None, names=columns)
data7 = pd.read_csv(data7_path, delimiter=r'\s+', header=None, names=columns)
data8 = pd.read_csv(data8_path, delimiter=r'\s+', header=None, names=columns)
data9 = pd.read_csv(data9_path, delimiter=r'\s+', header=None, names=columns)
data10 = pd.read_csv(data10_path, delimiter=r'\s+', header=None, names=columns)

data_train = pd.concat([data1, data2, data3, data4, data5, data6])
data_val = pd.concat([data7, data8])
data_test = pd.concat([data9, data10])

x_train = data_train.drop('activity_label', axis=1)
x_val = data_val.drop('activity_label', axis=1)
x_test = data_test.drop('activity_label', axis=1)
y_train = data_train['activity_label'].values
y_val = data_val['activity_label'].values
y_test = data_test['activity_label'].values


def windowz(data, size, step):
    start = 0
    while start < len(data):
        yield start, start + size
        start += step


def segment_opp(inputs, targets, window_size, step):
    segments = np.zeros(((len(inputs) - window_size) // step + 1, window_size, 21))
    labels = np.zeros(((len(targets) - window_size) // step + 1))
    i_segment = 0
    i_label = 0
    for (start, end) in windowz(inputs, window_size, step):
        if len(inputs[start:end]) == window_size:
            m = stats.mode(y_train[start:end])
            segments[i_segment] = x_train[start:end]
            labels[i_label] = m[0]
            i_label += 1
            i_segment += 1
    return segments, labels


window_size = 50
step = 25
print("segmenting signal...")
train_x, train_y = segment_opp(x_train, y_train, window_size, step)
val_x, val_y = segment_opp(x_val, y_val, window_size, step)
test_x, test_y = segment_opp(x_test, y_test, window_size, step)

num_features = 21
train_x = train_x.reshape(len(train_x), 1, window_size, num_features)
val_x = val_x.reshape(len(val_x), 1, window_size, num_features)
test_x = test_x.reshape(len(test_x), 1, window_size, num_features)

train_y0 = np.array(train_y)
val_y0 = np.array(val_y)
test_y0 = np.array(test_y)

train_x = torch.from_numpy(train_x).float()
train_y = torch.from_numpy(train_y).long()

val_x = torch.from_numpy(val_x).float()
val_y = torch.from_numpy(val_y).long()

test_x = torch.from_numpy(test_x).float()
test_y = torch.from_numpy(test_y).long()

training_data = data_utils.TensorDataset(train_x, train_y)
valid_data = data_utils.TensorDataset(val_x, val_y)
testing_data = data_utils.TensorDataset(test_x, test_y)

train_loader = torch.utils.data.DataLoader(dataset=training_data, batch_size=400,
                                           shuffle=True)

val_loader = torch.utils.data.DataLoader(dataset=valid_data, batch_size=400,
                                         shuffle=False)

test_loader = torch.utils.data.DataLoader(dataset=testing_data, batch_size=400,
                                          shuffle=False)

dataloaders = [train_loader, val_loader, test_loader]
print(val_x.shape)

class_weights0 = class_weight.compute_class_weight('balanced',
                                                   classes=np.unique(train_y0),
                                                   y=train_y0)

class_weights1 = class_weight.compute_class_weight('balanced',
                                                   classes=np.unique(val_y0),
                                                   y=val_y0)

class_weights2 = class_weight.compute_class_weight('balanced',
                                                   classes=np.unique(test_y0),
                                                   y=test_y0)


def compute_conv_dim(dim_size, kernel_size, padding, stride):
    return int((dim_size - kernel_size + 2 * padding) / stride + 1)


class Conv2Net(nn.Module):
    def __init__(self, num_filters_1, num_filters_2, num_filters_3,
                 kernel_size_1, kernel_size_2, kernel_size_3, num_l1):
        super(Conv2Net, self).__init__()
        num_classes = 13
        channels = train_x.shape[1]
        height = train_x.shape[2]
        width = train_x.shape[3]
        stride = 1
        padding = 0
        max_pool_size = 2
        max_pool_stride = 2

        self.max_pool = MaxPool2d(kernel_size=max_pool_size, stride=max_pool_stride)
        self.conv_1 = Conv2d(in_channels=channels, out_channels=num_filters_1, kernel_size=(kernel_size_1, 1),
                             stride=stride,
                             padding=padding)
        self.conv_out_height = compute_conv_dim(height, kernel_size_1, padding, stride) // max_pool_size
        self.conv_out_width = compute_conv_dim(width, 1, padding, stride) // max_pool_size
        self.bn1 = nn.BatchNorm2d(num_features=num_filters_1)

        self.conv_2 = Conv2d(in_channels=num_filters_1, out_channels=num_filters_2, kernel_size=(kernel_size_2, 1),
                             stride=stride, padding=padding)
        self.conv_out_height = compute_conv_dim(self.conv_out_height, kernel_size_2, padding, stride) // max_pool_size
        self.conv_out_width = compute_conv_dim(self.conv_out_width, 1, padding, stride) // max_pool_size
        self.bn2 = nn.BatchNorm2d(num_features=num_filters_2)

        self.l1_in_features = num_filters_2 * self.conv_out_height * self.conv_out_width

        self.l_1 = Linear(in_features=self.l1_in_features,
                          out_features=num_l1)

        self.bn4 = nn.BatchNorm1d(num_features=num_l1)

        self.l_out = Linear(in_features=num_l1,
                            out_features=num_classes)

        self.dropout = Dropout2d(p=0.5)

    def forward(self, x):
        x = x.cuda()
        x = F.relu(self.bn1(self.conv_1(x)))
        x = self.max_pool(x)
        x = F.relu(self.bn2(self.conv_2(x)))
        x = self.max_pool(x)

        x = x.view(-1, self.l1_in_features)

        x = F.relu(self.bn4(self.l_1(x)))
        x = self.dropout(x)

        return F.log_softmax(self.l_out(x), dim=1)


class EarlyStopping:
    """Early stops the training if validation loss doesn't improve after a given patience."""

    def __init__(self, patience=7, verbose=False, delta=0):
        """
        Args:
            patience (int): How long to wait after last time validation loss improved.
                            Default: 7
            verbose (bool): If True, prints a message for each validation loss improvement.
                            Default: False
            delta (float): Minimum change in the monitored quantity to qualify as an improvement.
                            Default: 0
        """
        self.patience = patience
        self.verbose = verbose
        self.counter = 0
        self.best_score = None
        self.early_stop = False
        self.val_loss_min = np.Inf
        self.delta = delta

    def __call__(self, val_loss, model):

        score = -val_loss

        if self.best_score is None:
            self.best_score = score
            self.save_checkpoint(val_loss, model)
        elif score < self.best_score + self.delta:
            self.counter += 1
            print(f'EarlyStopping counter: {self.counter} out of {self.patience}')
            if self.counter >= self.patience:
                self.early_stop = True
        else:
            self.best_score = score
            self.save_checkpoint(val_loss, model)
            self.counter = 0

    def save_checkpoint(self, val_loss, model):
        '''Saves model when validation loss decrease.'''
        if self.verbose:
            print(f'Validation loss decreased ({self.val_loss_min:.6f} --> {val_loss:.6f}).  Saving model ...')
        # torch.save(model.state_dict(), 'checkpoint.pt')
        torch.save(model, 'drive/My Drive/ML final project/checkpoint50finalf.pt')
        self.val_loss_min = val_loss


def train(model, device, train_loader, optimizer, epoch):
    model.train()
    losses = []
    for batch_idx, (data, target) in enumerate(train_loader):
        data = data.float()
        target = target.long()
        data = data.to(device)
        target = target.to(device)
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        output = model(data)
        weights = class_weights0
        class_weights = torch.FloatTensor(weights).cuda()
        loss = F.cross_entropy(output, target, weight=class_weights)
        # loss = F.nll_loss(output, target, weight=class_weights)
        loss.backward()
        optimizer.step()
        if batch_idx % 50 == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(train_loader.dataset),
                       100. * batch_idx / len(train_loader), loss.item()))
            losses.append(loss.item())
    return losses


def test(model, device, data_loader):
    model.eval()
    test_loss = 0
    f1 = 0
    precision = 0
    recall = 0
    correct = 0
    i = 0
    with torch.no_grad():
        for data, target in data_loader:
            data = data.to(device)
            output = model(data)
            i += 1
            weights = class_weights1
            class_weights = torch.FloatTensor(weights).cuda()

            # test_loss += F.nll_loss(output, target.to(device), weight=class_weights, reduction='sum').item() # sum up batch loss
            test_loss += F.cross_entropy(output, target.to(device), weight=class_weights,
                                         reduction='sum').item()  # sum up batch loss
            pred = output.argmax(dim=1, keepdim=True)  # get the index of the max log-probability
            pred = pred.cpu()
            correct += pred.eq(target.view_as(pred)).sum().item()
            f1 += f1_score(pred, target, average='macro')
            precision += precision_score(pred, target, average='macro')
            recall += recall_score(pred, target, average='macro')
    test_loss /= len(data_loader.dataset)
    f1 = f1 / i
    precision = precision / i
    recall = recall / i
    print(
        '\nTest set: Average loss: {:.4f}, Precision: {:.4f}, Recall: {:.4f}, F1 score: {:.4f},   Accuracy: {}/{} ({:.0f}%)\n'.format(
            test_loss, precision, recall, f1, correct, len(data_loader.dataset),
            100. * correct / len(data_loader.dataset)))
    return test_loss


use_cuda = torch.cuda.is_available()
device = torch.device('cuda:0')
model = Conv2Net(256, 128, 128, 6, 6, 4, 128).to(device)
# optimizer = torch.optim.SGD(model.parameters(), lr=0.001, momentum=0.5, weight_decay=0.00001)
optimizer = torch.optim.Adam(model.parameters(), lr=0.0005)
epoch = 200
train_losses = []
val_losses = []
# initialize the early_stopping object
early_stopping = EarlyStopping(patience=20, verbose=True)
t0 = time()
for i in range(epoch):
    train_loss = train(model, device, train_loader, optimizer, i)
    train_losses.extend(train_loss)
    val_loss = test(model, device, val_loader)
    val_losses.append(val_loss)
    # early_stopping needs the validation loss to check if it has decresed,
    # and if it has, it will make a checkpoint of the current model
    early_stopping(val_loss, model)

    if early_stopping.early_stop:
        print("Early stopping")
        break

    # load the last checkpoint with the best model
    last_model = torch.load('drive/My Drive/ML final project/checkpoint50finalf.pt')
    # model.load_state_dict(torch.load('checkpoint.pt'))
print("training time:", round(time() - t0, 3), "s")
