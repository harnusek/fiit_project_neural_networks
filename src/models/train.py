from argparse import ArgumentParser

# import os
# from src.models.model import LSTMrecommender
import yaml
import numpy as np


def train_and_validate(train_x, train_y, test_x, test_y, model=None):
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy'])

    model.fit(
        x=train_x,
        y=train_y,
        batch_size=10,
        epochs=30,
        validation_data=(test_x, test_y))


def main():
    parser = ArgumentParser(
        description='Script fits LSTMRec on train data. Hyperparameters can be defined as arguments.'
                    'Unspecified hyperparameters will be generated randomly.'
                    'Use -d to force default hyperparameters to be used.')
    parser.add_argument('-d', '--default', help='Forces the use of default hyperparameters', action="store_true")
    parser.add_argument('--emb-dim', type=int, help='Length of item embedding')
    parser.add_argument('--lstm-units', type=int, help='Count of LSTM units')
    parser.add_argument('--lstm-activation', type=str, help='LSTM activation function')
    parser.add_argument('--lstm-recurrent-activation', type=str, help='Activation function of recurrent units')
    parser.add_argument('--lstm-dropout', type=float,
                        help='Fraction of the units to drop for the linear transformation of the LSTM inputs')
    parser.add_argument('--lstm-recurrent-dropout', type=float,
                        help='Fraction of the units to drop for the linear transformation of the recurrent state')
    parser.add_argument('--dense-activation', type=str, help='Dense layer activation function')
    parser.add_argument('--batch-size', type=int, help='Batch size')
    parser.add_argument('--learning-rate', type=float, help='Learning rate of Adam optimizer')
    parser.add_argument('--adam-beta-1', type=float, help='Beta 1 parameter of Adam optimizer')
    parser.add_argument('--adam-beta-2', type=float, help='Beta 2 parameter of Adam optimizer')
    parser.add_argument('--adam-epsilon', type=float, help='Epsilon parameter of Adam optimizer')
    args = parser.parse_args()
    hparams = {}

    if args.default:
        with open('hparams.yaml') as f_hparams:
            hparams = yaml.safe_load(f_hparams)
            print(type(hparams))
    else:
        if args.emb_dim is not None:
            hparams['emb_dim'] = args.emb_dim
        else:
            hparams['emb_dim'] = 50 * np.random.randint(1, 11)

        if args.lstm_units is not None:
            hparams['lstm_units'] = args.lstm_units
        else:
            hparams['lstm_units'] = 25 * np.random.randint(1, 13)

        if args.lstm_activation is not None:
            hparams['lstm_activation'] = args.lstm_activation
        else:
            hparams['lstm_activation'] = ['relu', 'sigmoid', 'tanh', 'linear', 'softmax'][np.random.randint(0, 5)]

        if args.lstm_recurrent_activation is not None:
            hparams['lstm_recurrent_activation'] = args.lstm_recurrent_activation
        else:
            hparams['lstm_recurrent_activation'] = ['relu', 'sigmoid', 'tanh', 'linear', 'softmax'][np.random.randint(0, 5)]

        if args.lstm_dropout is not None:
            hparams['lstm_dropout'] = args.lstm_dropout
        else:
            hparams['lstm_dropout'] = 0.05 * np.random.randint(1, 11)

        if args.lstm_recurrent_dropout is not None:
            hparams['lstm_recurrent_dropout'] = args.lstm_recurrent_dropout
        else:
            hparams['lstm_recurrent_dropout'] = 0.05 * np.random.randint(1, 11)

        if args.dense_activation is not None:
            hparams['dense_activation'] = args.dense_activation
        else:
            hparams['dense_activation'] = ['relu', 'sigmoid', 'tanh', 'linear', 'softmax'][np.random.randint(0, 5)]

        if args.batch_size is not None:
            hparams['batch_size'] = args.batch_size
        else:
            hparams['batch_size'] = 2 ** (np.random.randint(3, 11))

        if args.learning_rate is not None:
            hparams['learning_rate'] = args.learning_rate
        else:
            hparams['learning_rate'] = 10 ** (-np.random.randint(2, 5))

        if args.adam_beta_1 is not None:
            hparams['adam_beta_1'] = args.adam_beta_1
        else:
            hparams['adam_beta_1'] = 0.05 * (np.random.randint(14, 25))

        if args.adam_beta_2 is not None:
            hparams['adam_beta_2'] = args.adam_beta_2
        else:
            hparams['adam_beta_2'] = 0.05 * (np.random.randint(14, 25)) - 0.001

        if args.adam_epsilon is not None:
            hparams['adam_epsilon'] = args.adam_epsilon
        else:
            hparams['adam_epsilon'] = 10 ** (-np.random.randint(6, 11))


if __name__ == "__main__" and __package__ is None:
    from sys import path
    from os.path import dirname as dir

    path.append(dir(path[0]))
    __package__ = "examples"

if __name__ == "__main__":
    main()
