import numpy as np
import csv

RND_MEAN = 0
RND_STD = 0.003
LEARNING_RATE = 0.0001

def load_dataset():
    global data, input_cnt, ouput_cnt
    with open('./data/abalone.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader, None)
        rows = []
        for row in csv_reader:
            rows.append(row)
    input_cnt, ouput_cnt = 10, 1
    data = np.zeros([len(rows), input_cnt + ouput_cnt])
    
    for n, row in enumerate(rows):
        if row[0] == "I":
            data[n, 0] = 1
        if row[0] == "M":
            data[n, 1] = 1
        if row[0] == "F":
            data[n, 2] = 1
        data[n, 3:] = row[1:]
    
def init_model():
    global weight, bias, input_cnt, ouput_cnt
    weight = np.random.normal(RND_MEAN, RND_STD, [input_cnt, ouput_cnt])
    bias = np.zeros([ouput_cnt])

def train_and_test(epoch_count=10, mb_size = 10):
    step_cout = arrange_data(mb_size)
    test_x, test_y = get_data_test()
    
    # 2. 학습
    for epoch in range(epoch_count):
        losses = []
        accs = []

        for n in range(step_cout):
            train_x, train_y = get_train_data(mb_size, n)
            loss, acc = run_train(train_x, train_y)
            losses.append(loss)
            accs.append(acc)

    # 3. 테스트

def run_train(x,y):
    # 순방향 => 정확도
    output, aux_nn = forward_neuralnet(x)
    loss, aux_pp = forward_postproc(output, y)
    accuracy = eval_accuracy(output, y)
    
    # 역방향 => 오차
    G_loss = 1.0
    G_output = backprop_postproc(G_loss, aux_pp)
    backprop_neuralnet(G_output, aux_nn)

    return loss, accuracy

def get_train_data(mb_size, nth):
    global data, shuffle_map, test_begin_idx, ouput_cnt
    if nth == 0:
        np.random.shuffle(shuffle_map[:test_begin_idx])
    train_data = data[shuffle_map[mb_size * nth : mb_size * (nth+1)]]
    return train_data[:, :-ouput_cnt], train_data[:, -ouput_cnt:]

def arrange_data(mb_size):
    global data, shuffle_map, test_begin_idx
    shuffle_map = np.arange(data.shape[0])
    np.random.shuffle(shuffle_map)
    step_cout = int(data.shape[0] * 0.8) // mb_size
    test_begin_idx = step_cout * mb_size
    return step_cout 

def get_data_test():
    global data, shuffle_map, test_begin_idx, ouput_cnt
    test_data = data[shuffle_map[test_begin_idx:]]
    return test_data[:, :-ouput_cnt], test_data[:, -ouput_cnt:]

if __name__ == "__main__":
    load_dataset() # CSV 파일 읽는 방법
    init_model() # 기울기와 절편
    train_and_test() # Epoch, Batch
